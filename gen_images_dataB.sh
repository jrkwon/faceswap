mkdir datasets/dataB/$1
ffmpeg -i datasets/dataB/$1.mp4 -vf fps=30 datasets/dataB/$1/clip%05d.png
