from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
chrome.get('https://quotes.toscrape.com/page/1/')

page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)