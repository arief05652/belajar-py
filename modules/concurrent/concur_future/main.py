import os
from concurrent.futures import (
    ALL_COMPLETED,
    FIRST_COMPLETED,
    FIRST_EXCEPTION,
    BrokenExecutor,
    CancelledError,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    TimeoutError,
    as_completed,
    wait,
)
from random import randint
from time import sleep

"""
ThreadPoolExecutor: cocok digunakan untuk I/O dan membuat thread di pool
ProcessPoolExecutor: membuat proses python secara paralel dan membuat banyak cpu bekerja di pool
"""

# ThreadPoolExecutor - untuk I/O bound tasks
thread_executor = ThreadPoolExecutor(
    max_workers=5,  # Jumlah thread di pool
    thread_name_prefix="MyThread",  # Prefix nama thread
    initializer=None,  # Fungsi yang dijalankan sebelum worker mulai
    initargs=(),  # Argumen untuk initializer
)

# ProcessPoolExecutor - untuk CPU bound tasks
process_executor = ProcessPoolExecutor(
    max_workers=os.cpu_count(),  # Jumlah process
    mp_context=None,  # Multiprocessing context ('spawn', 'fork', 'forkserver')
    initializer=None,  # Fungsi initializer per process
    initargs=(),  # Argumen initializer
)

# ========= MANUAL POOLING ===========
manual_pooling = ThreadPoolExecutor(max_workers=3)  # bikin pool
manual_task = manual_pooling.submit(
    sum, [25, 12, 60]
)  # masukan tugas ke pool, dan mengembalikan "Future"
print(manual_task.result())  # ambil hasil dari task yang selesai
# matikan pool, ( wait: menunggu task selesai dulu, cancel_futures: cancel task untuk operasi selanjutnya)
manual_pooling.shutdown()

# ========= FUTURE ===========
manual_task.cancel()  # cancel task yang running
manual_task.cancelled()  # true jika task sudah cancel
manual_task.running()  # cek task yang sedang running
manual_task.done()  # cek task jika sudah done / cancel
manual_task.add_done_callback(
    lambda result: print(f"result task: {result.result()}")
)  # kirim hasil ke fungsi


# ========= AUTOMATIC POOLING ===========
def sum_list(a: list, time: float | None):
    if time:
        sleep(time)
    return sum(i * 1231 for i in a)


with ThreadPoolExecutor(10) as worker:
    future = worker.submit(sum_list, [i for i in range(7_000_000)], randint(1, 5))
    try:
        result = future.result(timeout=1)
        print("result: ", result)
    except TimeoutError:
        print("task timeout")


# ========= AS_COMPLETED ===========
# as_completed: yield future satu per satu sesuai urutan task yang selesai duluan
# berbeda dengan iterasi biasa yang menunggu semua selesai berurutan


def fetch_data(url: str, delay: float):
    sleep(delay)
    return f"data dari {url} (delay: {delay}s)"


urls = ["api/users", "api/orders", "api/products", "api/stats"]
delays = [3, 1, 2, 0.5]

with ThreadPoolExecutor(max_workers=4) as worker:
    futures_map = {
        worker.submit(fetch_data, url, delay): delay  # map future -> url untuk tracking
        for url, delay in zip(urls, delays)
    }

    for future in as_completed(futures_map):  # yield future yang selesai duluan
        url = futures_map[future]  # ambil url dari map
        try:
            result = future.result()
            print(f"[as_completed] selesai: {result}")
        except Exception as e:
            print(f"[as_completed] error di {url}: {e}")


# ========= EXECUTOR.MAP ===========
# map: seperti built-in map(), tapi dijalankan paralel di pool
# hasilnya berurutan sesuai input (bukan urutan selesai)
# jika salah satu task error, exception dilempar saat iterasi hasil


def kuadrat(n: int):
    sleep(n * 0.1)  # simulasi beban berbeda per input
    return n**2


inputs = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as worker:
    # hasil iterator, diambil saat di-loop (lazy evaluation)
    results = worker.map(kuadrat, inputs, timeout=5)  # timeout per item
    try:
        for angka, hasil in zip(inputs, results):
            print(f"[map] {angka}^2 = {hasil}")
    except TimeoutError:
        print("[map] ada task yang timeout")


# map dengan banyak argumen menggunakan zip + starmap-style lambda
args_list = [([i], i * 0.2) for i in range(1, 6)]

