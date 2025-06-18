## Data acquisition
### Equipment
- 6-well tissue culture plates (Celltreat Scientific Products)
- 3D-printed lids (adapter_v5.stl)
- Odor delivery box (odor-delivery-box.dxf)


### Recording setting
- Camera: Machine vision camera (a2A1920-160umBAS, Basler AG, Germany)
- Lens: Arducam 8-50mm C-Mount Zoom Lens
- Frame rate: 60 fps
- Exposure time: 17000


## Crop video
### Create id file
`cd [video directory]`
`ls | grep -v 'metadata' | sed s/.avi//g | grep '-0' > id`

### Convert AVI to MP4 (for reducing data size)
`for i in `cat id`; do ffmpeg -i ${i}.avi -vcodec libx264 -pix_fmt yuv420p 24_${i}.mp4; done`

### Check crop window

1. `ffplay -i input.mp4 -vf "crop=350:350:0:415"`
1. `ffplay -i input.mp4 -vf "crop=350:350:370:415"`
1. `ffplay -i input.mp4 -vf "crop=350:350:750:415"`
1. `ffplay -i input.mp4 -vf "crop=350:350:0:35"`
1. `ffplay -i input.mp4 -vf "crop=350:350:370:35"`
1. `ffplay -i input.mp4 -vf "crop=350:350:750:35"`

### Crop each well position
run `sh crop.sh`
