from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProfilePage(BasePage):
    PROFILE_MENU = (By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[3]/ul/li[5]')
    PROFILE_REF = (By.XPATH, '/html/body/div[2]/div/header/div[2]/div/div[3]/ul/li[5]/div/div/div/ul/li[1]/span/a')
    PROFILE_EDIT_LINK = (By.CLASS_NAME, 'smallText')
    USER_MIDDLE_NAME_LOCATOR = (By.ID, 'user_middle_name')
    UPDATE_BUTTON = (By.XPATH, '//*[@id="userForm"]/p/input')
    MESSAGE_BOX = (By.ID, 'header_notice_container')

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def update_message(self):
        return self.element(ProfilePage.MESSAGE_BOX)

    @property
    def user_middle_name_locator(self):
        return self.element(ProfilePage.USER_MIDDLE_NAME_LOCATOR)

    @property
    def update_button(self):
        return self.element(ProfilePage.UPDATE_BUTTON)

    @property
    def profile_edit_link(self):
        return self.element(ProfilePage.PROFILE_EDIT_LINK)

    @property
    def profile_menu(self):
        return self.element(ProfilePage.PROFILE_MENU)

    @property
    def profile_ref(self):
        return self.element(ProfilePage.PROFILE_REF)

    def go_to_profile(self):
        self.profile_menu.click()
        self.profile_ref.click()

    def enable_edit_profile(self):
        self.profile_edit_link.click()

    def set_middle_name(self, m_name):
        self.user_middle_name_locator.clear()
        self.user_middle_name_locator.send_keys(m_name)

    def submit_update(self):
        self.update_button.click()

    def fill_form(self,account):
        self.enable_edit_profile()
        self.set_middle_name(account.middle_name)
        self.submit_update()

    def succesfull_profile_update(self, account):
        self.go_to_profile()
        self.fill_form(account)
        return self
