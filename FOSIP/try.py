import cv2
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def preprocess_image(gray_image):
    # Convert the gray image to binary image
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Adjust brightness and contrast
    alpha = 1.2  # Contrast control (1.0 means no change)
    beta = 10    # Brightness control (0 means no change)
    adjusted_image = cv2.convertScaleAbs(gray_image, alpha=alpha, beta=beta)

    # Apply Otsu's binarization to represent dim characters
    _, otsu_binary_image = cv2.threshold(adjusted_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return binary_image, adjusted_image, otsu_binary_image

def character_segmentation_vpp(binary_image):
    vpp = np.sum(binary_image, axis=0)
    threshold_value = max(vpp) * 0.5
    character_boundaries = (vpp > threshold_value).astype(np.uint8)
    boundary_indices = np.where(np.diff(character_boundaries))[0]
    characters = []
    
    for i in range(0, len(boundary_indices), 2):
        start_index = boundary_indices[i]
        end_index = boundary_indices[i + 1] if i + 1 < len(boundary_indices) else len(vpp) - 1
        character = binary_image[:, start_index:end_index]
        height, width = character.shape
        width_to_height_ratio = width / height
        
        if width_to_height_ratio > 0.8:
            print(f'Touching character detected at index {i//2 + 1}')
        
        characters.append(character)

    return characters

def touching_character_segmentation(binary_image):
    vpp = np.sum(binary_image, axis=0)
    tdp = np.argmax(binary_image, axis=0)
    score_graph = np.zeros_like(vpp)

    for i in range(len(vpp)):
        if tdp[i] > 0 and tdp[i] < binary_image.shape[0] - 1:
            start_index = max(0, tdp[i] - 1)
            end_index = min(binary_image.shape[0], tdp[i] + 2)
            score_graph[start_index:end_index] += vpp[i]

    boundary_indices = np.where(score_graph > 0)[0]
    combined_boundary_points = []

    for i in range(0, len(boundary_indices), 2):
        start_index = boundary_indices[i]
        end_index = boundary_indices[i + 1] if i + 1 < len(boundary_indices) else len(score_graph) - 1
        combined_boundary_points.append((start_index, end_index))

    correct_boundary_points = []

    for start_index, end_index in combined_boundary_points:
        # Implement recognition-based method to select correct boundary points
        # (you may need to modify this part based on your specific recognition approach)
        # For now, we'll just choose the middle point as correct boundary
        middle_point = (start_index + end_index) // 2
        correct_boundary_points.append(middle_point)

    return correct_boundary_points

def recognize_characters(characters):
    # Placeholder for training data and labels
    data = []
    labels = []

    # Assuming you have a dataset of labeled characters
    # Each character should be a grayscale image of the same size

    # Example dataset (replace this with your actual dataset)
    dataset = {
        "0": cv2.imread('char_0.png', cv2.IMREAD_GRAYSCALE),
        "1": cv2.imread('char_1.png', cv2.IMREAD_GRAYSCALE),
        # Add more characters and corresponding images
    }

    for label, char_image in dataset.items():
        # Resize the character image to match the segmented characters' size
        char_image = cv2.resize(char_image, (characters[0].shape[1], characters[0].shape[0]))

        # Flatten the image into a 1D array for SVM
        flattened_char = char_image.flatten()

        data.append(flattened_char)
        labels.append(label)

    # Convert lists to NumPy arrays
    data = np.array(data)
    labels = np.array(labels)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train a multi-class SVM model
    model = svm.SVC(kernel='linear', C=1)
    model.fit(X_train_scaled, y_train)

    # Make predictions on the segmented characters
    flattened_characters = [character.flatten() for character in characters]
    flattened_characters = np.array(flattened_characters)
    segmented_characters_labels = model.predict(flattened_characters)

    return segmented_characters_labels

# Example usage:
# Assuming 'gray_image' is your input grayscale image
gray_image = cv2.imread('2.jpeg', cv2.IMREAD_GRAYSCALE)
binary_image, adjusted_image, otsu_binary_image = preprocess_image(gray_image)

# Call the function for character segmentation using VPP
segmented_characters = character_segmentation_vpp(binary_image)

# Call the function for touching character segmentation
correct_boundary_points = touching_character_segmentation(binary_image)

# Extract characters based on correct boundary points
characters = [binary_image[:, start:end] for start, end in correct_boundary_points]

# Call the function for character recognition
recognized_characters = recognize_characters(characters)

# Display the recognized characters (you may need to adjust window names based on your preferences)
for i, character in enumerate(segmented_characters):
    cv2.imshow(f'Segmented Character {i + 1}', character)

for i, character_label in enumerate(recognized_characters):
    cv2.imshow(f'Recognized Character {i + 1}: {character_label}', characters[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
