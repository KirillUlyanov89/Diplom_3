from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOG_IN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//a[text()="Восстановить пароль"]'
    LOGIN_HEADER_TEXT = By.XPATH, '//h2[text()="Вход"]'
    EMAIL_INPUT_FORM = By.XPATH, '//label[text()="Email"]/../input'
    PASSWORD_INPUT_FORM = By.XPATH, '//label[text()="Пароль"]/../input'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'