"""
Scenario Outline: Successful Edit Profile
        After login
	  When I click on "My Profile" link on the "Home" page
	  And I fill in Middle Name as "<middlename>"
	  And I click on the "Update Profile" button
	  Then I should land on the "Profile" page
	  And I should see "success" message"
"""
from helpers.resources import Resources


def test_successfull_profile_update(login_page,valid_user, valid_account):
    page=login_page.successful_login(valid_user)
    profile_page=page.to_profile_page()
    profile_page.succesfull_profile_update(valid_account)

    assert profile_page.user_middle_name_locator.get_attribute('value') == valid_account.middle_name
    assert profile_page.update_message.is_displayed()
    assert profile_page.update_message.text == Resources.ProfilePage.UPDATE_MESSAGE

