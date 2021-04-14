from test_wexin.common.base import Base
from test_wexin.pages.about_address_list_page.member_info_page import MemberInfoPage
from test_wexin.pages.about_address_list_page.select_add_member_page import SelectAddMemberPage


class AddressListPage(Base):
    # _add_member_btn = ("-android uiautomator", 'new UiSelector().text("添加成员")')
    _add_member_btn = 'new UiSelector().text("添加成员")'

    def to_select_add_member_page(self):
        self.scroll_text_and_click("添加成员")
        # self.swipe_click(self._add_member_btn)
        return SelectAddMemberPage(self.driver)

    def to_member_info_page(self, username):
        self.scroll_text_and_click(username)
        return MemberInfoPage(self.driver)
