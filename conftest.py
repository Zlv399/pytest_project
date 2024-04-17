import pytest

@pytest.fixture(scope='package')
def package():
    print('不同包之间执行一次')
    yield


# class fixture():
#
#     @pytest.fixture()
#     def login(self):
#         token = 'token'
#         return token
#
# class Fixture(fixture):
#
#     def test(self,login):


