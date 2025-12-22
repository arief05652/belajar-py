import asyncio
import time
from typing import Optional, Union

type time_delay = Optional[Union[int, float]]


async def delay_sleep(time: time_delay = None, msg: str = "") -> None:
    # ini untuk delay eksekusi, jangan pakai time.sleep karna itu blocking
    print(f"Task | {time} | {msg} | Start")
    await asyncio.sleep(time)
    print(f"Task | {time} | {msg} | Done")


async def fail_task(time: time_delay = None):
    await asyncio.sleep(time)
    # error tasks simulation
    raise ValueError("Task Error")


def sync_code():
    return "Sync Code"


async def main():
    print("======================")

    # sleep
    # memberi jeda waktu untuk eksekusi
    start = time.perf_counter()
    await delay_sleep(0.5, "ini sleep")
    print(f"finished in {time.perf_counter() - start:.4f}")

    print("======================")

    # create task
    # menaruh coroutine ke event loop untuk di eksekusi
    start = time.perf_counter()
    task1 = asyncio.create_task(delay_sleep(0.7, "Create Task"))
    await task1
    print(f"finished in {time.perf_counter() - start:.4f}")

    print("======================")

    # task group
    # menunggu semua task selesai tapi ketika ada yg fail maka semua nya dibatalkan
    start = time.perf_counter()

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(delay_sleep(0.3, "Task Group A"))
            tg.create_task(delay_sleep(0.6, "Task Group B"))
            tg.create_task(delay_sleep(1, "Task Group C"))
            tg.create_task(fail_task(0.5))
            tg.create_task(fail_task(0.5))

    # * di except fungsi nya untuk mengambil semua error disatu waktu
    except* Exception as e:
        print("Error TaskGroup: ")
        for e in e.exceptions:
            print("  =>", e)

    print(f"finished in {time.perf_counter() - start:.4f}")
    print("task group selesai")

    print("======================")

    # gather task
    # ketika ada error di satu task, bisa tetep lanjut.
    # default nya "return_exceptions=False"
    start = time.perf_counter()

    try:
        await asyncio.gather(
            delay_sleep(1, "Concurrent A"),
            delay_sleep(0.8, "Concurrent B"),
            delay_sleep(0.5, "Concurrent C"),
            fail_task(0.1),
            return_exceptions=True,  # untuk melanjutkan walau ada error
        )

    except Exception as e:
        print("Error TaskGather: ", e)

    print(f"finished in {time.perf_counter() - start:.4f}")

    print("======================")

    # wait task for
    # untuk membatasi task yang lama di eksekusi
    try:
        await asyncio.wait_for(delay_sleep(1, "Wait For"), timeout=0.5)
    except asyncio.TimeoutError:
        print("Timeout Error")

    print("======================")

    # to thread
    # untuk menjalankan sync code di thread seolah menjadi async
    sync = await asyncio.to_thread(sync_code)
    print(sync)

    print("======================")

    # timeout with
    try:
        async with asyncio.timeout(1):
            await asyncio.create_task(delay_sleep(2, "Timeout with"))
    except asyncio.TimeoutError:
        print("Timeout Error")

    print("======================")


asyncio.run(main())
