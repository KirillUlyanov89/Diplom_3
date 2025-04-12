import src.data
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure

class FeedPage(BasePage):
    
    @allure.step('Открываем страницу Ленты заказов')
    def open_feed_page(self):
        self.open_url(src.data.FEED_PAGE_URL)
        self.wait_for_element(FeedPageLocators.ORDER_FEED_HEADER, 'visibility')
    
    @allure.step('Открываем Ленту заказа')
    def open_order_feed(self):
        self.click_on_element(FeedPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element(FeedPageLocators.ORDER_FEED_HEADER, 'visibility')
        return self.get_current_url()
    
    @allure.step('Тапаем на заказ')
    def click_on_order_block(self):
        self.click_on_element(FeedPageLocators.ORDER_BLOCK)
        self.wait_for_element(FeedPageLocators.ORDER_BLOCK_POPUP, 'visibility')
        return self.find_element(FeedPageLocators.ORDER_NUMBER_TEXT)
    
    @allure.step('Проверяем совпадение номера из Истории заказов с Лентой заказов')
    def check_number_order_in_feed_page(self, number):
        orders = self.find_all_elements(FeedPageLocators.ORDER_NUMBER_BOX)
        return any(number in order.text for order in orders)

    @allure.step('Проверяем появление номер заказа в разделе В работе на Ленте заказов')
    def check_number_order_in_at_work(self):
        self.wait_for_element(FeedPageLocators.ORDER_NUMBER_LIST, 'visibility')
        counter = self.find_element(FeedPageLocators.ORDER_NUMBER_LIST)
        return counter.text.lstrip('0')
    
    @allure.step('Проверяем счетчик Выполнено за все время')
    def get_counter_all_time_text(self):
        return self.find_element(FeedPageLocators.ORDER_COUNTER_ALL_TIME).text

    @allure.step('Проверяем счетчик Выполнено за сегодня')
    def get_counter_today_text(self):
        return self.find_element(FeedPageLocators.ORDER_COUNTER_TODAY).text