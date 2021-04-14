from test_wexin.common.base import Base


class InputAddMemberPage(Base):
    _username = "//*[contains(@text, '姓名')]/..//*[@text='必填']"
    _sex = "//*[contains(@text, '性别')]/..//*[@text='男']"
    _wait_sex = "//*[@text='女']"
    _phone = "//*[contains(@text,'手机')]/..//*[@text='手机号']"
    _save_btn = 'new UiSelector().text("保存")'
    _double_fail_text = 'new UiSelector().textContains("无法添加")'

    def add_member(self, username, sex, phone):
        self.send(self._username, username)
        self.click(self._sex)
        self.find(self._wait_sex)
        self.click(f'new UiSelector().text("{sex}")')
        self.send(self._phone, phone)
        self.click(self._save_btn)

    def add_success_toast(self, username, sex, phone):
        self.add_member(username, sex, phone)
        return self.get_toast()

    def add_double_fail_res(self, username, sex, phone):
        self.add_member(username, sex, phone)
        return self.get_text(self._double_fail_text)
