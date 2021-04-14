from test_wexin.common.base import Base
from test_wexin.pages.about_address_list_page.input_add_member_page import InputAddMemberPage


class SelectAddMemberPage(Base):
    _hand_add_input = 'new UiSelector().text("手动输入添加")'

    def to_input_add_member_page(self):
        self.click(self._hand_add_input)
        return InputAddMemberPage(self.driver)
