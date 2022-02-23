from PIL import Image
import sys
import os.path

target_dir = sys.argv[1]
save_dir = sys.argv[2]

isExist = os.path.exists('./new')
if isExist:
    print('This directory exists!')
else:
    os.makedirs('./new')
    print('The new directory has been created!')

for img in os.listdir(target_dir):
    clnm = os.path.splitext(img)[0]
    if img.endswith('.jpg'):
        im = Image.open(f'{target_dir}/{img}')
        im.save(f'{save_dir}/{clnm}.png', 'png')
    else:
        print('All images are in .png format!')
        break
