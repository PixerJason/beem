import os
try:
    import json
    import requests
    import colorama
    from datetime import datetime
    from prettytable import PrettyTable
    from menu import menu
    from check_sender_name import check_sender_names
    from request_sender_name import request_sender_id
    from check_balance import check_balance
    from time import sleep
    from configparser import ConfigParser

except ModuleNotFoundError:
    print(f"\033[32;1mInstalling Missing Packages...\033[0m")
    os.system("pip3 install requests > /dev/null")
    print("\033[32;1mDone\033[0m")
    os.system("pip3 install prettytable > /dev/null")
    print("\033[32;1mDone\033[0m")
    os.system("pip3 install datetime > /dev/null")
    print("\033[32;1mDone\033[0m")
    os.system("pip3 install configparser > /dev/null")
    print("\033[32;1mDone\033[0m")
    os.system("pip3 install json > /dev/null")
    print("\033[32;1mDone\033[0m")
    os.system("pip3 install time > /dev/null")
    print("\033[32;1mDone\033[0m")
    os.system("pip3 install colorama > /dev/null")
    print("\033[32;1mDone\033[0m")

parser = ConfigParser()

parser.read("midude/config.ini")
now = datetime.now()

#rangi za mchongo
kubali = "\033[32;1m"
kataa = "\033[31;1m"
siani = "\033[0;36m"
mwisho = "\033[0m"
teal_color = '\033[38;2;100;182;172m'
orange = "\033[0;33m"
kidude = '[+]'

#mazaga yangu ya baadae
ch_api = False
ch_sec = False

def check_key(ch_api,ch_sec):
    api = parser.get("key","api")
    secret = parser.get("key","secret")
    if  api and secret:
        pass
    else:
        set_api()

def userinfo():
    print(f"{teal_color}╒════════════════════════════════════════════╕\033[0m")
    print(" \033[0;41;36m                  USER INFO                \033[0m")
    print(f"{teal_color}╘════════════════════════════════════════════╛\033[0m")
    api = parser.get("key","api")
    secret = parser.get("key","secret")
    if  api and secret:
        ch_api = True
        ch_sec = True
        print(f"{kidude}API KEY     :   {kubali}{ch_api}{mwisho}")
        print(f"{kidude}SECRET KEY  :   {kubali}{ch_sec}{mwisho}")
    else:
        ch_api = False
        ch_sec = False
        print(f"{kidude}API KEY     :   {kataa}{ch_api}{mwisho}")
        print(f"{kidude}SECRET KEY  :   {kataa}{ch_sec}{mwisho}")

def balance_info():
    balance = check_balance()
    if balance == "0":
        print(f"{teal_color}╒════════════════════════════════════════════╕\033[0m")
        print(f"             {orange}[SMS BALANCE : {kataa}{balance}{mwisho}]\033[0m")
        print(f"{teal_color}╘════════════════════════════════════════════╛\033[0m")
        print(f"             Credit: Pixer Jason \033[0m")
    else:
        print(f"{teal_color}╒════════════════════════════════════════════╕\033[0m")
        print(f"             {orange}[SMS BALANCE : {kubali}{balance}{mwisho}]\033[0m")
        print(f"{teal_color}╘════════════════════════════════════════════╛\033[0m")
        print(f"             {kubali}Credit{mwisho}: Pixer Jason \033[0m")
        print(f"{teal_color}╒════════════════════════════════════════════╕\033[0m")
        print(" \033[0;41;36m                  MENU INFO                \033[0m")
        print(f"{teal_color}╘════════════════════════════════════════════╛\033[0m")  


def set_api():
    #midinyo inaanza
    while True:
        try:    
            api = input(f"{kidude}Enter Api Key From BeemAfrica: ")
            secret = input(f"{kidude}Enter Secret Key From BeemAfrica: ")
        
            if api and secret:
                ndoige = open("midude/config.ini","w")
                mandonga = f"[key]\napi = {api}\nsecret = {secret}"
                ndoige.write(mandonga)
                ndoige.close()
                break
            else:
                print(f"{kataa}{kidude}Api and Secret Fields Are Required!{mwisho}")
                sleep(2)
                os.system("cls")
        except KeyboardInterrupt:
            print(f"{kataa}\n{kidude}Operation Cancelled By User!{mwisho}")
            exit(1)

