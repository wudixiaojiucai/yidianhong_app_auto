from test_wexin.common.base import Base
from test_wexin.pages.about_address_list_page.address_list_page import AddressListPage
from test_wexin.pages.about_work_page.work_page import WorkPage


class MainPage(Base):
    # _address_list = ("-android uiautomator", 'new UiSelector().text("通讯录")')
    _address_list = 'new UiSelector().text("通讯录")'
    # _work = ("-android uiautomator", 'new UiSelector().text("工作台")')
    _work = 'new UiSelector().text("工作台")'

    def to_address_list_page(self):
        self.click(self._address_list)
        return AddressListPage(self.driver)

    def to_work_page(self):
        self.click(self._work)
        return WorkPage(self.driver)
