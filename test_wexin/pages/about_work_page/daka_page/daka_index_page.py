from test_wexin.common.base import Base
from test_wexin.pages.about_work_page.daka_page.out_daka_page import OutDaKaPage


class DaKaIndexPage(Base):
    _out_daka = ("-android uiautomator", 'new UiSelector().text("外出打卡")')

    def to_out_daka_page(self):
        self.click(self._out_daka)
        return OutDaKaPage(self.driver)
