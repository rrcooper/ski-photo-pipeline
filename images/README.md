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

| File | Photographer | Link |
|---|---|---|
| andri-klopfenstein-gUXQrpuJ1kc-unsplash.jpg | [Andri Klopfenstein](https://unsplash.com/@andri77) | [Unsplash](https://unsplash.com/photos/a-person-riding-skis-down-a-snow-covered-slope-gUXQrpuJ1kc) |
| banff-sunshine-village-UoBE_wJ-suk-unsplash.jpg | [Banff Sunshine Village](https://unsplash.com/@sunshinevillage) | [Unsplash](https://unsplash.com/photos/2-person-in-yellow-jacket-and-blue-helmet-riding-ski-blades-on-snow-covered-mountain-during-UoBE_wJ-suk) |
| eirik-uhlen-U5YfxhSze8k-unsplash.jpg | [Eirik Uhlen](https://unsplash.com/@uhlen96) | [View photo](https://unsplash.com/photos/2-person-in-white-pants-and-black-snow-ski-blades-standing-on-snow-covered-ground-during-U5YfxhSze8k) |
| karsten-winegeart-wQDdaWtlByw-unsplash.jpg | [Karsten Winegeart](https://unsplash.com/@_karsten) | [View photo](https://unsplash.com/photos/person-in-blue-jacket-and-pink-pants-riding-on-snowboard-during-daytime-wQDdaWtlByw) |
| kipras-streimikis-39-0VXkvcbw-unsplash.jpg | [Kipras Štreimikis](https://unsplash.com/@kkipras) | [View photo](https://unsplash.com/photos/selective-focus-photography-of-ski-blades-on-blue-cable-car-39-0VXkvcbw) |
| ryan-fleischer-3Srp3mB75Rg-unsplash.jpg | [Ryan Fleischer](https://unsplash.com/@flyshoot) | [View photo](https://unsplash.com/photos/two-skiers-ride-a-chairlift-against-a-blue-sky-3Srp3mB75Rg) |

## Sample outputs

`outputs/` contains one JSON file per sample photo, showing the final
metadata the pipeline generates for it: the combined tag list
(instructor hashtags plus AI-generated tags) and the description string
that gets written to the file in Google Drive. These are included so the
pipeline's actual output can be reviewed without needing to run n8n.

See `outputs/example_output.json` for the expected shape.
