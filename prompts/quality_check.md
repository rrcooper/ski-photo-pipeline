# quality_check

**Strategy:** Binary pass/fail technical quality screen, not a tagging
prompt.

**When to use it:** As a pre-upload gate. Intended to run as a separate
OpenAI call in parallel with tagging, with the result branching an IF
node in front of the Google Drive upload step so failed photos never get
uploaded. Drafted but not yet wired into the live workflow.

## Prompt text

```
You are screening photos for a ski school's photo library before
upload. Assess only technical quality, not content or subject matter.
Return "pass" if the photo is reasonably sharp, properly exposed, and
not blank/corrupted. Return "fail" only for severe issues: heavy
blur, extreme darkness/overexposure, or an unusable/broken image. Minor
imperfections should still pass. Return strictly valid JSON in the form
{"quality": "pass" | "fail", "reason": "..."}.
```

Returns `pass`/`fail` rather than a quality scale so it can drive a
simple workflow branch, plus a `reason` string for logging/debugging
even on a passing result.
