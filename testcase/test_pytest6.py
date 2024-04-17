import pytest

def test_03(login):
    print('这是测试方法03')

def test_05(session):
    print('这是测试用例05')

def test_06(package):
    print('这是测试用例06')


def test_08(user):
    print('注册用户：{}'.format(user))

def test_09(users):
    print('当前用户是：{}'.format(users))

