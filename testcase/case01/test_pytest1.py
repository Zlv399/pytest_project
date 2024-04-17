import pytest

# class Teststorm():
#
#     def setup_class(self):
#         print('这是类执行开始前的方法')
#
#     def teardown_class(self):
#         print('这是类执行结束后的方法')
#
#     def setup(self):
#         print('这是类方法的前置')
#
#     def teardown(self):
#         print('这是类方法的后置')
#     #
#     # def setup_method(self):
#     #     print('这是类方法执行前的方法')
#     #
#     # def teardown_method(self):
#     #     print('这是类方法执行结束后的方法')
#
#     def test_a(self):
#         print('这是函数A')
#         assert 'a' == 'a'
#
#     def test_b(self):
#         print('这是函数B')
#         assert 'b'== 'b'
#
# if __name__ =='__main__':
#     pytest.main(['-s','test_pytest1.py'])

# def setup_module():
#     print('这是整个文件执行开始前的方法')
# #
#
# def teardown_module():
#     print('这是整个文件执行结束后的方法')


def setup():
    print('这是函数执行前的方法')


def teardown():
    print('这是函数执行结束后的方法')

# def setup_function():
#     print('这是函数执行前的方法')
#
#
# def teardown_function():
#     print('这是函数执行结束后的方法')


def test_a():
    print('这是函数A')
    assert 'a' == 'a'


def test_b():
    print('这是函数B')
    assert 'b'=='b'

# def test_err():
#     #使用raises抛出TypeError异常，创建异常实例e
#     with pytest.raises(TypeError) as e:
#         pass
#
#     #通过type属性，断言异常的类型是否是预期的TypeError
#     assert e.type == TypeError
#     #通过value属性，断言异常提示语是否正确，value值必须转str类型
#     assert 'TypeError' in str(e.value)

if __name__ == '__main__':
    pytest.main()

