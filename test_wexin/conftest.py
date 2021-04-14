import pytest
from test_wexin.common.app import StartApp
from test_wexin.pages.main_page import MainPage


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['zh_CN']


@pytest.fixture(scope="session", name="page")
def get_driver():
    app = StartApp().start_app()
    page = MainPage(app)
    yield page
    app.quit()


@pytest.fixture()
def back_fixture(page):
    """操作完成后返回首页"""
    yield
    page.back()


def pytest_collection_modifyitems(items):
    """解决控制台unicode编码，改为中文"""
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
