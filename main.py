import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.message import EmailMessage
import random
import datetime as dt
import time

base_url = "https://quotes.toscrape.com"
current_url = base_url
scraped_quotes = {}

def scrape_quotes(soup):
    quotes = soup.find_all('div', {'class': 'quote'})

    for quote in quotes:
        text = quote.find('span', {'class': 'text'}).get_text(strip=True)
        author = quote.find('small', {'class': 'author'}).get_text(strip=True)
        author_link = base_url + quote.find('a')['href']
        scraped_quotes[text] = {
            'author': author,
            'author_link': author_link
        }

    with open('file.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_quotes, f, indent=4, ensure_ascii=False)
    return scraped_quotes


def get_next_page(soup):
    global current_url
    next_page = soup.find('li', {'class': 'next'})
    if next_page:
        next_page_url = next_page.find('a')['href']
        current_url = base_url + next_page_url
        return True
    return False


def send_email(sender, password, recipient, subject, body):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # For Gmail
            smtp.login(sender, password)
            smtp.send_message(msg)
        print(f"Email sent successfully at {send_time}")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email(
    sender="sender email you've connected to in smtp.login",
    password='your password from .env file',
    recipient="recipient email (can be a list of emails)",
    subject="Random Quote - Daily!",
    body=random.choice(list(scraped_quotes.keys()))
    )   


if __name__ == "__main__":
    while current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = scrape_quotes(soup)
        print(f"Scraped {len(quotes)} quotes from {current_url}")
        
        if not get_next_page(soup):
            break


first_email_time = dt.datetime(2025,5,11,10,49,0) # set your sending time in UTC
interval = dt.timedelta(hours=24) # set the interval for sending the email
send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval    