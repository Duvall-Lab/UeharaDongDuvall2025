temporal description

## Crop video
### Equipments and setting
- Basler
- Arducam 8-50mm C-Mount Zoom Lens
- frame rate: 60 fps
- exposure: 17000

### Create id file
`cd [video directory]`
`ls | grep -v 'metadata' | sed s/.avi//g | grep '-0' > id`

### Convert AVI to MP4
[In our environment, video is recorded as avi format and is large size. Format conversion is need.]
`for i in `cat id`; do ffmpeg -i ${i}.avi -vcodec libx264 -pix_fmt yuv420p 24_${i}.mp4; done`

### Check crop window

1. `ffplay -i input.mp4 -vf "crop=350:350:0:415"`
1. `ffplay -i input.mp4 -vf "crop=350:350:370:415"`
1. `ffplay -i input.mp4 -vf "crop=350:350:750:415"`
1. `ffplay -i input.mp4 -vf "crop=350:350:0:35"`
1. `ffplay -i input.mp4 -vf "crop=350:350:370:35"`
1. `ffplay -i input.mp4 -vf "crop=350:350:750:35"`

### Crop each well position
run `sh crop_loop.sh`
