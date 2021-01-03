
from flask import Flask
from flask import render_template
from webscraper import webScraper

app = Flask(__name__)
scraper_data = webScraper()


@app.route('/')
def home():
    return render_template('test.html', scraper_data=scraper_data)

if __name__ == '__main__':
    app.run(debug=True)