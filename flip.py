#rotation
import cv2 as cv
img=cv.imread("C:/Users/ayush/Desktop/ZZ/test/gray.jpg")
height,width=img.shape[:2]
#rotation matrix
matrix=cv.getRotationMatrix2D((width/2,height/2),30,1)
#applying matrix to the image
rotated=cv.warpAffine(img,matrix,(width,height))
matrix=cv.getRotationMatrix2D((width/2,height/2),45,1)
#applying matrix to the image
rotated1=cv.warpAffine(img,matrix,(width,height))
matrix=cv.getRotationMatrix2D((width/2,height/2),60,1)
#applying matrix to the image
rotated2=cv.warpAffine(img,matrix,(width,height))

output_path = "C:/Users/ayush/Desktop/ZZ/test/rotated.jpg"
cv.imwrite(output_path, rotated)
output_path = "C:/Users/ayush/Desktop/ZZ/test/rotated1.jpg"
cv.imwrite(output_path, rotated1)
output_path = "C:/Users/ayush/Desktop/ZZ/test/rotated3.jpg"
cv.imwrite(output_path, rotated2)