# Sample Photos

This folder holds sample photos used to demonstrate the pipeline, plus
the corresponding sample output for each one (see `outputs/`).

## Source & licensing

Sample photos are sourced from [Unsplash](https://unsplash.com). Under
the [Unsplash License](https://unsplash.com/license), attribution is not
legally required for standard downloads, but it's appreciated, and
crediting photographers is good practice, so each photo used here is
credited below.

**Note:** if any photo is pulled via the Unsplash API rather than a
direct download, attribution to both the photographer and Unsplash (with
a link back to the photographer's profile) is required by Unsplash's API
Terms, not just appreciated. Check which method was used for each image
before assuming the lighter, download-only terms apply.

### Attribution

| File | Photographer | Unsplash link |
|---|---|---|
| [your-filename].jpg | [Banff Sunshine Village](https://unsplash.com/@sunshinevillage) | [View photo](https://unsplash.com/photos/2-person-in-yellow-jacket-and-blue-helmet-riding-ski-blades-on-snow-covered-mountain-during-UoBE_wJ-suk) |
| andri-klopfenstein-gUXQrpuJ1kc-unsplash.jpg |  |  |
| eirik-uhlen-U5YfxhSze8k-unsplash.jpg |  |  |
| banff-sunshine-village-UoBE_wJ-suk-unsplash.jpg |  | https://unsplash.com/photos/2-person-in-yellow-jacket-and-blue-helmet-riding-ski-blades-on-snow-covered-mountain-during-UoBE_wJ-suk |
| banff-sunshine-village-ONYcbAjZq5A-unsplash.jpg |  |  |
| karsten-winegeart-L7289nHzVgI-unsplash.jpg |  |  |

Photo by <a href="https://unsplash.com/@sunshinevillage?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Banff Sunshine Village</a> on <a href="https://unsplash.com/photos/2-person-in-yellow-jacket-and-blue-helmet-riding-ski-blades-on-snow-covered-mountain-during-UoBE_wJ-suk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

_(Populate this table as photos are added. Format: "Photo by [Name] on
[Unsplash](link-to-photo-or-profile)".)_

## Sample outputs

`outputs/` contains one JSON file per sample photo, showing the final
metadata the pipeline generates for it: the combined tag list
(instructor hashtags plus AI-generated tags) and the description string
that gets written to the file in Google Drive. These are included so the
pipeline's actual output can be reviewed without needing to run n8n.

See `outputs/example_output.json` for the expected shape.
