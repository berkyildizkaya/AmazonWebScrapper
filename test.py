from email import header
import requests
from bs4 import BeautifulSoup
import telegram
import time
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
productList = []
productPriceList = []
count = 0
#STEP 1 https://telegram.me/BotFather go to link
# STEP 2 say /start
# STEP 3 /newbot
# STEP 4 give a nickname for bot
# STEP 5 give a username but It must end in `bot` keyword
# STEP 6 Father bot give a Token.
#STEP 7 Create a group chat
# STEP 8 invite @getidsbot to group and take this chat id starts with -
bot = telegram.Bot("BotToken#Step6")
productCount = int(input('Please specify the number of products you want to track\n'))
controlTime = int(input("Enter the time you want to check in seconds\n"))
for i in range(productCount):
    productList.append(input("Please enter the product link on Amazon\n"))
    productPriceList.append(int(input("Enter the price to be notified.\n")))
while True:
    for x in productList:
        page = requests.get(x,headers=HEADERS)
        soup = BeautifulSoup(page.content, features="lxml")
        price = soup.find("span",{"class":'a-price-whole'}).text
        price2 = int(price.replace('.',' ').replace(',',' ').replace(' ', ''))
        productName = soup.find("span",{"id":'productTitle'}).text.strip()
        productSymbol = soup.find("span",{"class":'a-price-symbol'}).text
        if price2 <= productPriceList[count]:
            bot.send_message(chat_id="#STEP8", text='Product Name :{} Price:{}{} The product added to the list is on sale '.format(productName,price2,productSymbol))
        count+=1
    time.sleep(controlTime)
    count=0

