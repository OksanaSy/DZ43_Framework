import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.my_books_page import MyBooksPage


class BookPage(BasePage):
    FOUND_BOOK_TITLE = (By.XPATH, '/html/body/div[1]/div[2]/main/div[1]/div[2]/div[1]/div[1]/div[1]/h1')
    WANT_TO_READ_BUTTON = (By.XPATH, '//*[@aria-label="Tap to shelve book as want to read"]')
    MY_BOOKS = (By.XPATH, '//*[@id="Header"]/div[2]/div[1]/nav/ul/li[2]/a')

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def found_book_title(self):
        return self.element(BookPage.FOUND_BOOK_TITLE)

    @property
    def want_to_read_button(self):
        return self.element(BookPage.WANT_TO_READ_BUTTON)

    @property
    def my_books(self):
        return self.element(BookPage.MY_BOOKS)

    def add_book(self):
        self.want_to_read_button.click()

    def go_to_my_books(self):
        self.my_books.click()

    def succesful_add(self):
        self.add_book()
        time.sleep(5)
        self.go_to_my_books()
        return MyBooksPage(self.driver)


