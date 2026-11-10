# Python Scripts

Eight small Python projects written while learning the language: two turtle games, a quiz, a timer interface, a letter generator and three web scraping scripts.

## Projects

| Folder | What it does |
| --- | --- |
| `1_Quiz_challenge` | True or false quiz in the terminal that keeps score. |
| `2_snake_game` | Snake game drawn with `turtle`, with a scoreboard that saves the high score to `data.txt`. |
| `3_US_State_Game` | Guess the 50 US states; each correct answer is written on a blank map, and the states you missed are saved to `states_to_learn.csv`. |
| `4_pomodoro` | Tkinter Pomodoro timer: 25 minute work sessions, 5 minute breaks and a 20 minute break after every fourth session, with a tick for each finished session. |
| `5_mail_tracker` | Fills a letter template with each name from a list and saves one letter per person. |
| `6_Amazon_price_tracker` | Scrapes the price of an Amazon product and sends an email alert when it drops below a set price. |
| `7_Musical_Time_Machine` | Asks for a date and scrapes the song titles from the Billboard Hot 100 chart for that day. |
| `8_data_entry_job_automation` | Scrapes rental listings from Zillow and enters them into a Google Form with Selenium. |

## Tech

- Python 3
- `turtle` and Tkinter for the games and interface
- pandas for the US states data
- requests, BeautifulSoup, lxml and Selenium for scraping
- smtplib for email

## Run it locally

Each project runs on its own from its folder, for example:

```bash
cd 2_snake_game
python main.py
```

The scraping scripts need extra packages:

```bash
pip install -r requirements.txt
```

The Amazon price tracker sends its alert from a Gmail account. Set the address and a Gmail app password as environment variables before running it:

```bash
export ALERT_EMAIL="you@gmail.com"
export ALERT_EMAIL_APP_PASSWORD="your-app-password"
```

The Zillow and Billboard pages change their HTML often, so the CSS class names in those scrapers may need updating.

## Changes since 2023

Ahmed Amine Tiffrent moved the Gmail login out of the code, fixed bugs in the quiz, the US states export, the chart date and the listing scraper, finished the Pomodoro timer and added `requirements.txt`.

---

Author: Aymen Allag ([allagaymen](https://github.com/allagaymen)) · README by Ahmed Amine Tiffrent ([portfolio](https://www.aminetiffrent.com/portfolio))
