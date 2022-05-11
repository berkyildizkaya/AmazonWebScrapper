import requests
from bs4 import BeautifulSoup
import telegram
import time
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
url = "https://www.amazon.com.tr/gp/product/B08ZSRH1SH/ref=ox_sc_act_title_1?smid=A15RHDN1RI1XDW&th=1"
page = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(page.content, features="lxml")
bot = telegram.Bot("1324090909:AAG-EgImotzJmYxgZtw_BxhQMtS2Or7DSmU")
while True:
    
    price = soup.find("span",{"class":'a-price-whole'}).text
    # price = soup.find("span",{"class":'a-price-whole'}).getText()
    price2 = int(price.replace('.',' ').replace(',',' ').replace(' ', ''))
    

    # price2 = int(price)
    if price2 <= 3200:
        bot.send_message(chat_id="-412479129", text='Monitörün fiyatı şuan {}'.format(price2))
    time.sleep(1800)
