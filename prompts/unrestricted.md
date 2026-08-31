# unrestricted

**Strategy:** No scoping at all. The model tags anything it notices.

**When to use it:** Open-ended exploration and testing. Not recommended
for production use without reviewing output first, since it can surface
off-topic tags (e.g. unrelated background details) alongside genuinely
useful ones.

## Prompt text

```
Look at the photo and describe it using short, lowercase, single- or
double-word tags: anything relevant you can identify (subjects, equipment,
activity, weather, mood, setting, etc). You are not restricted to a predefined
list. Include the tag "hero_shot" only if this photo is strong enough
for marketing use: genuine emotion or action, a clear focal subject,
good composition, and technically clean (sharp, well-exposed). Reserve
it for standout photos, not routine documentation shots. For reference
only, here are tags already used elsewhere in this system:
{allowed_tags}. Feel free to reuse any of these if they apply, but also
include any other relevant tags you notice that aren't in that list.
Return strictly valid JSON in the form {"tags": ["tag1", "tag2"]}.
```

`{allowed_tags}` is filled in at runtime with the comma-separated list of
approved tags pulled from the `tags_whitelist` Google Sheet.
