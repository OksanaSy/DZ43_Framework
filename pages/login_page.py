from selenium.webdriver.common.by import By

from helpers.project_helpers import get_base_url
from pages.base_page import BasePage
from pages.landing_page import LandingPage


class LoginPage(BasePage):
    SIGNIN_REFERENCE = (By.XPATH, "//*[@id='signIn']/div/div/a")
    SIGNIN_WITH_EMAIL_BUTTON = (By.XPATH, "//*[@id='choices']/div/a[4]/button")
    EMAIL_INPUT_FIELD_LOCATOR = (By.ID, 'ap_email')
    PASSWORD_INPUT_FIELD_LOCATOR = (By.ID, 'ap_password')
    LOGIN_BUTTON_LOCATOR = (By.ID, 'signInSubmit')
    ERROR_MESSAGE_LOCATOR=(By.ID,'auth-warning-message-box')

    def __init__(self, driver):
        super().__init__(driver)


    @property
    def sign_in_button(self):
        return self.element(LoginPage.SIGNIN_REFERENCE)
    @property
    def sign_in_email_button(self):
        return self.element(LoginPage.SIGNIN_WITH_EMAIL_BUTTON)
    @property
    def email_input_field(self):
        return self.element(LoginPage.EMAIL_INPUT_FIELD_LOCATOR)

    @property
    def password_input_field(self):
        return self.element(LoginPage.PASSWORD_INPUT_FIELD_LOCATOR)

    @property
    def login_button(self):
        return self.element(LoginPage.LOGIN_BUTTON_LOCATOR)

    @property
    def error_message(self):
        return self.element(LoginPage.ERROR_MESSAGE_LOCATOR)

    def get_to_form(self):
        self.sign_in_button.click()
        self.sign_in_email_button.click()

    def navigate(self):
        self.driver.get(get_base_url())

    def enter_email(self, email):
        self.email_input_field.send_keys(email)
        return self

    def enter_password(self, password):
        self.password_input_field.send_keys(password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def fill_login_form(self, user):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_login_button()

    def successful_login(self, user):
        self.get_to_form()
        self.fill_login_form(user)
        return LandingPage(self.driver)

    def unsuccessful_login(self, user):
        self.get_to_form()
        self.fill_login_form(user)
        return self
