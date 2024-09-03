import csv
import random
import time
import threading
import multiprocessing


# Function to generate CSV files
def generate_csv(file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(10000):
            row = [random.randint(1, 100) for _ in range(10)]
            writer.writerow(row)


# Function to read CSV files using multithreading
def read_csv_multithread(file_names):
    start_time = time.time()
   
    threads = []
    for file_name in file_names:
        thread = threading.Thread(target=generate_csv, args=(file_name,))
        thread.start()
        threads.append(thread)
   
    for thread in threads:
        thread.join()
   
    end_time = time.time()
    return end_time - start_time


# Function to read CSV files using multiprocessing
def read_csv_multiprocess(file_names):
    start_time = time.time()
   
    processes = []
    for file_name in file_names:
        process = multiprocessing.Process(target=generate_csv, args=(file_name,))
        process.start()
        processes.append(process)
   
    for process in processes:
        process.join()
   
    end_time = time.time()
    return end_time - start_time


# Generate 5 CSV files
file_names = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv']
for file_name in file_names:
    generate_csv(file_name)


if __name__ == '__main__':
    print("Time taken by multiprocessing:", read_csv_multithread(file_names), "seconds")


    print("Time taken by multithreading:", read_csv_multiprocess(file_names), "seconds")



