from locators.quotes_page_locators import QuotesPageLocators
from parsers.qoute import QuoteParser

from selenium.webdriver.common.by import By

class QuotesPage:
    def __init__(self, page):
        self.page = page
        
    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.page.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(e) for e in quote_tags]