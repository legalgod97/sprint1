import threading

counter = 0
mutex = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        mutex.acquire()
        counter += 1
        mutex.release()

t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)
t3 = threading.Thread(target=increment_counter)

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()

print(counter)

