import cv2 as cv

# Specify the full path to the image file
image_path = "C:/Users/ayush/Desktop/ZZ/test/IMG-20231031-WA0034.jpg"

# Read the image
img = cv.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print("Error: Unable to load image")
else:
    # Convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Specify the path for saving the grayscale image, including the file name and extension
    output_path = "C:/Users/ayush/Desktop/test/gray.jpg"

    # Save the grayscale image
    cv.imwrite(output_path, gray)