import asyncio
import socketio
import os
import requests
import webbrowser

sio = socketio.AsyncClient(reconnection=False)
server_url = 'https://codr-front-server.herokuapp.com/'
webpage_url = 'https://code-front.vercel.app/'


@sio.event
async def connect():
    try:
        print('connected to server')
        webbrowser.open_new_tab(f'{webpage_url}?roomId={roomid}')
        os.system(f"python routjango\main.py")
    except:
        print("  ERROR : Unable to call main.py file")


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


async def start_server(roomid):
    await sio.connect(f'{server_url}?roomId={roomid}&clientType=cli')
    await sio.wait()


if __name__ == '__main__':
    response = requests.post(f'{server_url}login')
    if response.status_code == 200:
        content = response.json()
        # print(content)
        roomid = content["roomId"]
        # print(roomid)
        asyncio.run(start_server(roomid))
    else:
        print("Failed to connect")
    
