import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSel58_PvciOuOVXIOv8tdff4fEFfe1Fx94oFJ38r8brhOxyRQ/viewform?usp=sf_link"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url ="https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.18726576757813%2C%22east%22%3A-121.67939223242188%2C%22south%22%3A37.61337875552385%2C%22north%22%3A37.93685032995972%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
response = requests.get(url, headers=headers)
zillow_link = response.text
# COLLECTION PRICES
soup: BeautifulSoup = BeautifulSoup(zillow_link, "lxml")
price_lists= soup.findAll(name="div", class_='StyledPropertyCardDataArea-c11n-8-82-3__sc-yipmu-0 gMDnGj')

appartement_prices = []
for n in range(len(price_lists)-1):
    price = price_lists[n]
    appartement_prices.append(price.text)

print(appartement_prices)

# COLLECTION ADDRESSES
address_lists = soup.findAll(name="address")

appartement_address = []
for n in range(len(address_lists)-1):
    address = address_lists[n]
    appartement_address.append(address.text)

print(appartement_address)

# COLLECTION LINKs
links_lists = soup.findAll(name="a", class_='StyledPropertyCardDataArea-c11n-8-82-3__sc-yipmu-0 hiBOYq property-card-link')

appartement_links = []
for n in range(len(links_lists)-1):
    link = links_lists[n]['href']
    appartement_links.append(link)

print(appartement_links)

# FILL FORM
chrome_driver_path = '/home/aymen-allag/Desktop/dev/chromedriver_linux64/chromedriver'
driver: WebDriver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(appartement_prices)):
    driver.get(form_link)
    time.sleep(5)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(appartement_address[n])
    price.send_keys(appartement_prices[n])
    link.send_keys(appartement_links[n])
    submit_button.click()

driver.quit()

#email_address: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
#email_address.send_keys("a.allag@esi-sba.dz")
#btn_email: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
#btn_email.click()
#password_address: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
#password_address.send_keys("Zinou1234#")
#btn_password: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
#btn_password.click()

