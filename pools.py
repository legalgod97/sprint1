import time
from multiprocessing import Pool


def worker(task_id):
    print(f'start {task_id}')
    time.sleep(2)
    print(f'end {task_id}')

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        values = [1, 2, 3, 4]
        pool.map(worker, values)
