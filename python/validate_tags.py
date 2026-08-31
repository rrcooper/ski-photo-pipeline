"""
Node: Validate Tags

Filters extracted hashtags against the approved tag whitelist, using
fuzzy matching to catch likely misspellings (e.g. "silverfirchair" ->
"silver_fir_chair").

Input: one item per photo, each carrying `tags` (raw hashtags from the
message) and `validTags` (the approved whitelist, identical on every item).

Output: each item updated with `tags` replaced by only the
whitelist-approved (or corrected) tags, plus `droppedTags` and
`correctedTags` for visibility into what was filtered or auto-corrected.
"""

FUZZY_THRESHOLD = 2  # max edit distance to treat a tag as a likely typo


def levenshtein(a: str, b: str) -> int:
    """Edit distance: the number of single-character edits to turn a into b."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # deletion
                dp[i][j - 1] + 1,        # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )
    return dp[m][n]


def find_closest_match(tag: str, allowed_list: list[str]) -> tuple[str | None, float]:
    """Returns the closest whitelist match for `tag` and its edit distance."""
    best = None
    best_distance = float('inf')
    for allowed in allowed_list:
        distance = levenshtein(tag, allowed)
        if distance < best_distance:
            best_distance = distance
            best = allowed
    return best, best_distance


allowed_rows = _items[0]['json']['validTags']
allowed_tags = [str(row.get('tag', '')).strip() for row in allowed_rows if row.get('tag')]
allowed_lower = [t.lower() for t in allowed_tags]

result = []
for item in _items:
    data = item['json']
    original_tags = data.get('tags', [])

    valid_tags = []
    dropped_tags = []
    corrected_tags = []  # kept for visibility/debugging, not used downstream

    for raw_tag in original_tags:
        tag = raw_tag.lower()

        if tag in allowed_lower:
            valid_tags.append(tag)
            continue

        match, distance = find_closest_match(tag, allowed_lower)
        if match is not None and distance <= FUZZY_THRESHOLD:
            valid_tags.append(match)
            corrected_tags.append({'original': raw_tag, 'correctedTo': match, 'distance': distance})
        else:
            dropped_tags.append(raw_tag)

    result.append({
        'json': {
            **data,
            'tags': valid_tags,
            'droppedTags': dropped_tags,
            'correctedTags': corrected_tags
        }
    })

return result
