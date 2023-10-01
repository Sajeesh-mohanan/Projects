import requests
import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
YESTERDAY = (datetime.date.today() - datetime.timedelta(days=1))
DAY_BFR_YST = (datetime.date.today() - datetime.timedelta(days=2))


## https://www.alphavantage.co API
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday.

def stockapi():
    aplhavantage_apikey = os.environ.get('apl_apikey')
    alphavantage_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={aplhavantage_apikey}'
    alphavantage_response = requests.get(url=alphavantage_url)

    alphavantage_data = alphavantage_response.json()
    yesterday_stock_price = float(alphavantage_data["Time Series (Daily)"][f'{YESTERDAY}']['4. close'])
    day_bfr_yst_stock_price = float(alphavantage_data["Time Series (Daily)"][f'{DAY_BFR_YST}']['4. close'])

    stock_price_difference = yesterday_stock_price - day_bfr_yst_stock_price
    stock_percentage = day_bfr_yst_stock_price*0.05

    if stock_percentage <= abs(stock_price_difference):
        if stock_price_difference < 0:
            stock_message = "Tesla stocks down ⬇%5!"
        else:
            stock_message = "Tesla stock are UP ⬆%5!"

        return stock_message
    else:
        return None


## https://newsapi.org API Function
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def getnews(i):
    newsapi_parameters = {
        "q": 'tesla',
        "apikey": os.environ.get('newsapikey'),
    }
    newsapi_url = "https://newsapi.org/v2/top-headlines?"
    newsapi_response = requests.get(url=newsapi_url, params=newsapi_parameters)
    newsapi_data = newsapi_response.json()["articles"]
    news_titles = f"{newsapi_data[i]['author']} : {newsapi_data[i]['title']}\nURL: {newsapi_data[i]['url']}"
    return news_titles


## twilio setup
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# twilio details
account_sid = 'AC111bc7c9f104791f926e9b0431bc6781'
auth_token1 = os.environ.get('auth_token')
client = Client(account_sid, auth_token1)

if 0 <= YESTERDAY.weekday() <= 5 and stockapi() is not None:
    news = f"{stockapi()}\n{getnews(0)}\n\n{getnews(1)}\n\n{getnews(2)}"

    message = client.messages.create(
        body=news,
        from_=os.environ.get('from_number'),
        to=os.environ.get('to_number')
    )
    print(message.status)

