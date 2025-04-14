import src.data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    @allure.step('Переход на главную страницу')
    def open_main_page(self):
        self.open_url(src.data.BASE_PAGE_URL)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON, 'visibility')
        
    @allure.step('Переход на страницу Конструктора')
    def open_constructor_page(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.find_element(MainPageLocators.CONSTRUCTOR_HEADER)
    
    @allure.step('Переход на страницу логина')
    def open_login_page(self):
        self.open_url(src.data.BASE_PAGE_URL)
        self.click_on_element(MainPageLocators.ACCOUNT_PAGE_MENU_BUTTON)
        self.wait_for_element(MainPageLocators.LOGIN_PAGE_HEADER, 'visibility')
    
    @allure.step('Открыть Детали ингредиента')
    def open_ingredient_popup(self):
        self.click_on_element(MainPageLocators.BUN_INGREDIENT_TEXT)
        self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.find_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    
    @allure.step('Закрыть Детали ингредиента')
    def close_ingredient_popup(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BUTTON)
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT_TEXT, 'visibility')
        return self.find_element(MainPageLocators.CLOSE_POPUP_CLASS)
    
    @allure.step('Добавить ингредиент в бургер')
    def add_ingredients_in_burger(self):
        self.wait_for_element(MainPageLocators.BUN_COUNTER_CLASS, 'visibility')
        self.drag_drop(MainPageLocators.BUN_INGREDIENT_TEXT, MainPageLocators.CONSTRUCTOR_ADD_SECTION)
    
    @allure.step('Проверить счетчик ингредиента до добавления ингредиента')
    def check_ingredient_counter_before(self):
        self.wait_for_element(MainPageLocators.BUN_COUNTER_CLASS, 'visibility')
        return self.get_text(MainPageLocators.BUN_COUNTER_CLASS)
    
    @allure.step('Проверить счетчик ингредиента после добавления ингредиента')
    def check_ingredient_counter_after(self):
        self.wait_for_element(MainPageLocators.BUN_COUNTER_CLASS, 'visibility')
        return self.get_text(MainPageLocators.BUN_COUNTER_CLASS)
    
    @allure.step('Нажать на кнопку Оформить заказ')
    def click_create_order_button(self):
        self.wait_for_element(MainPageLocators.CREATE_ORDER_BUTTON, 'visibility')
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_for_element(MainPageLocators.CREATE_ORDER_POPUP_CLASS)
        return self.find_element(MainPageLocators.CREATE_ORDER_POPUP_HEADER)
    
    @allure.step('Процесс оформления заказа')
    def create_order_process(self):
        self.open_main_page()
        self.add_ingredients_in_burger()
        self.click_create_order_button()