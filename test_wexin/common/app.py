from appium import webdriver
from test_wexin.common.base import Base


class StartApp(Base):

    def start_app(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "6.0.1"
            desired_caps["deviceName"] = "127.0.0.1:7555"
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
            desired_caps["ensureWebviewsHavePages"] = True
            desired_caps["autoGrantPermissions"] = True  # 解决app的权限弹框
            desired_caps["skipDeviceInitialization"] = "true"  # 跳过设备初始化
            desired_caps["skipServerInstallation"] = "true"  # 跳过 uiautomator2 server的安装
            desired_caps["settings[waitForIdleTimeout]"] = 0  # 解决动态页面定位慢
            desired_caps["dontStopAppOnReset"] = "true"
            desired_caps["noReset"] = "true"
            desired_caps["unicodeKeyboard"] = "true"
            desired_caps["resetKeyboard"] = "true"
            # ignoreUnimportantViews: 这个参数设置为true的时候可以忽略不重要的view，加速pageSource的加载，加快测试速度
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(15)
        return self.driver
