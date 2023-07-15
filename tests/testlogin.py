from helpers.resources import Resources

"""
    I navigate to the "Login" page
    When I click on "Sign In"
    And I click on "Sign in with email"
    And I fill in "email" with "<email>"
    And I fill in "password" with "<password>"
    And I click on the "Sign In" button
    Then I should be successfully logged in
    And I should land on the "Home" page
    And I should see "siteHeader__personal" menu
"""


def test_successfull_login(login_page, valid_user):
    landing_page=login_page.successful_login(valid_user)
    assert landing_page.is_page_displayed()

def test_locked_out_login(login_page, locked_out_user):
    login_page.unsuccessful_login(locked_out_user)
    assert login_page.login_button.is_displayed()

    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.ERROR_MESSAGE_FOR_LOCKED_OUT_USER

