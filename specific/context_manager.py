import asyncio
import traceback
from contextlib import asynccontextmanager

"""
kalau async operation bisa pakai "asynccontextmanager"
kalau sync "contextmanager"
"""


# context class: bisa langsung bikin fungsi didalamnya
class ContextSession:
    def __init__(self, data) -> None:
        self.data = data

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        exc_type: menangkap error saat proses masuk
        exc_val: sama kaya ext_type tapi bisa nangkap pesan error nya
        exc_tb: ngasih tau error nya di baris / kode mana
        """

        if exc_type is not None:
            print(f"Ada error: {exc_type.__name__} = {exc_val}")
            print(f"trace: {traceback.extract_tb(exc_tb)}")  # munculkan lokasi error

    async def get_data(self) -> int:
        return self.data


class Database:
    def __init__(self, host: str) -> None:
        self.host = host

    async def get_host(self) -> str:
        return self.host


# context func: lebih simple
@asynccontextmanager
async def CallContext(host: str):
    db = Database(host)  # kalau mau pakai custom fungsi mirip kaya class based
    try:
        yield db
    finally:
        print("clean session")


async def main():
    async with ContextSession(1) as cs:
        ...

    async with CallContext("127.0.0.1") as cc:
        print(await cc.get_host())


asyncio.run(main())
