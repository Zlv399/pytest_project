import pytest



# class Test04():
#
#     def test_c(self):
#         print('ccc')
#         assert 'c' == 'c'
#
#     # @pytest.mark.flaky(reruns=2,reruns_delay=3)
#     # @pytest.mark.repeat(2)
#     def test_d(self):
#         print('断言失败')
#         assert 'd' == 'D'

# if __name__ == '__main__':
#     pytest.main(['-s'])


# @pytest.mark.run(order=2)
# def test_a():
#     print('aaa')
#     assert 'a' == 'a'
#
#
# @pytest.mark.run(order=1)
# def test_b():
#     print('bbb')
#     assert 'b' == 'b'
#
#
# @pytest.mark.run(order=1)
# def test_c():
#     print('ccc')
#     assert 'c' == 'c'


# @pytest.mark.repeat(2)
# def test_a():
#     print('aaa')
#     assert 'a' == 'a'


# @pytest.mark.repeat(2)
# def test_b():
#     print('bbb')
#     assert 'b' == 'b'
#
#
# @pytest.mark.repeat(2)
# def test_c():
#     print('ccc')
#     assert 'c' == 'c'
#
#
# class Test03():
#
#     @pytest.mark.L1
#     # @pytest.mark.L2
#     def test_a(self):
#         print('aaa')
#         assert 'a' == 'a'
#
# #     # @pytest.mark.flaky(reruns=2,reruns_delay=2)
#     @pytest.mark.L2
#     @pytest.mark.L3
#     def test_b(self):
#         print('bbb')
#         assert 'b' == 'b'

# @pytest.mark.flaky(reruns=2,reruns_delay=2)
# def test_b():
#     print('bbb')
#     assert 'b' == 'c'
#
#
# def test_a():
#     print('aaa')
#     assert 'a' == 'a

# @pytest.mark.L3
# def test_c():
#     print('cccc')
#     assert 'c' == 'c'

@pytest.mark.skip(reason="函数级用例，不执行该用例！！因为没写好！！")
def test_case02():
    print("我是测试用例22222")

class Test1:

    def test_1(self):
        print("%% 我是类测试用例1111 %%")

    @pytest.mark.skip(reason="我是测试类下用例，不想执行")
    def test_2(self):
        print("%% 我是类测试用例2222 %%")

@pytest.mark.skip(reason="整个类下所有用例，可以全部跳过不执行")
class TestSkip:
    def test_1(self):
        print("不会执行")

# @pytest.mark.skipif('a'== 'b', reason="a == a 的时候才会跳过")
# class TestSkipIf(object):
#     def test_function(self):
#         print("condition为True才会跳过")

# skipmark = pytest.mark.skip(reason="不能运行====")
# skipifmark = pytest.mark.skipif('a' == 'a', reason="不能运行啦啦啦=====")
#
# # @pytest.mark.L1
# class TestSkip_Mark(object):
#     @skipifmark
#     def test_function(self,session):
#         print("测试用例function")
#
#     def test_def(self,session):
#         print("测试用例def")
#
# @skipmark
# def test_skip():
#     print("测试用例skip")
