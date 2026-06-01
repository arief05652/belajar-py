"""
ANYIO SYNCHRONIZATION PRIMITIVES DEMO
=====================================

Ini contoh 1 file untuk memahami:

1. Lock              → mencegah race condition
2. Semaphore         → membatasi jumlah task
3. Event             → signaling (ON/OFF)
4. CapacityLimiter   → limit concurrency (I/O control)

Konsep utama:
- Semua task berjalan di event loop yang sama
- Sync primitive = aturan siapa boleh jalan kapan
"""

import anyio

# =========================================================
# 1. LOCK DEMO (Race condition protection)
# =========================================================

counter = 0
lock = anyio.Lock()


async def lock_worker(name: str):
    """
    Tanpa lock → counter bisa rusak (race condition)
    Dengan lock → aman
    """
    global counter

    async with lock:
        temp = counter
        await anyio.sleep(0.1)  # simulasi delay (biar tabrakan kelihatan)
        counter = temp + 1
        print(f"[LOCK] {name} increment -> {counter}")


# =========================================================
# 2. SEMAPHORE DEMO (limit concurrency)
# =========================================================

sem = anyio.Semaphore(2)


async def semaphore_worker(i: int):
    """
    Hanya 2 task boleh jalan bersamaan
    """
    async with sem:
        print(f"[SEMAPHORE] start {i}")
        await anyio.sleep(1)
        print(f"[SEMAPHORE] done {i}")


# =========================================================
# 3. EVENT DEMO (signal / trigger)
# =========================================================

event = anyio.Event()


async def event_worker():
    """
    Menunggu signal sebelum jalan
    """
    print("[EVENT] waiting signal...")
    await event.wait()
    print("[EVENT] got signal -> run!")


# =========================================================
# 4. CAPACITY LIMITER DEMO (I/O throttling)
# =========================================================

limiter = anyio.CapacityLimiter(2)


async def limited_task(i: int):
    async with limiter:
        print(f"[LIMITER] start {i}")
        await anyio.sleep(1)
        print(f"[LIMITER] end {i}")


async def main():
    """
    Semua demo dijalankan dalam TaskGroup
    (structured concurrency - aman & clean shutdown)
    """

    async with anyio.create_task_group() as tg:
        # -------------------------
        # LOCK DEMO
        # -------------------------
        for i in range(2):
            tg.start_soon(lock_worker, f"worker-{i}")

        # -------------------------
        # SEMAPHORE DEMO
        # -------------------------
        for i in range(2):
            tg.start_soon(semaphore_worker, i)

        # -------------------------
        # EVENT DEMO
        # -------------------------
        tg.start_soon(event_worker)

        # trigger event setelah 2 detik
        async def trigger():
            await anyio.sleep(2)
            print("[EVENT] setting signal")
            event.set()

        tg.start_soon(trigger)

        # -------------------------
        # LIMITER DEMO
        # -------------------------
        for i in range(4):
            tg.start_soon(limited_task, i)


if __name__ == "__main__":
    anyio.run(main)


""" OUTPUT
[EVENT] waiting signal...
[SEMAPHORE] start 0
[SEMAPHORE] start 1
[LIMITER] start 0
[LIMITER] start 1
[LOCK] worker-0 increment -> 1
[LOCK] worker-1 increment -> 2
[SEMAPHORE] done 0
[SEMAPHORE] done 1
[LIMITER] end 0
[LIMITER] end 1
[LIMITER] start 2
[LIMITER] start 3
[EVENT] setting signal
[EVENT] got signal -> run!
[LIMITER] end 2
[LIMITER] end 3
"""
