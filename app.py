import requests

from pages.quotes_page import QuotesPage

page_content = requests.get('https://quotes.toscrape.com/page/1/').content

page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)