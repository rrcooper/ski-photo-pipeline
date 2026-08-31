"""
Node: Create Prompt

Selects and fills a prompt template for the OpenAI vision call.

Input: one item per photo, each carrying `validTags` (the approved tag
whitelist) and `promptKey` (which template to use, set upstream by the
"Select Prompt Key" node).

Output: each item unchanged, with `promptText` added: the fully-formed
prompt string ready to hand to the OpenAI node.

Three tagging strategies are available, each suited to a different need:
  - "whitelist_only": tags must come from the approved list only. Useful
    when consistency with existing tags matters more than coverage (e.g.
    an instructor missed tagging a slope name that's clearly visible).
  - "ski_relevant": the model can generate any tag, but scoped to what's
    actually relevant to a ski school context. Useful for surfacing new,
    on-topic tag candidates not yet in the approved list.
  - "unrestricted": no scoping at all, the model tags anything it
    notices. Useful for open-ended exploration/testing, not recommended
    for production use without reviewing output first.

All three prompts also ask the model to apply "hero_shot", a
marketing-relevance tag reserved for standout photos (genuine
emotion/action, clear subject, good composition, technically clean).
Since it's an ordinary whitelist tag ("hero_shot" is added as a row in
the tags_whitelist Google Sheet), it flows through the same
validation/description pipeline as any other tag, with no separate node
or API call needed to surface it.

Full prompt text for each strategy is also available individually,
outside of code, in /prompts for easier review.
"""

PROMPTS = {
    "whitelist_only": (
        "You are tagging photos for a ski school's photo library. Look at the photo "
        "and the full list of allowed tags below. Return every tag that clearly "
        "applies to what's visible in the photo. Consider all categories on the "
        "list, not just ski/snow-related tags (equipment, terrain, activity, "
        "weather), also look for people-related tags (expressions, roles) and "
        "location tags if they are clearly identifiable. Include the tag "
        "\"hero_shot\" only if this photo is strong enough for marketing use: "
        "genuine emotion or action, a clear focal subject, good composition, and "
        "technically clean (sharp, well-exposed). Reserve it for standout photos, "
        "not routine documentation shots. Allowed tags: {allowed_tags}. Return "
        "strictly valid JSON in the form {{\"tags\": [\"tag1\", \"tag2\"]}}. If "
        "nothing applies, return {{\"tags\": []}}. Do not invent tags that are "
        "not in the list."
    ),
    "ski_relevant": (
        "You are tagging photos for a ski school's photo library. Look at the photo "
        "and describe it using short, lowercase, single- or double-word tags: "
        "anything relevant to a ski school context (subjects, equipment, terrain, "
        "activity, weather, people's roles, location, etc). Only include tags "
        "that would make sense in a ski school's photo library, skip anything "
        "unrelated or out of context. Include the tag \"hero_shot\" only if this "
        "photo is strong enough for marketing use: genuine emotion or action, a "
        "clear focal subject, good composition, and technically clean (sharp, "
        "well-exposed). Reserve it for standout photos, not routine documentation "
        "shots. For reference, here are tags already used elsewhere in this "
        "system, which you may reuse if they apply: {allowed_tags}. You are not "
        "limited to this list, include any other ski-school-relevant tag you "
        "notice. Return strictly valid JSON in the form "
        "{{\"tags\": [\"tag1\", \"tag2\"]}}."
    ),
    "unrestricted": (
        "Look at the photo and describe it using short, lowercase, single- or "
        "double-word tags: anything relevant you can identify (subjects, equipment, "
        "activity, weather, mood, setting, etc). You are not restricted to a predefined "
        "list. Include the tag \"hero_shot\" only if this photo is strong enough "
        "for marketing use: genuine emotion or action, a clear focal subject, "
        "good composition, and technically clean (sharp, well-exposed). Reserve "
        "it for standout photos, not routine documentation shots. For reference "
        "only, here are tags already used elsewhere in this system: "
        "{allowed_tags}. Feel free to reuse any of these if they apply, but also "
        "include any other relevant tags you notice that aren't in that list. "
        "Return strictly valid JSON in the form {{\"tags\": [\"tag1\", \"tag2\"]}}."
    ),
    "quality_check": (
        "You are screening photos for a ski school's photo library before "
        "upload. Assess only technical quality, not content or subject matter. "
        "Return \"pass\" if the photo is reasonably sharp, properly exposed, and "
        "not blank/corrupted. Return \"fail\" only for severe issues: heavy "
        "blur, extreme darkness/overexposure, or an unusable/broken image. Minor "
        "imperfections should still pass. Return strictly valid JSON in the form "
        "{{\"quality\": \"pass\" | \"fail\", \"reason\": \"...\"}}."
    ),
}
DEFAULT_PROMPT_KEY = "whitelist_only"

prompt_key = _items[0]['json'].get('promptKey', DEFAULT_PROMPT_KEY)
allowed_tags = ', '.join(row.get('tag', '') for row in _items[0]['json'].get('validTags', []))
prompt_text = PROMPTS[prompt_key].format(allowed_tags=allowed_tags)

result = []
for item in _items:
    result.append({
        'json': {
            **item['json'],
            'promptText': prompt_text
        },
        'binary': item.get('binary')
    })

return result
