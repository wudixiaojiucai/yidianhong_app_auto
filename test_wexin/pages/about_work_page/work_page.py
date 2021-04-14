from test_wexin.common.base import Base
from test_wexin.pages.about_work_page.daka_page.daka_index_page import DaKaIndexPage


class WorkPage(Base):

    def to_daka_index_page(self):
        self.scroll_text_and_click("打卡")
        return DaKaIndexPage(self.driver)
