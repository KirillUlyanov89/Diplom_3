from selenium.webdriver.common.by import By

class AccountPageLocators:
    ACCOUNT_PAGE_MENU_BUTTON = By.XPATH, './/p[contains(@class, "AppHeader_header__linkText") and text()="Личный Кабинет"]'
    ORDER_HISTORY_MENU_BUTTON = By.XPATH, '//a[text()="История заказов"]'
    ORDER_NUMBER_BOX = By.XPATH, './/div[contains(@class, "OrderHistory_textBox")]/p[@class="text text_type_digits-default"]'
    ORDER_NUMBER_TEXT = By.XPATH, '//p[contains(@class, "text_type_digits")]'
    LOG_OUT_BUTTON = By.XPATH, '//button[text()="Выход"]'
    LOG_IN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    