from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    PASSWORD_RECOVERY_HEADER_TEXT = By.XPATH, '//h2[text()="Восстановление пароля"]'
    EMAIL_INPUT_FORM = By.XPATH, '//label[text()="Email"]/../input'
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    PASSWORD_RESET_INPUT_FORM = By.XPATH, "//input[@type='password']"
    PASSWORD_REST_INPUT_FORM_ACTIVE = By.XPATH, "//div[contains(@class, 'input_status_active')]"
    SHOW_PASSWORD_EYE_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]"
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'