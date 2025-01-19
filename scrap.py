#This python scraps the web every 5 seconds to retrieve BITCOIN price from google finance
#And if there's a change of a certain amount, user is notified

import requests
from bs4 import BeautifulSoup
import time
import smtplib

#method which notifies via email
def sendEmail(prevPrice, curPrice):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('upadhyayr003@gmail.com','WordPass_003RUpadhyay')

    subject = "Substantial price change in BTC"
    body = "price has changed from " + str(prevPrice) + " to " + str(curPrice)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('upadhyayr003@gmail.com', 'upadhyayr003@gmail.com', msg)


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

    #opening storage file
    f = open('btcTracker.csv', 'a+')
    f.write(time.strftime("%d-%m-%Y")  +','+  time.strftime("%H:%M:%S")  +','+  str(curPrice)  +  '\n')
    f.close()

    #skipping the first comparison, as the change will naturally be more than $10
    if prevPrice != 0:
        if compare(curPrice, prevPrice):
            print(time.strftime("%H:%M:%S: ") + "Price change of more than $10")
            #sendEmail(prevPrice, curPrice)
        else:
            print(time.strftime("%H:%M:%S: ") + "NO MAJOR CHANGE")

    prevPrice = curPrice

    #checking every 5 seconds
    time.sleep(5)
