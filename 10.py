import cv2

image = cv2.imread('img.webp')

if image is None:
    print("Error: Unable to read the image.")
else:
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    smoothed_image = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image (Gaussian)', blurred_image)
    cv2.imshow('Smoothed Image (Bilateral)', smoothed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
