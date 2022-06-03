import cv2 as cv
import pytesseract

img = cv.imread('handwritten.png')

data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
print(data)
to_find = "name"

for i in range(len(data['text'])):
    if to_find in data['text'][i].lower():
        x,y,w,h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        zoning_area = (x-10,y-20,x+w+100,h+y+10)
        break
        # cv.rectangle(img, (x-50,y-50), (x+w+100, y+h+50), (124,234,56), 2)

for i in range(len(data['text'])):
    x,y,w,h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
    if x>=zoning_area[0] and y >= zoning_area[1] and x+w<=zoning_area[2] and h+y<zoning_area[3]:
        print(data['text'][i])

# cv.imshow("IMAGE",img)
# cv.waitKey(0)