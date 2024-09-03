import csv
import random


features = ['fever', 'headache', 'jaundice']
labels = ['malaria', 'dengue']


data = []
for _ in range(50):
    fever = random.uniform(0.5, 1)
    headache = random.uniform(0.5, 1)
    jaundice = random.uniform(0, 1)
    
    if jaundice > 0.5:
        label = 1
    else:
        label = -1
    
    data.append([fever, headache, jaundice, label])


with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['fever', 'headache', 'jaundice', 'label'])
    writer.writerows(data)
