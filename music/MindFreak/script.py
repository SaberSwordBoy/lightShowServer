import requests
import time

URL=""

def send_req(func):
    req = requests.post(URL, data={"func": func})

def start():
    send_req("allRed")