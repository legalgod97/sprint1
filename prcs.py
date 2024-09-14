import time
from multiprocessing import Process


def worker(task_id):
    print(f'start {task_id}')
    time.sleep(2)
    print(f'end {task_id}')

if __name__ == '__main__':
    for i in range(1, 5):
        p = Process(target=worker, args=(i,))
        p.start()
        p.join()