import pytest

class Test01:

    def setup_class(self):
        print('这是Test01class的前置')

    def teardown_class(self):
        print('这是Test01class的后置')

    def setup_method(self):
        print('这是class01方法的前置')

    def teardown_method(self):
        print('这是class01方法的后置')

    def test_class01(self):
        print('这是class01的方法')
        assert 'class01' == 'class01'


class Test02:

    def setup_class(self):
        print('这是Test02class的前置')

    def teardown_class(self):
        print('这是Test02class的后置')

    def setup_method(self):
        print('这是class02方法的前置')

    def teardown_method(self):
        print('')

    def test_class02(self):
        print('这是class02的方法')
        assert 'class02' == 'class02'

if __name__ == '__main__':
    pytest.main(['-s'])