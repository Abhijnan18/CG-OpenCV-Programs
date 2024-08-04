import cv2
import numpy as np

image = cv2.imread('img.webp')

if image is None:
    print("Error: Unable to read the image.")
else:
    height, width = image.shape[:2]

    angle = 90

    scale_x = 0.5
    scale_y = 0.5

    offset_x = 100
    offset_y = 50

    rotation_matrix = cv2.getRotationMatrix2D(
        (width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    scaled_image = cv2.resize(image, None, fx=scale_x,
                              fy=scale_y)

    translation_matrix = np.float32([[1, 0, offset_x], [0, 1, offset_y]])
    translated_image = cv2.warpAffine(
        image, translation_matrix, (width, height))

    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.imshow('Scaled Image', scaled_image)
    cv2.imshow('Translated Image', translated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read the image
image = cv2.imread('img1.webp')

if image is not None:
    h, w = image.shape[:2]

    # Rotation
    rot_matrix = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
    rotated_image = cv2.warpAffine(image, rot_matrix, (w, h))

    # Scaling
    scaled_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    # Translation
    trans_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    translated_image = cv2.warpAffine(image, trans_matrix, (w, h))

    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.imshow('Scaled Image', scaled_image)
    cv2.imshow('Translated Image', translated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to read the image.")
