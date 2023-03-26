import json
from configparser import ConfigParser
import requests

parser = ConfigParser()
kubali = "\033[32;1m"
kataa = "\033[31;1m"
siani = "\033[0;36m"
mwisho = "\033[0m"
teal_color = '\033[38;2;100;182;172m'
orange = "\033[0;33m"
kidude = '[+]'

parser.read("midude/config.ini")
def check_balance():
    try:
        URL = 'https://apisms.beem.africa/public/v1/vendors/balance'
        api_key = parser.get("key","api")
        secret_key = parser.get("key","secret")
        content_type = 'application/json'
        apikey_and_apisecret = api_key + ':' + secret_key


        headers = {
            'Content-Type': content_type,
            'Authorization': 'Basic ' + apikey_and_apisecret,
        }
        #tunaondoa warning za kipumbavu kutoka urllib3
        requests.packages.urllib3.disable_warnings()

        first_request = requests.get(url=URL,  headers=headers, auth=(api_key, secret_key), verify=False).text

        try:
            balance = json.loads(first_request)['data']['credit_balance']
            return balance
        except KeyError:
            pass    

        #print(first_request)
    except Exception:
        print(f"{kataa}{kidude}Oops! Check Your Internet Connection{mwisho}")    
