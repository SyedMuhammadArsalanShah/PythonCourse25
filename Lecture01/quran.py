import requests


response= requests.get("http://api.alquran.cloud/v1/surah")
surah_list=response.json()["data"]
if response.status_code==200:
    for s in surah_list:
        print(f"{s["englishName"]}")