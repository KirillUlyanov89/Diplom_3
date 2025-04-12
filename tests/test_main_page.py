import src.data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
import allure

class TestMainPageFunctionality:
    @allure.title('Проверяем переход на Конструктор')
    def test_open_constructor_page_by_click_on_header_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        main_page = MainPage(driver)

        assert main_page.open_constructor_page()
        
    @allure.title('Проверяем переход на Ленту заказов')
    def test_open_order_history_by_click_on_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        feed_page = FeedPage(driver)
        
        assert feed_page.open_order_feed() == src.data.FEED_PAGE_URL
        
    @allure.title('Проверяем открытие поп-апа с деталями об ингредиенте')
    def test_open_ingredient_popup_by_click_on_item(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        assert main_page.open_ingredient_popup()
        
    @allure.title('Проверяем закрытие поп-апа с деталями об ингредиенте')
    def test_close_ingredient_popup_by_click_on_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_ingredient_popup()
        
        assert main_page.close_ingredient_popup()
        
    @allure.step('Проверяем работу счетчика ингредиента после добавления в состав')
    def test_check_ingredient_counter_increases_after_add_item_in_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.check_ingredient_counter_before()
        main_page.add_ingredients_in_burger()
        counter_after = main_page.check_ingredient_counter_after()
        
        assert counter_before == '0' and counter_after == '2'
        
    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_create_order__with_authorized_user(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.user_login(create_user)
        main_page = MainPage(driver)
        main_page.add_ingredients_in_burger()
        
        assert main_page.click_create_order_button()