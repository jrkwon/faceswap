import glob
import os

input_files = './datasets/dataA/taeri/extracted/*.png'
#data_path = '*.png'
output_path = './datasets/dataA/taeri_triple/'
 
files = glob.glob(input_files)
print(len(files))

count = len(files)-3
if count < 0:
    print('You must have more than three files')

for i in range(count):
    os.system('convert +append {} {} {} {}{:05d}.png'.format(files[i], files[i+1], files[i+2], output_path, i))
    print(    'convert +append {} {} {} {}{:05d}.png'.format(files[i], files[i+1], files[i+2], output_path, i))

