import json
import requests
from configparser import ConfigParser
from prettytable import PrettyTable
import colorama 

colorama.init()
kubali = "\033[32;1m"
kataa = "\033[31;1m"
siani = "\033[0;36m"
mwisho = "\033[0m"
teal_color = '\033[38;2;100;182;172m'
orange = "\033[0;33m"
kidude = '[+]'
mbuzi = ConfigParser()
mbuzi.read("midude/config.ini")

def check_sender_names():
    try:
        URL = 'https://apisms.beem.africa/public/v1/sender-names'
        api_key = mbuzi.get("key","api")
        secret_key = mbuzi.get("key","secret")
        content_type = 'application/json'
        apikey_and_apisecret = api_key + ':' + secret_key


        headers = {
            'Content-Type': content_type,
            'Authorization': 'Basic ' + apikey_and_apisecret,
        }

        requests.packages.urllib3.disable_warnings()
        first_request = requests.get(url=URL,  headers=headers, auth=(api_key, secret_key), verify=False).text

        x = PrettyTable()
        x.field_names = ["Sender Name","Description","Status","Date Of Creation"]
        try:
            main = json.loads(first_request)["data"]
        except KeyError:
            print(f"{kataa}{kidude}Oops! Invalid Keys, Please Add Correct Keys{mwisho}")   
            exit(1) 
        for i in main:
            status = i["status"]
            if status == "active":
                status = colorama.Fore.GREEN + status + colorama.Style.RESET_ALL
            else:
                status = status = colorama.Fore.YELLOW + status + colorama.Style.RESET_ALL    
            x.add_row([i["senderid"],i["sample_content"],status,i["created"]])
        print(x)    
    except Exception:
        print(f"{kataa}{kidude}Oops! Check Your Internet Connection{mwisho}")             

