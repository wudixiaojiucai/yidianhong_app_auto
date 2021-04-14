from test_wexin.common.base import Base


class OutDaKaPage(Base):
    _out_daka_count = ("-android uiautomator", 'new UiSelector().textContains("次外出")')
    _out_daka_success_res = ("-android uiautomator", 'new UiSelector().textContains("打卡成功")')

    def out_daka_success(self):
        self.click(self._out_daka_count)
        return self.get_text(self._out_daka_success_res)
