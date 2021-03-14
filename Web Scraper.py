import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'the url of your item'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text() #container that the title is in
    price = soup.find(id="priceblock_ourprice").get_text() #container that the price is in
    converted_price = float(price[1:])

    if(converted_price < 24.9): #the alert price
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email', 'your password')

    subject = 'Price fell down!'
    body = 'Check the amazon link 'link of item'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
       'email sender',
       'email reciever',
      msg
   )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 1440)
