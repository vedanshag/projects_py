import os
import cv2

path = input('Enter the address of the directory\n')
#os.chdir('D:\Vedansh\EBooks\Manga\Shiver-II')
os.chdir(path)
list = sorted(os.listdir(), key=lambda x: int("".join([i for i in x if i.isdigit()])))

os.makedirs('Cropped')
for index, title in enumerate(list):
    if(title != str(index) + '.png'):
        os.rename(title, str(index) + '.png')

    img = cv2.imread(str(index) + '.png')   #reading the image
    rows = 0
    cols = 0
    if(index == 0):
        rows, cols, _ = img.shape;
        print(f'Rows - {rows}pixels, Columns - {cols}pixels')
    cut_image = img[100:1500, 75:1050]      #set the value of cropping here
    os.chdir(path+'\Cropped')
    status = cv2.imwrite(str(index) + '.png', cut_image)
    os.chdir(path)


