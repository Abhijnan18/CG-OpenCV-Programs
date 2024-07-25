import cv2
import numpy as np

# Read the image
image = cv2.imread('img.webp')

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to read the image.")
else:
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Define rotation angle (in degrees)
    angle = 90

    # Define scaling factors (in percentage)
    scale_x = 0.5  # Scaling factor for width
    scale_y = 0.5  # Scaling factor for height

    # Define translation offsets (in pixels)
    offset_x = 100
    offset_y = 50

    # Perform rotation
    rotation_matrix = cv2.getRotationMatrix2D(
        (width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    # Perform scaling
    scaled_image = cv2.resize(image, None, fx=scale_x,
                              fy=scale_y, interpolation=cv2.INTER_LINEAR)

    # Perform translation
    translation_matrix = np.float32([[1, 0, offset_x], [0, 1, offset_y]])
    translated_image = cv2.warpAffine(
        image, translation_matrix, (width, height))

    # Display original, rotated, scaled, and translated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.imshow('Scaled Image', scaled_image)
    cv2.imshow('Translated Image', translated_image)

    # Wait for any key to be pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
