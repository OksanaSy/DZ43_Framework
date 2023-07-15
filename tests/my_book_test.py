"""
Scenario Outline: Successful add and delete book to/from my books
	  When I click on "Search books" field on the "Home" page
	  And I fill in this field as "<bookname>"
	  And I click on the "bookname" link in quick search results
	  Then I should land on the "Book" page
	  And I should see "Bookname" in title"
"""

from helpers.resources import Resources


def test_succesful_add(login_page, valid_user, book_n):
    page = login_page.successful_login(valid_user)
    book_page = page.succesful_search(book_n)
    my_book_page = book_page.succesful_add()

    assert my_book_page.my_books_title_locator.is_displayed()
    assert my_book_page.new_book_locator.is_displayed()



