from flask import Flask, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY="TxRRz1nADBLAa09PhaYPutaIgZLLtemz"

def get_latest_news():
    news_data = requests.get(f'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={NEWS_API_KEY}').json()
    return news_data['results']


@app.route('/')
def news_headlines():
    news_articles = get_latest_news()
    return render_template("index.html", news_articles=news_articles)