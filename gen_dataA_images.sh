mkdir datasets/dataA/$1
ffmpeg -i datasets/dataA/$1.mp4 -vf fps=30 datasets/dataA/$1/clip%05d.png
