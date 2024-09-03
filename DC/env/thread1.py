import urllib.request
import time
import concurrent.futures
import multiprocessing
from functools import partial

URLS = ['https://en.wikipedia.org/wiki/Concurrent_computing#:~:text=A%20concurrent%20system%20is%20one,that%20may%20be%20executed%20concurrently',
        'https://en.wikipedia.org/wiki/World_War_II',
        'https://en.wikipedia.org/wiki/Fashion',
        'https://en.wikipedia.org/wiki/Apple_Inc.',
        'https://en.wikipedia.org/wiki/Samsung']


def load_url(url, timeout):
    start_time = time.time()
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        conn.read()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'{url} executed in {execution_time:.2f} seconds')
    return execution_time

if __name__ == '__main__':
    # Using multiprocessing
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results_multiprocess = pool.map(partial(load_url, timeout=60), URLS)
    end_time = time.time()
    multiprocessing_time = end_time - start_time
    print('Multiprocessing execution time:', multiprocessing_time, 'seconds')

    # Using multithreading
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results_multithread = list(executor.map(partial(load_url, timeout=60), URLS))
    end_time = time.time()
    multithreading_time = end_time - start_time
    print('Multithreading execution time:', multithreading_time, 'seconds')
