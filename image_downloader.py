
import asyncio
import requests


async def func_1():
    url = "https://cdn.ebaumsworld.com/mediaFiles/picture/2452130/85386506.jpg"
    response = requests.get(url)
    open("inage1.jpg", "wb").write(response.content)
    print("Function 1 run successfully.")
    return 1


async def func_2():
    url = "http://www.pixelstalk.net/wp-content/uploads/2016/08/Free-Random-Wallpaper-Download.jpg"
    response = requests.get(url)
    open("inage2.jpg", "wb").write(response.content)
    print("Function 2 run successfully.")
    return 2


async def func_3():
    url = "http://images.unsplash.com/photo-1604409969824-6cdc3f32d682?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max"
    response = requests.get(url)
    open("inage3.jpg", "wb").write(response.content)
    print("Function 3 run successfully.")
    return 3


async def main():
    
    await asyncio.gather(
        func_1(),
        func_2(),
        func_3(),
    )
asyncio.run(main())
