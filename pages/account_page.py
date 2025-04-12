from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):
    @allure.step('Открываем страницу профиля')
    def open_account_page(self):
        self.wait_for_element(AccountPageLocators.ACCOUNT_PAGE_MENU_BUTTON, 'visibility')
        self.click_on_element(AccountPageLocators.ACCOUNT_PAGE_MENU_BUTTON)
        
    @allure.step('Открываем историю заказов')
    def open_orders_history(self):
        self.wait_for_element(AccountPageLocators.ORDER_HISTORY_MENU_BUTTON, 'visibility')
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_MENU_BUTTON)
        return self.get_current_url()
    
    @allure.step('Поиск номера заказа в истории заказов')
    def search_number_in_orders_history(self):
        self.wait_for_element(AccountPageLocators.ORDER_NUMBER_BOX, 'visibility')
        orders_history_number = self.get_text(AccountPageLocators.ORDER_NUMBER_TEXT)
        return orders_history_number.lstrip('#0')
    
    @allure.step('Выход из аккаунта')
    def account_log_out(self):
        self.wait_for_element(AccountPageLocators.LOG_OUT_BUTTON, 'visibility')
        self.click_on_element(AccountPageLocators.LOG_OUT_BUTTON)
        self.wait_for_element(AccountPageLocators.LOG_IN_BUTTON, 'visibility')
        return self.get_current_url()