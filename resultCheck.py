import requests as rt 
from bs4 import BeautifulSoup
from playsound import playsound

import time


url = 'https://ktu.edu.in/'

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    'Cache-Control': 'no-cache',
    "Pragma": "no-cache"
}

ktu = rt.get(url,headers=headers)

ktusoup = BeautifulSoup(ktu.content,'html.parser')


content =  ktusoup.find(class_="annuncement").get_text()



while(True):
    if "B.Tech S6" in content:
        playsound("sound.mp3")
        print("result vannu.....:(")

    ktu = rt.get(url,headers=headers)
    ktusoup = BeautifulSoup(ktu.content,'html.parser') 
    content =  ktusoup.find(class_="annuncement").get_text()
    print("test")
    time.sleep(60)
