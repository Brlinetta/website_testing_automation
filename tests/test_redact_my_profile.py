from pages.base_page import BasePage
from time import sleep
from pages.my_profile_page import My_profile_page
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
import allure


surname = (By.ID, 'profile_last_name')
name_1 = (By.ID, 'profile_first_name')
patronymic = (By.ID, 'profile_patronymic')
address = (By.ID, 'profile_addressИндекс')
city = (By.ID, 'profile_city')
additional_information = (By.ID, 'profile_info')
contact_information = (By.ID, 'profile_contacts')
profile_birth_time = (By.ID, 'profile_birth_time')


@allure.feature('test_my_profile1')
def test_surname_redact(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(surname, 'Пахомов\n')
    my_profile_page.redact_save()
    sleep(5)
    surname_2 = my_profile_page.check_element(surname)
    assert surname_2 == 'Пахомов'


@allure.feature('test_my_profile2')
def test_surname_redact_invalid_data(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(surname, 'etyusdfghsdfghjdfghsssssss\n')
    notification_invalid_input = my_profile_page.check_invalid()
    assert notification_invalid_input == 'Значение «Фамилия» должно содержать максимум 20 символов.'


@allure.feature('test_my_profile3')
def test_name_redact(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(name_1, 'Никита\n')
    my_profile_page.redact_save()
    name = my_profile_page.check_element(name_1)
    assert name == 'Никита'


@allure.feature('test_my_profile4')
def test_name_redact_invalid_data(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(name_1, 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n')
    notification_invalid_input = my_profile_page.check_invalid()
    assert notification_invalid_input == 'Значение «Имя» должно содержать максимум 20 символов.'


@allure.feature('test_my_profile5')
def test_patronymic_redact(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(patronymic, 'Евгеньевич\n')
    my_profile_page.redact_save()
    data = my_profile_page.check_element(patronymic)
    assert data == 'Евгеньевич'


@allure.feature('test_my_profile6')
def test_patronymic_redact_invalid_data(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(patronymic, '1111111111111111111111111111111111111111\n')
    notification_invalid_input = my_profile_page.check_invalid()
    assert notification_invalid_input == 'Значение «Отчество» должно содержать максимум 20 символов.'


@allure.feature('test_my_profile7')
def test_address_redact (driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(address, 'улица 37\n')
    my_profile_page.redact_save()
    data = my_profile_page.check_element(address)
    assert data == 'улица 37'


@allure.feature('test_my_profile8')
def test_city_redact (driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(city, 'Минск\n')
    my_profile_page.redact_save()
    data = my_profile_page.check_element(city)
    assert data == 'Минск'


@allure.feature('test_my_profile9')
def test_date_birth(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(profile_birth_time, '19.08.2000\n')
    my_profile_page.redact_save()
    data = my_profile_page.check_element(profile_birth_time)
    assert data == '19.08.2000'


@allure.feature('test_my_profile10')
def test_additional_information(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(additional_information, 'я человек')
    my_profile_page.redact_save()
    data = my_profile_page.check_element(additional_information)
    assert data == 'я человек'


@allure.feature('test_my_profile11')
def test_contact_information(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    my_profile_page = My_profile_page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    my_profile_page.click_redact_profile_button()
    my_profile_page.redact_element(contact_information, '+375*******')
    my_profile_page.redact_save()
    data = my_profile_page.check_element(contact_information)
    assert data == '+375*******'