with ThreadPoolExecutor(max_workers=3) as worker:
    results = worker.map(lambda args: sum_list(*args), args_list)
    for hasil in results:
        print(f"[map multi-arg] hasil: {hasil}")


# ========= WAIT ===========
# wait: tunggu sekumpulan future berdasarkan kondisi tertentu
# return: (done: set, not_done: set)
# return_when options:
#   ALL_COMPLETED     -> tunggu semua task selesai (default)
#   FIRST_COMPLETED   -> return begitu ada 1 task selesai
#   FIRST_EXCEPTION   -> return begitu ada 1 task raise exception


def task_bisa_gagal(n: int):
    sleep(n)
    if n == 2:
        raise ValueError(f"task {n} sengaja gagal!")
    return f"task {n} selesai"


with ThreadPoolExecutor(max_workers=4) as worker:
    futures = [worker.submit(task_bisa_gagal, i) for i in range(5)]

    # -- ALL_COMPLETED: tunggu semua selesai
    done, not_done = wait(futures, return_when=ALL_COMPLETED)
    print(f"[ALL_COMPLETED] selesai: {len(done)}, belum: {len(not_done)}")

    # -- FIRST_COMPLETED: return begitu ada yang selesai pertama
    futures2 = [worker.submit(task_bisa_gagal, i) for i in [3, 1, 2]]
    done, not_done = wait(futures2, return_when=FIRST_COMPLETED)
    print(f"[FIRST_COMPLETED] selesai: {len(done)}, belum: {len(not_done)}")
    for f in done:
        print(f"  -> {f.result()}")

    # -- FIRST_EXCEPTION: return begitu ada task yang throw exception
    futures3 = [worker.submit(task_bisa_gagal, i) for i in [3, 2, 1]]
    done, not_done = wait(futures3, timeout=10, return_when=FIRST_EXCEPTION)
    print(f"[FIRST_EXCEPTION] selesai/gagal: {len(done)}, belum: {len(not_done)}")
    for f in done:
        try:
            print(f"  -> {f.result()}")
        except Exception as e:
            print(f"  -> exception tertangkap: {e}")


# ========= INITIALIZER ===========
# initializer: fungsi yang dijalankan SEKALI saat worker pertama kali dibuat
# cocok untuk setup resource per-worker: koneksi DB, load model ML, buka file, dll.
# initargs: tuple argumen untuk initializer

import threading

worker_local = threading.local()  # storage per-thread (thread-safe)


def setup_worker(db_url: str, debug: bool):
    """Dijalankan sekali saat thread/process worker dibuat"""
    worker_local.conn = f"koneksi ke {db_url}"  # simulasi koneksi DB
    worker_local.debug = debug
    name = threading.current_thread().name
    print(f"[init] worker '{name}' siap, koneksi: {worker_local.conn}")


def query_db(query: str):
    """Task yang berjalan di worker, bisa akses resource dari initializer"""
    conn = getattr(worker_local, "conn", "tidak ada koneksi")
    debug = getattr(worker_local, "debug", False)
    sleep(0.5)
    if debug:
        print(f"[query] menggunakan {conn} -> '{query}'")
    return f"hasil query: {query}"


with ThreadPoolExecutor(
    max_workers=2,
    thread_name_prefix="DBWorker",
    initializer=setup_worker,  # dijalankan saat worker dibuat
    initargs=("postgresql://localhost/app", True),  # argumen untuk initializer
) as worker:
    queries = [
        "SELECT * FROM users",
        "SELECT * FROM orders",
        "SELECT COUNT(*) FROM logs",
    ]
    futures = [worker.submit(query_db, q) for q in queries]
    for future in as_completed(futures):
        print(future.result())


# ========= PROCESS POOL EXECUTOR ===========
# ProcessPoolExecutor: untuk CPU-bound tasks
# setiap worker adalah proses Python terpisah (bukan thread)
# menghindari GIL -> bisa pakai semua core CPU
# PENTING: fungsi dan argumen harus bisa di-pickle
# PENTING: jika di Windows/macOS, kode harus di dalam if __name__ == "__main__"


def hitung_prima(n: int) -> int:
    """CPU-bound: hitung semua bilangan prima sampai n (Sieve of Eratosthenes)"""
    if n < 2:
        return 0
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return sum(sieve)


