import time
from bs4 import BeautifulSoup
import requests

from telethon import functions
from telethon.sync import TelegramClient

import bd

api_id = bd.api_id
api_hash = bd.api_hash
default_status = bd.status
current_playing = ''


def shorten_track_name():
    tools = [
        lambda a: (a.split('—')[0] + '—' + a.split('—')[1].split('(')[0]).strip(),
        lambda a: (', '.join(a.split('—')[0].split(', ')[:3]) + ' —' + a.split('—')[1]).strip(),
        lambda a: (', '.join(a.split('—')[0].split(', ')[:2]) + ' —' + a.split('—')[1]).strip(),
        lambda a: (a.split('—')[0].split(', ')[0] + ' —' + a.split('—')[1]).strip(),
        lambda a: (a.split('—')[0].split(' feat. ')[0] + ' —' + a.split('—')[1]).strip(),
        lambda a: (a.split('—')[0].split(' ft ')[0] + ' —' + a.split('—')[1]).strip(),
        lambda a: (a.split('—')[0].split(' & ')[0] + ' —' + a.split('—')[1]).strip(),
        lambda a: (a.split('—')[1]).strip()
    ]
    
    for tool in tools:
        yield tool


def update_status(_current_playing):
    response = requests.get(bd.group_link)
    current = BeautifulSoup(response.text, features="html.parser").find_all(class_='pp_status')
    if current:

        track = current[0].contents[0]
        music_status = "🎧 VK Музыка | " + track
        shorter = shorten_track_name()
        while len(music_status) > 70:
            try:
                track = next(shorter)(track)
                music_status = "🎧 VK Музыка | " + track
            except StopIteration:
                music_status = default_status

        if _current_playing != track:
            with TelegramClient('anon', api_id, api_hash) as client:
                client(functions.account.UpdateProfileRequest(about=music_status))
            print(f"🆗 Установил статус: «{music_status}»")

        return track

    if _current_playing is not None:
        
        with TelegramClient('anon', api_id, api_hash) as client:
            client(functions.account.UpdateProfileRequest(about=default_status))    
        print(f"🆗 Установил статус: «{default_status}»")
        time.sleep(10)

    return None


if __name__ == '__main__':
    print('🚀 Запускаем...')
    while True:
        try:
            time.sleep(5)
            current_playing = update_status(current_playing)
        except Exception as e:
            print(f'⚡ Ошибка: {str(e)}')
