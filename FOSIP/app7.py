import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the kernel for spatial filtering
kernel = np.ones((3, 3), np.float32) / 9.0  # Adjust coefficients as needed

def spatial_filtering_refresher(original_image):
    smoothed_image = cv2.filter2D(original_image, -1, kernel)
    return smoothed_image

def sharpening_spatial_filters(image):
    derivative1 = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    enhanced_image = laplacian + derivative1
    return enhanced_image

def sobel_filters(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_result = np.sqrt(sobel_x**2 + sobel_y**2)
    return sobel_result

def combine_spatial_enhancement_methods(laplacian_result, sobel_result):
    combined_result = laplacian_result - sobel_result
    return combined_result

# Load the original image
original_image = cv2.imread("me1.jpg", cv2.IMREAD_GRAYSCALE)

# Apply the spatial filtering refresher
smoothed_image = spatial_filtering_refresher(original_image)

# Apply sharpening spatial filters
enhanced_image = sharpening_spatial_filters(smoothed_image)

# Apply Sobel filters
sobel_result = sobel_filters(smoothed_image)

# Combine spatial enhancement methods
final_result = combine_spatial_enhancement_methods(enhanced_image, sobel_result)

# Display all images
plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(original_image, cmap="gray")

plt.subplot(2, 3, 2)
plt.title("Smoothed Image")
plt.imshow(smoothed_image, cmap="gray")

plt.subplot(2, 3, 3)
plt.title("Enhanced Image")
plt.imshow(enhanced_image, cmap="gray")

plt.subplot(2, 3, 4)
plt.title("Sobel Result")
plt.imshow(sobel_result, cmap="gray")

plt.subplot(2, 3, 5)
plt.title("Combined Result")
plt.imshow(final_result, cmap="gray")

plt.show()
