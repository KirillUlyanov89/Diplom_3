from selenium.webdriver.common.by import By

class FeedPageLocators:
    ORDER_FEED_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]'
    ORDER_FEED_HEADER = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_BLOCK = By.XPATH, '//a[contains(@class, "OrderHistory_link")]'
    ORDER_BLOCK_POPUP = By.XPATH, '//div[contains(@class, "Modal_orderBox")]'
    ORDER_NUMBER_TEXT = By.XPATH, '//p[contains(@class, "text_type_digits")]'
    ORDER_COUNTER_ALL_TIME = By.XPATH, '//p[contains(@class, "text_type_digits-large")]'
    ORDER_COUNTER_TODAY = By.XPATH, '//p[contains(@class, "text_type_main") and contains(text(), "Выполнено за сегодня")]/following-sibling::p[contains(@class, "text_type_digits-large")]'
    ORDER_NUMBER_BOX = By.XPATH, './/div[contains(@class, "OrderHistory_textBox")]/p[@class="text text_type_digits-default"]'
    ORDER_NUMBER_LIST = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text_type_digits-default")]'