#njaa inaniuma kinyama yan dah!
def send_sms():
    URL = 'https://apisms.beem.africa/v1/send'
    api_key = f'{parser.get("key","api")}'
    secret_key = f'{parser.get("key","secret")}'
    content_type = 'application/json'
    apikey_and_apisecret = api_key + ':' + secret_key
    try: 
        phn_no = input(f"{kidude}Enter Phone Number starting with country without + Eg,2557111111: ")
        source_addr = input(f"{kidude}Enter Sender Name Or Press Enter To use Default: ")
        message = input(f"{kidude}Enter Message: ")
        if source_addr:
            source_addr=source_addr
        else:
            source_addr="INFO"
    except KeyboardInterrupt:
        print(f"\n{kataa}Operation Cancelled by user!{mwisho}")
        exit(1)

    try:        
        recipients = [
            {
                'recipient_id': 1,
                'dest_addr': phn_no,
            }
        ]
        
        data = {
            'source_addr': source_addr,
            'schedule_time': '',
            'encoding': '0',
            'message': message,
            'recipients': recipients,
        }

        headers = {
            'Content-Type': content_type,
            'Authorization': 'Basic ' + apikey_and_apisecret,
        }
        requests.packages.urllib3.disable_warnings()
        first_request = requests.post(url=URL, data=json.dumps(data), headers=headers, auth=(api_key, secret_key), verify=False).text
        with open("message/message.txt","a") as bibi:
            bibi.write(f"Mobile Number: {phn_no}\n")
            bibi.write(f"SMS Sent: {message}\n")
            bibi.write(f"Date and Time: {now}\n")
            bibi.write(f"{kubali}{kidude}{mwisho}Script By https://t.me/PixerJason\n")
            bibi.write("\n")
    except Exception:
        print(f"\n{kataa}{kidude}Opps! Please Check Your internet connection{mwisho}")  
        exit(1)  

    done = json.loads(first_request)["message"]
    #hapa nimecode kama boya haha
    if "Invalid" in done:
        print("")
        print(kataa,kidude,done,mwisho)
        input("press Enter To Continue...")
        os.system("clear")
        userinfo()
        balance_info()
        menu()
    else:
        print("")
        print(kubali,kidude,done,mwisho)   
        input("press Enter To Continue...")
        os.system("clear")
        userinfo()
        balance_info()
        menu()

def view_sent_messages():
    with open("message/message.txt", "r") as fuck:
        print(fuck.read())        

if __name__ == "__main__":
    while True:    
        os.system("clear")
        check_key(ch_api,ch_sec)
        os.system("clear")
        userinfo()
        balance_info()
        menu()
    
        try:
            chagua = input(f"{kidude}Enter Option (1-5): ")

            if chagua == "1":
                os.system("clear")
                send_sms()
                #break
            elif chagua == "2":
                set_api()
                print(f"{kubali}{kidude}API And Secret Key Updated!{mwisho}")
                input("press Enter To Continue...")
                os.system("clear")
                userinfo()
                balance_info()
                menu()
                #break
            elif chagua == "3":
                os.system("clear")
                request_sender_id()
                input("press Enter To Continue...")
                os.system("clear")
                userinfo()
                balance_info()
                menu()
                #break
            elif chagua == "4":
                os.system("clear")
                check_sender_names()
                input("press Enter To Continue...")
                os.system("clear")
                userinfo()
                balance_info()
                menu()
                #break
            elif chagua == "5":
                os.system("clear")
                view_sent_messages()
                input("press Enter To Continue...")
                os.system("clear")
                userinfo()
                balance_info()
                menu()
                #break
            elif chagua == "6":
                print(f"{kataa}\n{kidude}Oops! You've Quited{mwisho}")      
                exit(1)    
            else:
                print(f"{kataa}\n{kidude}Wrong Input Bitch!{mwisho}")
                sleep(1)
                os.system("clear")                          

        except KeyboardInterrupt:
            exit(1)    
        