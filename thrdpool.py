from concurrent.futures import ThreadPoolExecutor

def task_function(task_id):
    result = f"task with id {task_id} done"
    print(result)
    return result

with ThreadPoolExecutor(max_workers=4) as executor:

    future1 = executor.submit(task_function, 1)
    future2 = executor.submit(task_function, 2)
    future3 = executor.submit(task_function, 3)
    future4 = executor.submit(task_function, 4)

    result1 = future1.result()
    result2 = future2.result()
    result3 = future3.result()
    result4 = future4.result()