temporal description

## Crop video
### Convert AVI to MP4
`for i in `cat id`; do ffmpeg -i ${i}.avi -vcodec libx264 -pix_fmt yuv420p 24_${i}.mp4; done`

### Check crop window
`ffplay -i input -vf 24_14-12-00.513.mp4 -vf "crop=350:350:750:415"`

### Crop each well position
```
#!/bin/bash

for i in `cat id`

do
videoID="${i}"
mkdir "cropped_vid" #"$videoID"
data_dir="cropped_vid" #`pwd`"/$videoID"

ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:0:415" -c:a copy ${data_dir}/${videoID}_1.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:370:415" -c:a copy ${data_dir}/${videoID}_2.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:750:415" -c:a copy ${data_dir}/${videoID}_3.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:0:35" -c:a copy ${data_dir}/${videoID}_4.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:370:35" -c:a copy ${data_dir}/${videoID}_5.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:750:35" -c:a copy ${data_dir}/${videoID}_6.mp4

done
```
