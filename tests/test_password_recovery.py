from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
import allure
import src.data

class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля через кнопку Восстановить пароль')
    def test_open_password_recovery_page_by_button_click(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_password_recovery_button()
        
        assert login_page.get_current_url() == src.data.PASSWORD_RECOVERY_PAGE_URL
        
    @allure.title('Проверка ввода почты и работы кнопки Восстановить')
    def test_email_input_form_and_password_recovery_button_by_input_and_click(self, create_user, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_password_recovery_page()
        password_recovery_page.fill_email_input_form(create_user)
        password_recovery_page.click_password_recovery_button()
        
        assert password_recovery_page.get_current_url() == src.data.PASSWORD_RESET_PAGE_URL
        
    @allure.title('Проверка скрытия/показа текста в поле Пароль')
    def test_password_show_button_and_active_state_by_click_on_hide_password_button(self, driver, create_user):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_password_reset_page(create_user)
        
        assert recovery_page.click_hide_password_icon()