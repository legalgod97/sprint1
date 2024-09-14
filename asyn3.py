import asyncio
import aioping

async def do_ping1():
    url = "google.com"
    try:
        delay = await aioping.ping(url) * 1000
        print(f"Пинг сайта {url} - %s ms" % delay)

    except:
        print("URL сайта некорректен")

async def do_ping2():
    url = "vk.com"
    try:
        delay = await aioping.ping(url) * 1000
        print(f"Пинг сайта {url} - %s ms" % delay)

    except:
        print("URL сайта некорректен")

async def do_ping3():
    url = "3333"
    try:
        delay = await aioping.ping(url) * 1000
        print(f"Пинг сайта {url} - %s ms" % delay)

    except:
        print("URL сайта некорректен")

async def do_ping4():
    url = "yandex.ru"
    try:
        delay = await aioping.ping(url) * 1000
        print(f"Пинг сайта {url} - %s ms" % delay)

    except:
        print("URL сайта некорректен")

async def do_ping5():
    url = "yahoo.com"
    try:
        delay = await aioping.ping(url) * 1000
        print(f"Пинг сайта {url} - %s ms" % delay)

    except:
        print("URL сайта некорректен")

async def main():
    await asyncio.gather(do_ping1(), do_ping2(), do_ping3(), do_ping4(), do_ping5())

asyncio.run(main())





