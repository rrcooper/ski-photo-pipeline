"""
Node: Merge Tags

Combines AI-generated tags with hashtag-derived tags, and prepares the
final metadata needed for the Google Drive upload.

Input: one item per photo, combining the OpenAI response
(`aiResponseText`, extracted by the "Extract AI Response" node) with the
original message/tag data carried forward from "Create Prompt".

Output: one item per photo with a deduplicated combined tag list and a
comma-joined description string ready for Google Drive's description field.
"""

import json
import re

result = []
for item in _items:
    data = item['json']

    raw_text = data['aiResponseText']
    cleaned = re.sub(r'^```json\s*|\s*```$', '', raw_text.strip())

    try:
        ai_tags = json.loads(cleaned).get('tags', [])
    except (json.JSONDecodeError, KeyError):
        ai_tags = []  # degrade gracefully if the model returns malformed JSON

    hashtag_tags = data.get('tags', [])
    all_tags = list(dict.fromkeys(hashtag_tags + ai_tags))  # dedupe, preserves order

    media = data.get('media', {})
    media_url = media.get('url', '')
    file_name = media_url.rsplit('/', 1)[-1] if media_url else f"{data.get('messageSid')}.jpg"

    result.append({
        'json': {
            'from': data.get('from'),
            'messageSid': data.get('messageSid'),
            'fileName': file_name,
            'media': media,
            'aiTags': ai_tags,
            'allTags': all_tags,
            'driveDescription': ', '.join(all_tags)
        },
        'binary': item.get('binary')
    })

return result
