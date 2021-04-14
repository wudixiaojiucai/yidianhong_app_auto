from test_wexin.common.base import Base

from test_wexin.pages.about_address_list_page.member_info_set_page import MemberInfoSetPage


class MemberInfoPage(Base):
    _right_top_btn = "//*[@text='个人信息']/../../../../following-sibling::android.widget.LinearLayout"

    def to_member_info_set_page(self):
        self.click(self._right_top_btn)
        return MemberInfoSetPage(self.driver)
