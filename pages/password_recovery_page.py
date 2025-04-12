import src.data
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
import allure

class PasswordRecoveryPage(BasePage):
    @allure.step('Открываем страницу восстановления пароля')
    def open_password_recovery_page(self):
        self.open_url(src.data.PASSWORD_RECOVERY_PAGE_URL)
        self.wait_for_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_HEADER_TEXT, 'visibility')
        
    @allure.step('Заполнение формы на странице восстановления пароля')
    def fill_email_input_form(self, create_user):
        email, _, _ = create_user
        self.send_keys(PasswordRecoveryPageLocators.EMAIL_INPUT_FORM, email)
        
    @allure.step('Кликнуть на кнопку Восстановить')
    def click_password_recovery_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.wait_for_element(PasswordRecoveryPageLocators.SAVE_BUTTON)
        
    @allure.step('Ввод пароля в форму на странице восстановления пароля')
    def fill_password_reset_input_form(self, create_user):
        _, password, _ = create_user
        self.send_keys(PasswordRecoveryPageLocators.PASSWORD_RESET_INPUT_FORM, password)
        
    @allure.step('Клик на иконку скрытия пароля (глаз)')
    def click_hide_password_icon(self):
        self.click_on_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_EYE_BUTTON)
        return self.find_element(PasswordRecoveryPageLocators.PASSWORD_REST_INPUT_FORM_ACTIVE)
    
    @allure.step('Открываем страницу сброса пароля')
    def open_password_reset_page(self, create_user):
        self.open_password_recovery_page()
        self.fill_email_input_form(create_user)
        self.click_password_recovery_button()
        self.fill_password_reset_input_form(create_user)
        