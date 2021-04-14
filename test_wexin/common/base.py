import time
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from func_timeout import func_set_timeout
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ElementNotFound(Exception):
    pass


class Base:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        if "new UiSelector()" in locator:
            by = "-android uiautomator"
        elif "id:" in locator:
            by = "id"
        else:
            by = "xpath"
        print(f"当前定位元素：{by}, {locator}")
        return self.driver.find_element(by, locator)

    def finds(self, locator):
        if "new UiSelector" in locator:
            by = "-android uiautomator"
        elif "id" in locator:
            by = "id"
        else:
            by = "xpath"
        return self.driver.find_elements(by, locator)

    def click(self, locator):
        self.find(locator).click()

    def send(self, locator, text):
        self.find(locator).send_keys(text)

    def scroll_text(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')

    def scroll_text_and_click(self, text):
        ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().'
                                       'scrollable(true).instance(0)).'
                                       'scrollIntoView(new UiSelector().'
                                       f'text("{text}").instance(0));')
        time.sleep(0.5)
        ele.click()

    @func_set_timeout(60)
    def swipe_find(self, locator):
        eles = self.finds(locator)
        while len(eles) == 0:
            self.driver.swipe(200, 600, 200, 300)
            eles = self.finds(locator)
        return eles[0]

    def swipe_click(self, locator):
        self.swipe_find(locator).click()

    def get_toast(self):
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((MobileBy.XPATH, "//*[@class='android.widget.Toast']")))
        res = ele.text
        return res

    def is_presence(self, locator):
        try:
            WebDriverWait(self.driver, 10).until_not(
                expected_conditions.presence_of_element_located((locator[0], locator[1])))
            return True
        except:
            return False

    def get_text(self, locator):
        ele = self.find(locator)
        return ele.text

    def back(self):
        self.driver.start_activity(app_package="com.tencent.wework", app_activity="launch.WwMainActivity")
