import cv2
import numpy as np

# Read the image
image = cv2.imread('img2.webp')

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to read the image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Edge detection using Canny edge detector
    cv2.imshow('Original Image', image)

    edges = cv2.Canny(blurred_image, 50, 150)
    cv2.imshow('Edges', edges)

    # Texture analysis using Laplacian operator
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    cv2.imshow('Texture (Laplacian)', laplacian)

    # Wait for any key to be pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
