import src.data
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure

class TestAccountPage:
    @allure.title('Проверка перехода к Личному кабинету')
    def test_open_account_page_by_button_click_on_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_login_page()
        
        assert main_page.get_current_url() == src.data.LOGIN_PAGE_URL
        
    @allure.title('Проверка перехода к разделу История заказов')
    def test_open_orders_history_by_button_click_on_account_page(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.open_login_page()
        login_page = LoginPage(driver)
        login_page.user_login(create_user)
        account_page = AccountPage(driver)
        account_page.open_account_page()
        
        assert account_page.open_orders_history() == src.data.ORDER_HISTORY_PAGE_URL
        
    @allure.title('Проверка на выход из аккаунта')
    def test_check_user_log_out_by_button_click_on_account_page(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.open_login_page()
        login_page = LoginPage(driver)
        login_page.user_login(create_user)
        account_page = AccountPage(driver)
        account_page.open_account_page()
        
        assert account_page.account_log_out() == src.data.LOGIN_PAGE_URL
        