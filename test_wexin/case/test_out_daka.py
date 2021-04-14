import pytest


class TestDaka:

    def test_out_daka(self, page, back_fixture):
        """外出打卡"""
        res = page.to_work_page().to_daka_index_page().to_out_daka_page().out_daka_success()

        assert res == "外出打卡成功"
