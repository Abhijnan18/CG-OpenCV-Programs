import cv2

# Read the image
image = cv2.imread('img.webp')

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to read the image.")
else:
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (11, 11), 0)

    # Apply bilateral filter for smoothing
    smoothed_image = cv2.bilateralFilter(image, 9, 75, 75)

    # Display the original and blurred images
    cv2.imshow('Original Image | 1JS21CS004', image)
    cv2.imshow('Blurred Image (Gaussian)', blurred_image)
    cv2.imshow('Smoothed Image (Bilateral)', smoothed_image)

    # Wait for any key to be pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
