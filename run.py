import requests
import random
from faker import Faker
"""
Gleam auto entry
Date: 27/aug/2021
Author: Cori
"""
refferal = input("Input refferal link [ ex: https://gleam.io/tFUIH/hrb-whitelist-reg?gsr=tFUIH-YmZe7vZVq8 ]: ")
reff_info = refferal.split("gsr=")[1].split("-")
fake = Faker()
req = requests.Session()

headers = {
    'authority': 'gleam.io',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://gleam.io',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': refferal,
    'accept-language': 'en-US,en;q=0.9',
}

proxies = {
    'http':  'http://dziu69:saninkicker123@162.55.13.177:10000',
    'https': 'http://dziu69:saninkicker123@162.55.13.177:10000'
}
def entry_campaign():
    name = random.choice([fake.name().lower(), fake.name().lower()[::-1]])
    print("register name: %s" % name)
    print("email: %s@gmail.com" % name.replace(' ', ""))
    data = '{"campaign_key":"%s","contestant":{"firstname":"","lastname":"","name":"%s","email":"%s@gmail.com"},"additional_details":false}'%(reff_info[0], name, name.replace(" ", ""))
    response = req.post('https://gleam.io/set-contestant', headers=headers, data=data, proxies=proxies)
    if response.status_code == 200:
        if "ip ban" in response.text:
            print("IP GOT BANNED!")
        else:
            print("Success register event!")
    else:
        print("Failed register event, StatusCode: ", response.status_code)

def get_cookies():
    req.get('https://gleam.io/%s/hrb-whitelist-reg'%(reff_info[0]), headers=headers, proxies=proxies)
    print("Renew the cookies!")

def get_ip():
    ip = requests.get("https://api.ipify.org?format=json", proxies=proxies).json()["ip"]
    print("Your ip changed to ", ip)
while True:
    try:
        get_ip()
        get_cookies()
        entry_campaign()
        req.cookies.clear()
        print()
    except Exception as E:
        print(E)