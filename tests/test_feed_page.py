from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure

class TestFeedOrdersPage:

    @allure.title('Проверка перехода к деталям заказа по клику на заказ в Ленте заказов')
    def test_check_open_order_details_by_feed_button(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        
        assert feed_page.click_on_order_block()
        
    @allure.title('Проверка синхронизации раздела История заказов с Лента заказов')
    def test_check_sync_history_order_and_feed_orders(self, driver, login_user_and_create_order):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        number = login_page.user_login_with_order(login_user_and_create_order)
        account_page = AccountPage(driver)
        account_page.open_account_page()
        account_page.open_orders_history()
        number_in_history = account_page.search_number_in_orders_history()
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        number_in_feed = feed_page.check_number_order_in_feed_page(number)
        
        assert number == number_in_history and number_in_feed == True
        
    @allure.title('Проверка увеличения счетчика Выполнено за всё время после создания заказа')
    def test_check_rise_counter_all_time_after_made_order(self, driver, create_user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        counter_before = feed_page.get_counter_all_time_text()
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.user_login(create_user)
        main_page = MainPage(driver)
        main_page.create_order_process()
        feed_page.open_feed_page()
        counter_after = feed_page.get_counter_all_time_text()
        
        assert counter_before != counter_after
        
    @allure.title('Проверка увеличения счетчика Выполнено за сегодня после создания заказа')
    def test_check_rise_counter_today_after_made_order(self, driver, create_user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        counter_before = feed_page.get_counter_today_text()
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.user_login(create_user)
        main_page = MainPage(driver)
        main_page.create_order_process()
        feed_page.open_feed_page()
        counter_after = feed_page.get_counter_today_text()
        
        assert counter_before != counter_after
        
    @allure.title('Проверка наличия номера заказа в статусе В работе после его создания')
    def test_check_order_status_in_work_after_order_creation(self, driver, login_user_and_create_order):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        number = login_page.user_login_with_order(login_user_and_create_order)
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        number_in_at_work = feed_page.check_number_order_in_at_work()
        
        assert number == number_in_at_work        