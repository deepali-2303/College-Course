import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings

# Suppressing warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('data.csv')

label_encoder = LabelEncoder()
data['color'] = label_encoder.fit_transform(data['color'])
data['height'] = label_encoder.fit_transform(data['height'])
data['smelly'] = label_encoder.fit_transform(data['smelly'])
data['species'] = label_encoder.fit_transform(data['species'])

X = data[['color', 'legs', 'height', 'smelly']]
y = data['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_classifier = GaussianNB()

nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')

def calculate_conditional_probability(feature, value, species):
    count = sum(1 for i in range(len(X_train)) if X_train.iloc[i][feature] == value and y_train.iloc[i] == species)
    total_species_count = sum(1 for i in range(len(y_train)) if y_train.iloc[i] == species)
    
    smoothing_factor = 0.01
    constant = 1
    
    return (count + smoothing_factor) / (total_species_count + constant)

print("\nConditional Probability Table for Color:")
for value in [0, 1]:
    for species in [0, 1]:
        prob = calculate_conditional_probability(0, value, species)
        print(f"P(color={value} | species={species}) = {prob}")

print("\nConditional Probability Table for Legs:")
for value in [0, 1]:
    for species in [0, 1]:
        prob = calculate_conditional_probability(1, value, species)
        print(f"P(legs={value} | species={species}) = {prob}")

print("\nConditional Probability Table for Height:")
for value in [0, 1]:
    for species in [0, 1]:
        prob = calculate_conditional_probability(2, value, species)
        print(f"P(height={value} | species={species}) = {prob}")

print("\nConditional Probability Table for Smelly:")
for value in [0, 1]:
    for species in [0, 1]:
        prob = calculate_conditional_probability(3, value, species)
        print(f"P(smelly={value} | species={species}) = {prob}")

test_entry = [[0, 1, 1, 0]]
predicted_species = nb_classifier.predict(test_entry)

predicted_species = label_encoder.inverse_transform(predicted_species)

print(f"\nThe predicted species is: {predicted_species[0]}")
