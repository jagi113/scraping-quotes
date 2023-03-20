from selenium.webdriver.common.by import By


from locators.quote_locators import QuoteLocators, DropdownQuoteLocators


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote (quote content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent
        
    def __repr__(self) -> str:
        return f'<Quote {self.content}, by {self.author}>'
        
    @property
    def content(self) -> str:
        locator = QuoteLocators.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
    
    @property
    def author(self) -> str:
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
    
    @property
    def tags(self) -> list[str]:
        locator = QuoteLocators.TAG
        return [tag.text for tag in self.parent.find_elements(By.CSS_SELECTOR, locator)]
    
    
class DropdownQuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote (quote content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent
        
    def __repr__(self) -> str:
        return f'<Quote {self.content}, by {self.author}>'
    
    @property
    def content(self) -> str:
        locator = DropdownQuoteLocators.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
    
    @property
    def author(self) -> str:
        locator = DropdownQuoteLocators.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text