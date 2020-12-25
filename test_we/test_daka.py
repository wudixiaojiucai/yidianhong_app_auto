from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:

    def test_out_daka(self, driver):
        """外出打卡"""
        driver.find_element(By.XPATH, "//*[@text='工作台' and @class='android.widget.TextView']").click()
        # # 滚动查找元素
        driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                    'scrollable(true).instance(0)).'
                                                    'scrollIntoView(new UiSelector().'
                                                    'text("打卡").instance(0));').click()
        # 点击外出打开
        driver.find_element(By.XPATH, "//*[@text='外出打卡']").click()
        driver.find_element(By.XPATH, "//*[contains(@text,'次外出')]").click()
        # 等待获取页面内容
        WebDriverWait(driver, timeout=10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in driver.page_source
