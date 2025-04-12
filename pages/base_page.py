from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        
    def get_current_url(self):
        return self.driver.current_url
    
    def get_text(self, locator):
        return self.find_element(locator).text    

    def wait_for_element(self, locator, condition_type='presence'):
        conditions = {
            'visibility': EC.visibility_of_element_located,
            'presence': EC.presence_of_element_located,
            'presence_of_all': EC.presence_of_all_elements_located,
            'clickable': EC.element_to_be_clickable
        }
        condition = conditions.get(condition_type, EC.presence_of_element_located)
        WebDriverWait(self.driver, 20).until(condition(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_all_elements(self, locator):
        self.wait_for_element(locator, 'presence_of_all')
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        self.wait_for_element(locator, 'clickable')
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator, 'visibility')
        self.find_element(locator).send_keys(text)

    def drag_drop(self, locator_from, locator_to):
        ActionChains(self.driver).drag_and_drop(
            self.find_element(locator_from),
            self.find_element(locator_to)
        ).perform()