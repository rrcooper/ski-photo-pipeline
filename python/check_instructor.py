"""
Node: Check Instructor

Verifies that the MMS sender is an approved instructor.

Input: one item per row of the instructor allow-list (from Google Sheets),
each carrying the sender's phone number and the raw MMS payload as
sibling fields (stamped on by the "Add Sender Data" node upstream).

Output: a single item indicating whether the sender is allowed, plus the
sender's phone number and the original MMS message payload (passed
through so downstream nodes don't need to look back to the webhook node).
"""

sender_phone = _items[0]['json']['senderPhone']
sender_message = _items[0]['json']['senderMessage']

allowed_phones = [
    str(item['json'].get('formated_phone', '')).strip()
    for item in _items
]
is_allowed = sender_phone in allowed_phones

return [{
    'json': {
        'isAllowed': is_allowed,
        'senderPhone': sender_phone,
        'senderMessage': sender_message
    }
}]
