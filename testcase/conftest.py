"""
conftest.py实现全局数据共享
文件名称不能修改，只能固定conftest.py
"""

import os
import pytest
import allure
from selenium import webdriver

@pytest.fixture(scope='module')
def login():
    print('登录')
    token = 'token'
    return token

@pytest.fixture(scope='session')
def session():
    print('多个py文件的用例执行前，调用一次')



data = [{'name' :'zhangsan'}]
@pytest.fixture(params=data)
def user(request):
    return request.param

my_dict = [{'name1' :'admin'} ,{'name2' :'test'}]
dicts_name = ['A' ,'B']
@pytest.fixture(params=my_dict ,ids=dicts_name)
def users(request):
    return request.param

@pytest.fixture(name='driver')
def web_driver():
    print('设置了fixture别名为driver')

@pytest.fixture(scope='module')
def logins():
    print('登录成功')
    token = 'abc'
    yield token
    print('用例执行完成')



"""
钩子函数，解决pytest.mark.parametrize中ids参数设置中文，控制台输出乱码的问题
"""
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")



# """
# 钩子函数，修改pytest-html测试报告的标题
# """
# def pytest_html_report_title(report):
#     report.title = "pytest 测试报告标题"

# def pytest_itemcollected(item):     # 把case中的三引号注释输出到输出中的用例列表
#     """
#     解决参数化执行用例时。用例ids参数设置中文执行报错，无法生成pytest-html报告的问题，
#     :param item:
#     :return:
#     """
#     item._nodeid = item._nodeid.encode("unicode_escape").decode("utf-8")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     获取每个用例状态的钩子函数
#     :param item: 测试用例
#     :param call: 测试步骤
#     :return:
#     """
#     # 获取钩子方法的调用结果
#     out_come = yield
#     rep = out_come.get_result()  # 从钩子方法的调用结果中获取测试报告
#     # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write((rep.nodeid + extra + "\n"))
#         # 添加allure报告截图
#         dirver = Driver.get_driver()
#         if hasattr(dirver, "get_screenshot_as_png"):
#             with allure.step('用例执行失败时，添加失败截图...'):
#                 logger.error("用例执行失败，捕获当前页面......")
#                 allure.attach(dirver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    hook pytest allure用例失败截图
    :param item:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    # 从钩子方法的调用结果中获取测试报告
    rep = outcome.get_result()
    # print(rep,'调试')
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加报告截图
        with allure.step('查看失败截图'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


driver = None
@pytest.fixture(scope='session')
def init_driver():
    global driver
    if driver == None:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture(scope='session')
def aaa():
    print('aaa')

@pytest.fixture(scope='class')
def bbb(aaa):
    print('bbb')