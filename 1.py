import cv2

# Read the image
image = cv2.imread('img.webp')

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to read the image.")
else:
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Split the image into quadrants
    top_left = image[0:height//2, 0:width//2]
    top_right = image[0:height//2, width//2:width]
    bottom_left = image[height//2:height, 0:width//2]
    bottom_right = image[height//2:height, width//2:width]

    # Display each quadrant separately
    cv2.imshow('TLQ | 1JS21CS004', top_left)
    cv2.imshow('Top Right Quadrant', top_right)
    cv2.imshow('Bottom Left Quadrant', bottom_left)
    cv2.imshow('Bottom Right Quadrant', bottom_right)

    # Wait for any key to be pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
