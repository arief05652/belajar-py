"""AnyIo tutorial use
- mudah dipakai
- lebih modern
"""

import asyncio

import sniffio
import uvloop
from anyio import (
    CancelScope,
    create_task_group,
    get_cancelled_exc_class,
    move_on_after,
    run,
    sleep,
    to_thread,
)
from anyio.abc import TaskStatus


async def no_wait(num: int) -> None:
    try:
        while True:
            print("run: ", num)
            await sleep(2)
    except get_cancelled_exc_class():
        print("cancel task")
        raise
    finally:
        with CancelScope(shield=True):
            print("ini akan aktif dulu walaupun tugas nya berhenti")


async def wait_task(num: int, task_status: TaskStatus) -> None:
    task_status.started()
    print("wait: ", num)


def heavy_sum():
    result = [i * 12931293 for i in range(1_000_000)]
    print(sum(result))


async def main():
    """Utility Tool"""
    loop = asyncio.get_running_loop()
    print(f"current async lib: {sniffio.current_async_library()}")
    print(f"event loop: {type(loop)}")

    print("WORKER THREAD")
    async with create_task_group() as tg:
        await to_thread.run_sync(heavy_sum)

    print("CREATE TASK")
    async with create_task_group() as tg:
        for num in range(2):
            """
            start: menunggu server siap dulu baru jalankan tugas nya
            start_soon: langsung menjalankan tugas bisa gagal kalau server belum siap
            """
            # tg.start_soon(no_wait, num)
            await tg.start(wait_task, num)
            # tg.cancel_scope.cancel() # cancel task manual

    print("TIMEOUT TASK")
    async with create_task_group() as tg:
        with move_on_after(2) as scope:
            print("cetak timeout")
            await sleep(2)
            print("ga akan di print")
            print("timeout", scope.cancelled_caught)


if __name__ == "__main__":
    run(
        main,
        backend="asyncio",
        backend_options={
            "loop_factory": uvloop.new_event_loop,  # pakai uvloop sebagai event utama
            "debug": True,
        },
    )
