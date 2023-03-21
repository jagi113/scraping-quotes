from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from locators.quotes_page_locators import QuotesPageLocators
from parsers.qoute import QuoteParser, DropdownQuoteParser

from locators.quotes_page_locators import DropdownQuotesPageLocators


class QuotesPage:
    def __init__(self, page):
        self.page = page
        
    @property
    def quotes(self)-> list[QuoteParser]:
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.page.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(e) for e in quote_tags]
    
    # DROPDOWN OPERATIONS
    @property
    def author_dropdown(self) -> Select:
        locator = DropdownQuotesPageLocators.AUTHOR
        element = self.page.find_element(*locator)
        return Select(element)
    
    def get_available_authors(self) -> list[str]:
        return [option.text.strip() for option in self.author_dropdown.options]
    
    def select_author(self, author_name:str):
        self.author_dropdown.select_by_visible_text(author_name)
        
    @property
    def tags_dropdown(self) -> Select:
        locator = DropdownQuotesPageLocators.TAG
        element = self.page.find_element(*locator)
        return Select(element)
    
    def get_available_tags(self) -> list[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]
    
    def select_tag(self, tag:str):
        self.tags_dropdown.select_by_visible_text(tag)
        
    
    @property
    def search_button(self) -> Select:
        locator = DropdownQuotesPageLocators.SEARCH_BUTTON
        element = self.page.find_element(*locator)
        return element
    
    @property
    def dropdown_quote(self)-> list[DropdownQuoteParser]:
        locator = DropdownQuotesPageLocators.QUOTE
        quote_tag = self.page.find_element(*locator)
        return DropdownQuoteParser(quote_tag)