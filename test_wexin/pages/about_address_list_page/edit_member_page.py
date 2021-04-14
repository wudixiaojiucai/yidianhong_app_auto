from test_wexin.common.base import Base
from appium.webdriver.common.mobileby import MobileBy as By


class EditMemberPage(Base):
    # _del_member_btn = ("-android uiautomator", 'new UiSelector().text("删除成员")')
    _del_member_btn = 'new UiSelector().text("删除成员")'
    # _sure_btn = ("xpath", "//*[@resource-id='com.tencent.wework:id/bom' and @text='确定']")
    _sure_btn = "//*[@resource-id='com.tencent.wework:id/bom' and @text='确定']"

    def del_member(self, username):
        self.click(self._del_member_btn)
        self.click(self._sure_btn)
        return self.is_presence((By.XPATH, f"//*[@text='{username}']"))
