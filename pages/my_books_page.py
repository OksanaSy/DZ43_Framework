from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyBooksPage(BasePage):
    MY_BOOKS_TITLE = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/h1/a')
    NEW_BOOK = (By.XPATH, '//*[@title="Python Crash Course: A Hands-On, Project-Based Introduction to Programming"]')
    DELETE_BOOK = (By.XPATH, '//*[@data-confirm="Are you sure you want to remove Python Crash Course from your books? This will permanently remove this book from your shelves, including any review, rating, tags, or notes you have added. To change the shelf this book appears on please edit the shelves."]')
    CONFIRM_BUTTON = (By.XPATH, '// div[ @ role =“dialog”] // button[text() =“OK”]')

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def new_book_locator(self):
        return self.element(MyBooksPage.NEW_BOOK)

    @property
    def my_books_title_locator(self):
        return self.element(MyBooksPage.MY_BOOKS_TITLE)

    @property
    def delete_book_locator(self):
        return self.element(MyBooksPage.DELETE_BOOK)

    @property
    def confirm_delete(self):
        return self.element(MyBooksPage.CONFIRM_BUTTON)

    def delete_book(self):
        self.delete_book_locator.click()

    def confirm_delete(self):
        self.driver.switch_to.alert.accept()
        self.confirm_delete.click()

