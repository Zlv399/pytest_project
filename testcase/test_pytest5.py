import  pytest
"""
fixture scope=function时的作用域
"""
# @pytest.fixture(scope='function')
# def login():
#     print('登录')
#     token = 'token'
#     return token
#
# def test_01(login):
#     print('测试方法01')
#     assert login == 'token'

"""
fixture scope=class时的作用域
"""


#
class Testcase():

    def test_01(self,login):
        print('这是测试方法01')
        assert login == 'token'

    def test_02(self,login):
        print('这是测试方法02')
        assert login == 'token'





def test_04(session):
    print('这是测试用例04')
