from imutils import paths
import cv2 as cv

# Specify the directory containing the images
image_directory1 = "C:/Users/ayush/Desktop/ZZ/original/neem/"
image_directory2 = "C:/Users/ayush/Desktop/ZZ/original/tulsi/"


# List all the image paths in the directory
image_paths1 = list(paths.list_images(image_directory1))
image_paths2 = list(paths.list_images(image_directory2))


for image_path1 in image_paths1:
    img = cv.imread(image_path1) #read the image
    
     # Check if the image was successfully loaded
    if img is None:
        print("Error: Unable to load image:", image_path1)
    else:
        
    # Convert the image to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    #For blurring the image
        blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
    
    #For rotating the image to specific angle
        def rotate(image, angle, rotPoint=None):
            (height,width)= img.shape[:2]
    
            if rotPoint is None:
                rotPoint= (height//2, width//2)
                rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
                dimensions = (width,height)
                return cv.warpAffine(gray,rotMat, dimensions, )


    #Flipping
        flip1 = cv.flip(gray , 0)#vertically
        flip2 = cv.flip(gray , 1)#horizontally
    
    #canny    
        canny = cv.Canny(blur , 10, 230, cv.BORDER_DEFAULT)
    
    #rotate
        rotated = rotate(gray, 45)
        rotated1 = rotate(gray, 30)
        rotated2 = rotate(gray, 60)

    # Specify the path for saving the grayscale image with "gray" prefix
    output_path1 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/gray/gray" +  image_path1.split("/")[-1] + ".jpg"
    output_path2 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/blur/blur_" + image_path1.split("/")[-1] + ".jpg"
    output_path3 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/flip/flip1_" + image_path1.split("/")[-1] + ".jpg"
    output_path4 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/flip/flip2_" + image_path1.split("/")[-1] + ".jpg"
    output_path5 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/rotated/rotated_" + image_path1.split("/")[-1] + ".jpg"
    output_path6 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/rotated/rotated1_" + image_path1.split("/")[-1] + ".jpg"
    output_path7 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/rotated/rotated2_" + image_path1.split("/")[-1] + ".jpg"
    output_path8 = "C:/Users/ayush/Desktop/ZZ/dataset/neemD/canny/canny_" + image_path1.split("/")[-1] + ".jpg"
    cv.imwrite(output_path1, gray)
    cv.imwrite(output_path2, blur)
    cv.imwrite(output_path3, flip1)
    cv.imwrite(output_path4, flip2)
    cv.imwrite(output_path5, rotated)
    cv.imwrite(output_path6, rotated1)
    cv.imwrite(output_path7, rotated2)
    cv.imwrite(output_path8, canny)

    
for image_path2 in image_paths2:
    img = cv.imread(image_path2) #read the image
    
     # Check if the image was successfully loaded
    if img is None:
        print("Error: Unable to load image:", image_path2)
    else:
        
    # Convert the image to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    #For blurring the image
        blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
    
    #For rotating the image to specific angle
        def rotate(image, angle, rotPoint=None):
            (height,width)= img.shape[:2]
    
            if rotPoint is None:
                rotPoint= (height//2, width//2)
                rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
                dimensions = (width,height)
                return cv.warpAffine(gray,rotMat, dimensions, )


    #Flipping
        flip1 = cv.flip(gray , 0)#vertically
        flip2 = cv.flip(gray , 1)#horizontally
    
    #canny
        bi = cv.bilateralFilter(blur , 5 , 6 , 6 )
        canny = cv.Canny(bi , 30, 35, cv.BORDER_DEFAULT)
    
    #rotate
        rotated = rotate(gray, 45)
        rotated1 = rotate(gray, 30)
        rotated2 = rotate(gray, 60)

    # Specify the path for saving the grayscale image with "gray" prefix
    output_path1 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/gray/gray" +  image_path2.split("/")[-1] + ".jpg"
    output_path2 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/blur/blur_" + image_path2.split("/")[-1] + ".jpg"
    output_path3 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/flip/flip1_" + image_path2.split("/")[-1] + ".jpg"
    output_path4 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/flip/flip2_" + image_path2.split("/")[-1] + ".jpg"
    output_path5 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/rotated/rotated_" + image_path2.split("/")[-1] + ".jpg"
    output_path6 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/rotated/rotated1_" + image_path2.split("/")[-1] + ".jpg"
    output_path7 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/rotated/rotated2_" + image_path2.split("/")[-1] + ".jpg"
    output_path8 = "C:/Users/ayush/Desktop/ZZ/dataset/tulsiD/canny/canny_" + image_path2.split("/")[-1] + ".jpg"
    cv.imwrite(output_path1, gray)
    cv.imwrite(output_path2, blur)
    cv.imwrite(output_path3, flip1)
    cv.imwrite(output_path4, flip2)
    cv.imwrite(output_path5, rotated)
    cv.imwrite(output_path6, rotated1)
    cv.imwrite(output_path7, rotated2)
    cv.imwrite(output_path8, canny)