from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def task(n):
    print(f"Mulai {n}")
    time.sleep(2)
    print(f"Selesai {n}")
    return n * 2

# block eksekusi & auto di tutup kalo udah selesai
with ThreadPoolExecutor(max_workers=3) as executor:
    # map akan membagi task sebanyak max_workers
    # dan mengumpulkan result sesuai urutan nya
    # results = list(executor.map(task, range(10)))

    # with submit
    # yg di return yg duluan selesai bukan yg sesuai urutan kerja
    results = [executor.submit(task, n) for n in range(10)]

    for result in as_completed(results):
        print(result.result())

# print("Hasil:", results)
