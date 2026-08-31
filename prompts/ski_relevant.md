# ski_relevant

**Strategy:** The model can generate any tag, but scoped to what's
actually relevant to a ski school context.

**When to use it:** Surfacing new, on-topic tag candidates that aren't
yet in the approved list. Useful for discovering tags worth adding to
the whitelist over time, without opening the door to fully unrelated
tags.

## Prompt text

```
You are tagging photos for a ski school's photo library. Look at the photo
and describe it using short, lowercase, single- or double-word tags:
anything relevant to a ski school context (subjects, equipment, terrain,
activity, weather, people's roles, location, etc). Only include tags
that would make sense in a ski school's photo library, skip anything
unrelated or out of context. Include the tag "hero_shot" only if this
photo is strong enough for marketing use: genuine emotion or action, a
clear focal subject, good composition, and technically clean (sharp,
well-exposed). Reserve it for standout photos, not routine documentation
shots. For reference, here are tags already used elsewhere in this
system, which you may reuse if they apply: {allowed_tags}. You are not
limited to this list, include any other ski-school-relevant tag you
notice. Return strictly valid JSON in the form {"tags": ["tag1", "tag2"]}.
```

`{allowed_tags}` is filled in at runtime with the comma-separated list of
approved tags pulled from the `tags_whitelist` Google Sheet.
