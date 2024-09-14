import asyncio

async def main():
    print("Hello, asyncio!")
    await asyncio.sleep(2)
    print("Goodbye, asyncio!")

asyncio.run(main())