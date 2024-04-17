import  pytest
import allure
from selenium import webdriver
import  time
import os


def test_baidu_login():
    url = 'https://www.baidu.com'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    try:
        driver.find_element('id','xsdsd')

    except Exception as e:
        img = driver.get_screenshot_as_png()
        allure.attach(img,'失败截图',allure.attachment_type.PNG)


def test_baidu_fail(init_driver):
    url = 'https://www.baidu.com'
    init_driver.get(url)
    init_driver.maximize_window()
    assert '1' == '1'

# def test_os():
#
#     print(os.getcwd())
#     print(os.path.dirname(r'D:\pytest_project\testcase\test_pytest10.py'))


def setup_module():
    print('这是整个文件执行开始前的方法')


def teardown_module():
    print('这是整个文件执行结束后的方法')

class Teststorm():

    def setup_class(self):
        print('这是类执行开始前的方法')

    def teardown_class(self):
        print('这是类执行结束后的方法')

    def setup_method(self):
        print('这是类方法执行前的方法')

    def teardown_method(self):
        print('这是类方法执行结束后的方法')

    def test_a(self):
        print('这是函数A')
        assert 'a' == 'a'

    def test_b(self):
        print('这是函数B')
        assert 'b'== 'b'