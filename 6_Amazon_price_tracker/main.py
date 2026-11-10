import os
import smtplib

from bs4 import BeautifulSoup
import requests

# Gmail address and app password are read from the environment, never stored in the code
EMAIL = os.environ["ALERT_EMAIL"]
APP_PASSWORD = os.environ["ALERT_EMAIL_APP_PASSWORD"]

# Get the product price
url = "https://www.amazon.com/dp/B09TYVYRD9/ref=syn_sd_onsite_desktop_121?ie=UTF8&psc=1&pd_rd_plhdr=t"
headers = {'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
            }
responce = requests.get(url, headers=headers)
your_web_page = responce.text
soup = BeautifulSoup(your_web_page, "lxml")

price = soup.find(name="span", class_='a-price a-text-price a-size-medium apexPriceToPay').text
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# Send Email Alert When Price Below Preset Value
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 82

if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price_without_currency}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, APP_PASSWORD)
        print(result)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n{message}\n{url}"
        )
