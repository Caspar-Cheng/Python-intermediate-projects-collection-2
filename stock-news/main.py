import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "123456789"
auth_token = "123456789"

news_api = "123456789"
stock_api = "123456789"


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": stock_api
}

# Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, stock_parameters)
stock_data = response.json()["Time Series (Daily)"]
# yesterday = datetime.date.today() - datetime.timedelta(days=1)
data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_closing_price = float(data_list[1]["4. close"])
difference = abs(yesterday_closing_price - day_before_closing_price)
percentage = round((difference / yesterday_closing_price) * 100)
if percentage > 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": news_api
    }

    # https://newsapi.org/ to get the first 3 news pieces for the COMPANY_NAME.
    response = requests.get(NEWS_ENDPOINT, news_parameters)
    articles = response.json()["articles"][:3]
    info = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    # Send articles to phone via twilio sms service
    client = Client(account_sid, auth_token)
    for article in info:
        message = client.messages.create(
            body=article,
            from_='twilio phone number',
            to='your assigned phone number'
        )
