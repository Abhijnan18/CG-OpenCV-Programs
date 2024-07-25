import cv2

# Read the image
image = cv2.imread('img.webp')

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to read the image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on a copy of the original image
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

    # Display the original image with contours
    cv2.imshow('Original Image | 1JS21CS004', image)

    cv2.imshow('Contours', contour_image)

    # Wait for any key to be pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
