sh rename.sh
ffmpeg -r 30 -i 'datasets/dataA/idol1/%05d.png' -vcodec libx264 -crf 18 -pix_fmt yuv420p datasets/dataA/idol1/merged.mp4
