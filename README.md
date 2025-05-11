# 🌟 Daily Quote Scraper & Email Sender 📬

A Python script that scrapes inspirational quotes and sends them via email on a schedule!

## ✨ Features

- **Web Scraping Magic** 🕷️  
  Automatically harvests quotes from [Quotes to Scrape](https://quotes.toscrape.com)
- **Smart Pagination** 🔄  
  Crawls through all available pages to build a complete quote collection
- **Scheduled Email Delivery** ⏰  
  Sends random quotes daily at your preferred time
- **JSON Backup** 💾  
  Saves all quotes with author info in a neat JSON file

## 🛠️ How It Works

### 🔍 Scraping Engine
```python
def scrape_quotes(soup):
    # Extracts:
    # - Quote text
    # - Author name
    # - Author profile link
    # Saves to beautiful JSON format
```

## 📧 Email System
```python
def send_email():
    # Uses SMTP with SSL
    # Randomly selects one quote daily
    # Sends at precise scheduled times
```

## ⏱️ Scheduling Magic
```python
# First run at:
first_email_time = dt.datetime(2025,5,11,10,49,0) 

# Then repeats every:
interval = dt.timedelta(hours=24)
```

## 🚀 Setup Guide

1: Install requirements
```python
pip install requests beautifulsoup4 python-dotenv
```
2: Configure email
Create .env file:
```python
EMAIL_USER=your@gmail.com
EMAIL_PASS=your_app_password
```
3: Set your schedule
Modify in main.py:
```python
first_email_time = dt.datetime(YEAR,MONTH,DAY,HOUR,MINUTE,SECOND)
interval = dt.timedelta(hours=24)  # Change for different frequency
```

4: Run it!
```python
python main.py
```
## 🌈 Sample Output

Email Content:

    "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."
    ― Albert Einstein

## JSON Structure:
```json
{
    "Quote text": {
        "author": "Author Name",
        "author_link": "https://.../author/..."
    }
}
```

## 💡 Pro Tips
1: 🔒 Use App Passwords for Gmail
2: 🌐 Change SMTP settings for different email providers:
```python
    # Outlook: 'smtp.office365.com', 587
    #Yahoo: 'smtp.mail.yahoo.com', 465
```
3: 📅 Want weekly quotes? Change hours=24 to days=7
4: 💌 Add multiple recipients: msg['To'] = "email1@x.com, email2@y.com"

## 🤝 Contributing
Found a bug? Want to improve something?
PRs are welcome! Just fork and submit your changes.


Made with ❤️ and Python 🐍
Happy quoting! ✉️💬