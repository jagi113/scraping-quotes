from driver.driver import get_chrome
from pages.quotes_page import QuotesPage


chrome = get_chrome()

def get_quotes()->None:
    chrome.get('https://quotes.toscrape.com/page/1/')

    page = QuotesPage(chrome)

    for quote in page.quotes:
        print(quote)


def search_for_quote()->None:
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


def main()->None:
    while True:
        choice = input("Do you want to get all quotes ('all'), or look for a specific one ('search')? ")
        if choice == "quit":
            break
        elif choice == "all":
            get_quotes()
        elif choice == "search":
            search_for_quote()
        else:
            print("Unrecognized error! Try: all, search or quit! ")

if __name__ == "__main__":
    main()