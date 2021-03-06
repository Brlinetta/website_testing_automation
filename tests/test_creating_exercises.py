from pages.base_page import BasePage
from pages.my_exercises_page import Exercises
from pages.home_page import HomePage
import allure


@allure.feature('test_exercises1')
def test_create_exercises(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    exercises = Exercises(driver)
    id_exercises = exercises.create_exercises()
    name_exercises, category_exercises,  = exercises.open_exercises(id_exercises)
    assert name_exercises == 'exercise 1\nредактировать' and\
           category_exercises == 'Категория: Спина'


@allure.feature('test_exercises2')
def test_redact_exercises(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercises = Exercises(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    id_exercises = exercises.create_exercises()
    exercises.open_exercises(id_exercises)
    id_exercises_redact = exercises.redact_exercises()
    name_exercises, category_exercises = exercises.open_exercises(id_exercises_redact)
    assert name_exercises == 'exercise 1 redact\nредактировать' and\
           category_exercises == 'Категория: Шея'
