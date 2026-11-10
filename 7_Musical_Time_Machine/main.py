from bs4 import BeautifulSoup
import requests
import datetime

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = datetime.date(year, month, day)

print(date1)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date1.isoformat()}/")
response_text = response.text

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select("li ul li h3")
song_names = [title.getText().strip() for title in titles]
print(song_names)
print(len(song_names))
