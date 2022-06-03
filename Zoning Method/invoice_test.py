import cv2 as cv
import pytesseract
from typing import OrderedDict

img = cv.imread('invoice.jpg')

image_data = pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)
print(image_data['text'])

key_vals = ['Bill', "#", "Due", "Grand"]


# to_find = key_vals[0].lower()


for key in key_vals:
    to_find = key.lower()
    found_val = ""
    for i in range(len(image_data['text'])):
        if to_find in image_data['text'][i].lower():
            x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
            if to_find == "bill":
                zoning_area = (x-10,y-20,x+w+170,h+y+90)
            else:
                zoning_area = (x-10,y-10,x+w+500,h+y+10)
            # cv.rectangle(img, (zoning_area[0], zoning_area[1]), (zoning_area[2],zoning_area[3]), (0,255,0), 2)
            break


    for i in range(len(image_data['text'])):
        x,y,w,h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
        if x>=zoning_area[0] and y >= zoning_area[1] and x+w<=zoning_area[2] and h+y<zoning_area[3]:
            found_val += image_data['text'][i]+" "

    print(f"{to_find} = {found_val}")
# cv.imshow("ABC", img)
# cv.waitKey(0)