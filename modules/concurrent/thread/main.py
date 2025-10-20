import threading
import time


def thread_function_biasa():
    print("Thread started | Biasa")
    time.sleep(2)
    print("Thread started | Biasa")

def thread_function_args(delay: int | float):
    print("Thread started | Args")
    time.sleep(delay)
    print("Thread started | Args")

def daemon_background():
    i = 1
    
    while i < 5:
        print("Daemon running in background")
        time.sleep(1)
        i += 1


# untuk mencegah thread mengubah data yg sama
lock = threading.Lock()

n = 0

def increment():
    global n
    for _ in range(10000):
        with lock:
            n += 1
            
# jalanin 10 thread
lock_thread = [threading.Thread(target=increment) for _ in range(10)]

for thread in lock_thread:
    thread.start()

for thread in lock_thread:
    thread.join()

print("Hasil Akhir: ", n)

# ini jalanin fungsi biasa
t = threading.Thread(target=thread_function_biasa)

# ini kalo jalanin fungsi yg ada parameternya
t1 = threading.Thread(target=thread_function_args, args=(1,))

# menjalankan thread
t.start()
t1.start()

# menunggu thread selesai
t.join()
t1.join()


# menjalankan daemon
d = threading.Thread(target=daemon_background, daemon=True)
d.start()
d.join()

print("Thread selesai")