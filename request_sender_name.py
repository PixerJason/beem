import json
from configparser import ConfigParser
import requests

kubali = "\033[32;1m"
kataa = "\033[31;1m"
siani = "\033[0;36m"
mwisho = "\033[0m"
teal_color = '\033[38;2;100;182;172m'
orange = "\033[0;33m"
kidude = '[+]'

mandonga = ConfigParser()
mandonga.read("midude/config.ini")
def request_sender_id():
    try:
        URL = 'https://apisms.beem.africa/public/v1/sender-names'
        api_key = mandonga.get("key","api")
        secret_key = mandonga.get("key","secret")
        content_type = 'application/json'
        apikey_and_apisecret = api_key + ':' + secret_key

        id = input(f"{kubali}{kidude}{mwisho}Enter Sender Id (Maximum 11 Characters): ")
        desc = input(f"{kubali}{kidude}{mwisho}Enter Description (Maximum 17 characters): ")
        if len(id) > 11:
            print(f"{kataa}{kidude}Sender Name Exceeded 11 characters{mwisho}")
            
        else:
            if  id and desc:
                pass
            else:
                print(f"{kataa}{kidude}Sender Id and Description Are Required!{mwisho}")
                pass      
        headers = {
            'Content-Type': content_type,
            'Authorization': 'Basic ' + apikey_and_apisecret,
        }


        data = {
            'senderid' : id,
            'sample_content' : desc
        }

        requests.packages.urllib3.disable_warnings()
        first_request = requests.post(url=URL,  data=json.dumps(data),headers=headers, auth=(api_key, secret_key), verify=False).text

        try:
            nimechoka = json.loads(first_request)["data"]["message"]
            print(nimechoka)  
        except KeyError:
            print(f"{kubali}{kidude}Sender ID Requested Successfully{mwisho}")
        
    except Exception:
        print(f"{kataa}{kidude}Oops! Check Your Internet Connection{mwisho}") 

