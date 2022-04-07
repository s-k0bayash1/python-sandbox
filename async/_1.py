import asyncio
import time


async def run():
    start = time.perf_counter()
    gather = asyncio.gather(hoge(1), hoge(3))
    print("start tasks")
    a = await gather
    print(a)
    print(time.perf_counter() - start)


async def hoge(n: int) -> str:
    await asyncio.sleep(n)
    return f"sleep {n}ms"


if __name__ == "__main__":
    asyncio.run(run())
