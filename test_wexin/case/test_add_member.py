import pytest


class TestAddMember:

    @pytest.mark.parametrize("username,sex,phone", [("回马一电", "女", 11199998888)])
    def test_add_member(self, page, back_fixture, username, sex, phone):
        """正常添加成员"""
        res = page.to_address_list_page().to_select_add_member_page().to_input_add_member_page() \
            .add_success_toast(username, sex, phone)

        assert res == "添加成功"

    # --------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize("username,sex,phone", [("回马一电", "女", 11199998888)])
    def test_add_double(self, page, back_fixture, username, sex, phone):
        """重复添加"""
        res = page.to_address_list_page().to_select_add_member_page().to_input_add_member_page() \
            .add_double_fail_res(username, sex, phone)

        assert res == "手机已存在于通讯录，无法添加"

        """添加完成后删除，调试用"""
        page.back()
        page.to_address_list_page().to_member_info_page(
            username).to_member_info_set_page().to_edit_member_page().del_member(username)
