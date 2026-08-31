# whitelist_only

**Strategy:** Tags must come from the approved list only.

**When to use it:** Consistency matters more than coverage, e.g. an
instructor sent a message but didn't hashtag a slope name that's clearly
visible in the photo. This prompt fills that gap without ever introducing
a tag outside the controlled vocabulary.

## Prompt text

```
You are tagging photos for a ski school's photo library. Look at the photo
and the full list of allowed tags below. Return every tag that clearly
applies to what's visible in the photo. Consider all categories on the
list, not just ski/snow-related tags (equipment, terrain, activity,
weather), also look for people-related tags (expressions, roles) and
location tags if they are clearly identifiable. Include the tag
"hero_shot" only if this photo is strong enough for marketing use:
genuine emotion or action, a clear focal subject, good composition, and
technically clean (sharp, well-exposed). Reserve it for standout photos,
not routine documentation shots. Allowed tags: {allowed_tags}. Return
strictly valid JSON in the form {"tags": ["tag1", "tag2"]}. If nothing
applies, return {"tags": []}. Do not invent tags that are not in the list.
```

`{allowed_tags}` is filled in at runtime with the comma-separated list of
approved tags pulled from the `tags_whitelist` Google Sheet.
