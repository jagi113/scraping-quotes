from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def get_quotes():
    chrome.get('https://quotes.toscrape.com/page/1/')

    page = QuotesPage(chrome)

    for quote in page.quotes:
        print(quote)
        
def search_for_quote():
    chrome.get('https://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)
    
    authors = page.get_available_authors()
    print(f"Select one of these authors: [{' | '. join(authors[1:])}]")
    author = input("Enter the author you would like quotes from: ")
    page.select_author(author)
    
    tags = page.get_available_tags()
    print(f"Select one of these tags: [{' | '. join(tags[1:])}]")
    tag = input("Enter the tag you would like quote about: ")
    page.select_tag(tag)
    
    page.search_button.click()
    
    print(page.dropdown_quote)
    

search_for_quote()