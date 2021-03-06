from pages.base_page import BasePage
from pages.my_profile_page import My_profile_page
from pages.home_page import HomePage
import allure


@allure.feature('home_page')
def test_return_home_page(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.open_my_profile_page()
    page = my_profile_page.return_home_page_check()
    assert page == 'https://gymlog.ru/'
