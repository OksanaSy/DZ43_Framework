from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from pages.book_page import BookPage


class LandingPage(BasePage):

    SITE_HEADER_PERSONAL = (By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[3]')
    SEARCH_FIELD = (By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[2]/form/input[1]')
    FOUND_BOOK = (By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[2]/form/div/div/div[1]/a/div/div[1]')



    def __init__(self, driver):
        super().__init__(driver)
    @property
    def site_header_personal(self):
        return self.element(LandingPage.SITE_HEADER_PERSONAL)

    @property
    def search_book(self):
        return self.element(LandingPage.SEARCH_FIELD)

    @property
    def found_book(self):
        return self.element(LandingPage.FOUND_BOOK)


    def is_page_displayed(self):
        return self.site_header_personal.is_displayed()

    def to_profile_page(self):
        return ProfilePage(self.driver)

    def search_book_input(self, book_n):
        self.search_book.clear()
        self.search_book.send_keys(book_n.name)

    def select_book(self):
        self.found_book.click()

    def succesful_search(self, book_n):
        self.search_book_input(book_n)
        self.select_book()
        return BookPage(self.driver)