def faktorial_besar(n: int) -> int:
    """CPU-bound: hitung faktorial angka besar"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# -- MANUAL POOLING (ProcessPool) --
proc_pool = ProcessPoolExecutor(max_workers=2)
proc_task = proc_pool.submit(hitung_prima, 100_000)
print(f"[process manual] jumlah prima sampai 100.000: {proc_task.result()}")
proc_pool.shutdown(wait=True)


# -- AUTOMATIC POOLING dengan submit (ProcessPool) --
batas_list = [500_000, 1_000_000, 200_000, 750_000]

with ProcessPoolExecutor(max_workers=os.cpu_count()) as worker:
    futures_proc = {worker.submit(hitung_prima, n): n for n in batas_list}

    for future in as_completed(futures_proc):
        batas = futures_proc[future]
        try:
            jumlah = future.result()
            print(f"[process as_completed] prima sampai {batas:,}: {jumlah}")
        except Exception as e:
            print(f"[process as_completed] error: {e}")


# -- MAP dengan ProcessPool --
angka_besar = [500, 600, 700, 800, 900]

with ProcessPoolExecutor(max_workers=os.cpu_count()) as worker:
    results = worker.map(faktorial_besar, angka_besar)
    for n, hasil in zip(angka_besar, results):
        # faktorial angka besar -> tampilkan jumlah digit saja
        print(f"[process map] {n}! memiliki {len(str(hasil))} digit")


# -- WAIT dengan ProcessPool --
with ProcessPoolExecutor(max_workers=2) as worker:
    proc_futures = [worker.submit(hitung_prima, n) for n in [300_000, 100_000, 200_000]]
    done, not_done = wait(proc_futures, return_when=FIRST_COMPLETED)
    print(f"[process wait FIRST_COMPLETED] {len(done)} selesai duluan")
    for f in done:
        print(f"  -> {f.result()}")


# -- INITIALIZER dengan ProcessPool --
# initializer di ProcessPool berjalan di setiap PROSES (bukan thread)
# cocok untuk: load model ML yang berat, buka file besar, dll.


def init_proses(nama_model: str):
    """Setup sekali per proses worker"""
    import os

    pid = os.getpid()
    # simulasi load model ML yang berat
    print(f"[process init] PID {pid} load model '{nama_model}' selesai")


def inferensi(data: int) -> float:
    """Simulasi inferensi model per data"""
    sleep(0.1)
    return data * 3.14  # simulasi hasil prediksi


with ProcessPoolExecutor(
    max_workers=2,
    initializer=init_proses,  # dijalankan sekali per proses
    initargs=("model_regresi_v2",),  # argumen initializer (tuple, jangan lupa koma)
) as worker:
    dataset = list(range(1, 8))
    results = worker.map(inferensi, dataset)
    for data, pred in zip(dataset, results):
        print(f"[process init map] data={data} -> prediksi={pred:.2f}")


# ========= EXCEPTION HANDLING ===========
# exception tidak langsung muncul, baru muncul saat .result() dipanggil
# bisa juga terjadi BrokenExecutor jika worker crash total


def task_berbahaya(n: int):
    if n % 3 == 0:
        raise RuntimeError(f"input {n} adalah kelipatan 3, ditolak!")
    return n * 10


with ThreadPoolExecutor(max_workers=3) as worker:
    futures_exc = [worker.submit(task_berbahaya, i) for i in range(6)]

    for i, future in enumerate(as_completed(futures_exc)):
        try:
            print(f"[exception handling] hasil: {future.result()}")
        except RuntimeError as e:
            print(f"[exception handling] RuntimeError tertangkap: {e}")
        except CancelledError:
            print(f"[exception handling] task di-cancel")
        except Exception as e:
            print(f"[exception handling] error tak terduga: {e}")


# ========= SHUTDOWN ===========
# shutdown(wait=True)             -> tunggu semua task selesai, lalu shutdown
# shutdown(wait=False)            -> shutdown segera, task yang jalan tetap jalan
# shutdown(cancel_futures=True)   -> cancel semua task yang belum mulai
# context manager (with) otomatis panggil shutdown(wait=True)

late_pool = ThreadPoolExecutor(max_workers=2)
[late_pool.submit(sleep, i) for i in range(5)]
late_pool.shutdown(
    wait=False,  # jangan tunggu task selesai
    cancel_futures=True,  # cancel task yang belum mulai di queue
)
print("[shutdown] pool ditutup paksa, task yang antri di-cancel")
