import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def split_image(image, block_size):
    height, width = image.shape
    blocks = []
    for i in range(0, height - block_size + 1, block_size):  # Adjusted the range to fit blocks properly
        for j in range(0, width - block_size + 1, block_size):
            block = image[i:i + block_size, j:j + block_size]
            blocks.append(block)
    return blocks


def find_best_match(block, blocks):
    min_diff = float('inf')
    best_match = None

    for candidate_block in blocks:
        diff = np.sum(np.abs(block - candidate_block))
        if diff < min_diff:
            min_diff = diff
            best_match = candidate_block

    return best_match

def compress_image(image, block_size):
    blocks = split_image(image, block_size)
    compressed_image = np.zeros_like(image)

    for i, block in enumerate(blocks):
        best_match = find_best_match(block, blocks)
        compressed_image[i // (image.shape[1] // block_size) * block_size: (i // (image.shape[1] // block_size) + 1) * block_size,
                         (i % (image.shape[1] // block_size)) * block_size: ((i % (image.shape[1] // block_size)) + 1) * block_size] = best_match

    return compressed_image

# Load an image
input_image = Image.open('image1.jpg')
input_image = input_image.convert('L')  # Convert to grayscale
input_array = np.array(input_image)

# Set block size for partitioning
block_size = 8

# Compress the image
compressed = compress_image(input_array, block_size)

# Save compressed image to calculate file size
compressed_image = Image.fromarray(compressed.astype(np.uint8))
compressed_image.save('compressed_image.jpg', 'JPEG')  # Save the compressed image

# Calculate file sizes
original_size = os.path.getsize('image1.jpg') / 1024  # in kilobytes
compressed_size = os.path.getsize('compressed_image.jpg') / 1024  # in kilobytes

# Display the original and compressed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(input_array, cmap='gray')
plt.axis('off')
print(f'Original Image Size: {original_size:.2f} KB')

plt.subplot(1, 2, 2)
plt.title(f'Compressed Image (Block Size: {block_size})')
plt.imshow(compressed, cmap='gray')
plt.axis('off')
print(f'Compressed Image Size: {compressed_size:.2f} KB')

compression_ratio = original_size / compressed_size
print(f'Compression Ratio: {compression_ratio:.2f}')

plt.tight_layout()
plt.show()