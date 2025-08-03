import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = input("Enter your stock API key: ")
NEWS_API_KEY = input("Enter your news API key: ")
TWILIO_SID = input("Enter your Twilio SID: ")
TWILIO_AUTH_TOKEN = input("Enter your Twilio auth token: ")

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
    }

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round((difference / float(yesterday_closing_price)) * 100)

# If difference in percentage is greater than 5, use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percentage) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)

# Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number. 

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


# Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+13349464313",
        to=input("Enter your phone number: ")
    )
