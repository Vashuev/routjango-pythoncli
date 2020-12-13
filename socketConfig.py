import asyncio
import socketio
import os

sio = socketio.AsyncClient(reconnection=False)


@sio.event
async def connect():
    try:
        print('connected to server')
        os.system(f"python init.py")
    except:
        print("  ERROR : Unable to call init.py file")


@sio.event
async def disconnect():
    # print('disconnected from server\nDo you want to reconnect?')
    print('disconnected from server\nPlease exit with CTRL+BREAK and restart the script')

@sio.event
async def error():
    print('error from server\nDisconnecting from server')
    sio.disconnect()


@sio.event
def message(msg):
    print(f'message from server{msg}')


async def start_server():
    await sio.connect('http://localhost:8080/?roomId=26821&clientType=cli')
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(start_server())
