from test_wexin.common.base import Base
from test_wexin.pages.about_address_list_page.edit_member_page import EditMemberPage


class MemberInfoSetPage(Base):
    _edit_member_btn = 'new UiSelector().text("编辑成员")'

    def to_edit_member_page(self):
        self.click(self._edit_member_btn)
        return EditMemberPage(self.driver)
