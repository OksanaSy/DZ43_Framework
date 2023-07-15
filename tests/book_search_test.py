"""
Scenario Outline: Successful find the book
	  When I click on "Search books" field on the "Home" page
	  And I fill in this field as "<bookname>"
	  And I click on the "bookname" link in quick search results
	  Then I should land on the "Book" page
	  And I should see "Bookname" in title"
"""

from helpers.resources import Resources


def test_succesful_search(login_page, valid_user, book_n):
    page = login_page.successful_login(valid_user)
    book_page = page.succesful_search(book_n)

    assert book_page.found_book_title.is_displayed()
    assert book_page.found_book_title.get_attribute('aria-label') == 'Book title: ' + Resources.BookPage.BOOK_TITLE
