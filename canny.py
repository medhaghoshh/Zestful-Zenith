import cv2 as cv

# Specify the full path to the image file

image_path = "C:/Users/ayush/Desktop/ZZ/test/IMG-20231031-WA0035.jpg"
img = cv.imread(image_path)

#canny
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
 
canny = cv.Canny(blur , 10, 230, cv.BORDER_DEFAULT)

output_path = "C:/Users/ayush/Desktop/ZZ/test/canny.jpg"
cv.imwrite(output_path, canny)