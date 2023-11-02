import cv2 as cv

# Specify the full path to the image file
image_path = "C:/Users/ayush/Desktop/ZZ/test/gray.jpg"
img = cv.imread(image_path)


flip = cv.flip( img, 1) 

output_path = "C:/Users/ayush/Desktop/ZZ/test/flip.jpg"
cv.imwrite(output_path, flip)