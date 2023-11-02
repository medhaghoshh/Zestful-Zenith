import cv2 as cv

# Specify the full path to the image file
image_path = "C:/Users/ayush/Desktop/ZZ/test/gray.jpg"

# Read the image
img = cv.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print("Error: Unable to load image")
else:
    # noise filteration
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

    # Specify the path for saving the grayscale image, including the file name and extension
    output_path = "C:/Users/ayush/Desktop/test/blur.jpg"

    # Save the grayscale image
    cv.imwrite(output_path, blur)