#This python scraps the web every 5 seconds to web scrap BITCOIN price from google finance
#And if there's a change of a certain amount, user is notified

import requests
from bs4 import BeautifulSoup
import time

#method to compare the prices; returns true if the difference is more than $10
def compare(curPrice, prevPrice):
    if abs(curPrice - prevPrice) > 10:
        return True
    else:
        return False


#settimg up the initial price
prevPrice = 0

while True:
    r = requests.get('https://www.google.com/finance/quote/BTC-CAD')

    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='YMlKec fxKbKc')
    curPrice = float(s.text.replace(',',''))

    if compare(curPrice, prevPrice):
        print(time.strftime("%H:%M:%S: ") + "Price change of more than $10")
    else:
        print(time.strftime("%H:%M:%S: ") + "NO CHANGE")
    prevPrice = curPrice

    #checking every 5 seconds
    time.sleep(5)