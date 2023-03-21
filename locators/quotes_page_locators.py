from selenium.webdriver.common.by import By

class QuotesPageLocators:
    QUOTE = 'div.quote'
    
class DropdownQuotesPageLocators:
    AUTHOR = By.CSS_SELECTOR, "select#author"
    TAG= By.CSS_SELECTOR, "select#tag"
    SEARCH_BUTTON = By.CSS_SELECTOR, "input[name='submit_button']"
    QUOTE = By.CSS_SELECTOR, "div.quote"
    