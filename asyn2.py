import asyncio

async def f1():
    print("Hello, function 1!")
    await asyncio.sleep(1)
    print("Goodbye, function 1!")

async def f2():
    print("Hello, function 2!")
    await asyncio.sleep(2)
    print("Goodbye, function 2!")

async def f3():
    print("Hello, function 3!")
    await asyncio.sleep(3)
    print("Goodbye, function 3!")


async def main():
    await asyncio.gather(f1(), f2(), f3())

asyncio.run(main())

