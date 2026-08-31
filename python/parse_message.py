"""
Node: Parse Message

Extracts hashtags and media attachments from the raw Twilio MMS payload.

Input: a single item carrying `senderMessage` (the raw MMS webhook body)
and `validTags` (the approved tag list, merged in from a parallel branch).

Output: a single item with the sender's phone number, message SID, the
hashtags found in the message text, and a list of attached media
(url + content type). Media entries with a missing URL are dropped,
since Twilio's `NumMedia` count can occasionally overstate the number of
attachments actually present.
"""

import re

item = _items[0]['json']
body = item['senderMessage']
valid_tags = item['validTags']

num_media = int(body.get('NumMedia', 0))
media = [
    {
        'url': body.get(f'MediaUrl{i}'),
        'contentType': body.get(f'MediaContentType{i}')
    }
    for i in range(num_media)
    if body.get(f'MediaUrl{i}')  # skip entries Twilio listed but didn't attach
]

tags = [t[1:] for t in re.findall(r'#\w+', body.get('Body', ''))]

return [{
    'json': {
        'from': body.get('From'),
        'messageSid': body.get('MessageSid'),
        'tags': tags,
        'media': media,
        'validTags': valid_tags
    }
}]
