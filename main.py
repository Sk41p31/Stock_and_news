import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
KEY = "ZCMGDK2R9JLH1F7X"

NEWS_KEY = "8828f6cd1d194bf2a5b479bc0520a276"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": KEY,
}

news_params = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME,
    "searchin": "title",

}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
json_response = response.json()['Time Series (Daily)']
keys_list = list(json_response.keys())

yesterday_closing = json_response[keys_list[0]]['4. close']
b_yesterday_closing = json_response[keys_list[1]]['4. close']

dif = float(b_yesterday_closing) - float(yesterday_closing)
abs_dif = abs(dif)

change_mark = None
if dif < 0:
    change_mark = "🔺"
else:
    change_mark = "🔻"

percent_diff = abs_dif / float(yesterday_closing) * 100

if percent_diff > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    last_3_articles = articles[:3]

    first_news = [f"{STOCK_NAME}: {change_mark}{round(percent_diff, 2)}%\n"
                  f"Headline: {article['title']}\n"
                  f"Brief: {article['description']}" for article in last_3_articles]
    for i in first_news:
        print(i)
