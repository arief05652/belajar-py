import os

from anyio import (
    NamedTemporaryFile,
    Path,
    SpooledTemporaryFile,
    TemporaryDirectory,
    TemporaryFile,
    gettempdir,
    mkdtemp,
    mkstemp,
    open_file,
    run,
)


async def main():
    """FILE DISK"""
    # write
    async with await open_file("modules/concurrent/anyio/test.txt", "w") as f:
        await f.write("askd")

    # read
    async with await open_file("modules/concurrent/anyio/test.txt", "r") as f:
        print(await f.read())

    path = Path("modules/concurrent/anyio/test.txt")
    print(await path.read_text())

    """TEMPORARY FILE"""
    async with TemporaryFile("w+t") as f:
        # write
        await f.write("temp file")

        # read
        await f.seek(0)
        print(await f.read())

    # temp file tapi keliatan di filesystem
    async with NamedTemporaryFile("r+") as f:
        print("path: ", f.name)

    """SPOOLED TEMP FILE"""
    # di simpan di memori dan bisa diatur sizenya jadi super cepat
    async with SpooledTemporaryFile(max_size=1024, mode="w+") as f:
        await f.write("memory data")  # write

        await f.seek(0)
        print(await f.read())  # read

    """TEMPORARY DIRECTORY"""
    async with TemporaryDirectory() as temp_dir:
        print("temp dir:", temp_dir)

        # buat file di dalam temp directory
        file_path = Path(temp_dir) / "hello.txt"
        await file_path.write_text("hello temporary directory")

        print(await file_path.read_text())

    # setelah keluar dari context manager
    # directory dan seluruh isinya otomatis dihapus

    """LOW LEVEL TEMP FUNCTIONS"""
    # membuat file temporary dan mengembalikan:
    # (file descriptor, path)
    fd, path = await mkstemp(
        suffix=".txt",
        prefix="example_",
        text=True,
    )

    print("mkstemp fd:", fd)
    print("mkstemp path:", path)

    os.close(fd)
    os.remove(path)

    # membuat temporary directory
    temp_dir = await mkdtemp(prefix="project_")

    print("mkdtemp path:", temp_dir)

    os.rmdir(temp_dir)

    # lokasi default temp directory
    print("temp dir:", await gettempdir())


run(main)
