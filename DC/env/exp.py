import concurrent.futures
import time


def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def execute_with_threading():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(calculate_factorial, 100000) for _ in range(5)]
        for future in concurrent.futures.as_completed(results):
            result = future.result()
            # print(f"Thread Result: {result}")
    end_time = time.time()
    print(f"Time taken with threading: {end_time - start_time} seconds")


def execute_with_multiprocessing():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(calculate_factorial, 100000) for _ in range(5)]
        for future in concurrent.futures.as_completed(results):
            result = future.result()
            # print(f"Process Result: {result}")
    end_time = time.time()
    print(f"Time taken with multiprocessing: {end_time - start_time} seconds")


if __name__ == '__main__':
    execute_with_threading()
    execute_with_multiprocessing()
