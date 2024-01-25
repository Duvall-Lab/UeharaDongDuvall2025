#!/bin/bash

ls *mp4 | sed s/.mp4//g | grep h_ > id

for i in `cat id`

do
videoID="${i}"
mkdir "cropped_vid" #"$videoID"
data_dir="cropped_vid" #`pwd`"/$videoID"

ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:0:415" -c:a copy ${data_dir}/${videoID}_LVP0.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:370:415" -c:a copy ${data_dir}/${videoID}_LVP24.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:750:415" -c:a copy ${data_dir}/${videoID}_ORL0.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:0:35" -c:a copy ${data_dir}/${videoID}_ORL24.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:370:35" -c:a copy ${data_dir}/${videoID}_FOS0.mp4
ffmpeg -i ${videoID}.mp4 -vf "crop=350:350:750:35" -c:a copy ${data_dir}/${videoID}_FOS24.mp4

done