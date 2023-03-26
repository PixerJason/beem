from prettytable import PrettyTable


kubali = "\033[32;1m"
mwisho = "\033[0m"
# Define the menu as a list of dictionaries

def menu():
    #alafu sijatumia tena prettytable mamae haha
    print(f"""
        {kubali}[1]{mwisho}:  Send SMS
        {kubali}[2]{mwisho}:  Change API and Secret Key
        {kubali}[3]{mwisho}:  Request Sender Name
        {kubali}[4]{mwisho}:  Show Currently Sender names
        {kubali}[5]{mwisho}:  Show Sent Messages
        {kubali}[6]{mwisho}:  Quit!
        """
          )

 