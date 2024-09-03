import cv2
import numpy as np


def normalize_image(image):
    normalized_image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return normalized_image


def convert_to_lab(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return lab_image


def adaptive_kmeans_segmentation(image, k=2):
    Z = image.reshape((-1, 3))

    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)


    center = np.uint8(center)
    segmented_image = center[label.flatten()]
    segmented_image = segmented_image.reshape(image.shape)

    return segmented_image


input_image = cv2.imread('ant.jpeg')

normalized = normalize_image(input_image)

lab_image = convert_to_lab(normalized)

segmented_image = adaptive_kmeans_segmentation(lab_image)

cv2.imshow('Input Image', input_image)
cv2.imshow('Normalized Image', normalized)
cv2.imshow('L*a*b* Image', lab_image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
