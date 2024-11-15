from datetime import datetime
from pytz import timezone
import requests
from bs4 import BeautifulSoup

def commands():

    my_commands = {
        "1":".dos >>> دلار سلیمانیه",
        "2":".dof >>> دلار بازار داخلی",
        "3":".doc >>>  دلار کانادا",
        "4":".eur >>> یورو اروپا",
        "5":".chf >>> فرانک سوئیس",
        "6":".gbp >>> پوند انگلیس",
        "7":".iqd >>> دینار عراق",
        "8":".try >>> لیر ترکیه",
        "9":".btc >>> بیت کوین",
        "10":".eth >>> اتریوم",
        "11":".mgl >>> مثقال طلا",
        "12":".bhr >>> سکه بهار آزادی",
        "13":".imm >>> سکه امامی",
        "14":".bnk >>> کارت بانکی",
        "15":".mob >>> شماره موبایل",
        }

    command = "\n".join(my_commands.values())

    return command

def time_request():
    time = datetime.now(timezone('Asia/Tehran')).strftime("****\nTIME:%X\nDATE:%x\n****")
    return time

def get_data(name:str):
    try:
        url = f"https://www.tgju.org/profile/price_{name}"
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "html.parser")
        price = soup.find_all("td", {"class":"text-left"})[0]
        last_time = soup.find("span", {"class":"tgju-widget-up-i"})
        h,m,s=list(map(int, last_time.text.split(":")))
        time = str(datetime.now().replace(hour=h,minute=m,second=s))[11:19]
    
    except ValueError:
        time = last_time.text

    return [price.text, time]

def get_data_crypto(name: str):                                  
    try:
        url = f"https://www.tgju.org/profile/crypto-{name}"
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "html.parser")
        price = soup.find_all("td", {"class":"text-left"})[0]
        last_time = soup.find("span", {"class":"tgju-widget-up-i"})
        h,m,s=list(map(int, last_time.text.split(":")))
        time = str(datetime.now().replace(hour=h,minute=m,second=s))[11:19]
    
    except ValueError:
        time = last_time.text

    return [price.text, time]

def get_data_gold(name: str):
    try:
        url = f"https://www.tgju.org/profile/{name}"
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "html.parser")
        price = soup.find_all("td", {"class":"text-left"})[0]
        last_time = soup.find("span", {"class":"tgju-widget-up-i"})
        h,m,s=list(map(int, last_time.text.split(":")))
        time = str(datetime.now().replace(hour=h,minute=m,second=s))[11:19]
    
    except ValueError:
        time = last_time.text

    return [price.text, time]

