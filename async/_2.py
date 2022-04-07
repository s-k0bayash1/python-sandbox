import asyncio
import time


async def run():
    start = time.perf_counter()
    semaphore = asyncio.Semaphore(1)
    gather = asyncio.gather(hoge(1, semaphore), hoge(3, semaphore))
    print("start tasks")
    a = await gather
    print(a)
    print(time.perf_counter() - start)


async def hoge(n: int, s: asyncio.Semaphore) -> str:
    async with s:
        await asyncio.sleep(n)
        return f"sleep {n}ms"


if __name__ == "__main__":
    asyncio.run(run())
