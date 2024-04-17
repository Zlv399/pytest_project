import pytest
import allure


@pytest.fixture()
def autouse():
    print('设置autouse参数为True')

def test_08():
    print('这是测试用例08')

def test_09():
    print('这是测试用例09')

def test_10(driver):
    print('使用fixture的别名进行调用')


@pytest.fixture
def func():
    print("function")

@pytest.fixture(scope="class")
def cls():
    print("class")

@pytest.fixture(scope="module")
def mod():
    print("module")

@pytest.fixture(scope="package")
def pack():
    print("package")

@pytest.fixture(scope="session")
def sess():
    print("session")


def test_demo(func, cls, mod, pack, sess):
    print("测试用例")

@pytest.fixture
def order():
    return []
@pytest.fixture
def a(order):
    order.append("a")
@pytest.fixture
def b(a, order):
    order.append("b")
@pytest.fixture(autouse=True)
def c(b, order):
    order.append("c")
@pytest.fixture
def d(b, order):
    order.append("d")
@pytest.fixture
def e(d, order):
    order.append("e")
@pytest.fixture
def f(e, order):
    order.append("f")
@pytest.fixture
def g(f, c, order):
    order.append("g")
def test_order_and_g(g, order):
    print(order)
    assert order == ["a", "b", "c", "d", "e", "f", "g"]

def test11(logins):
    print('这是用例1,token值={}'.format(logins))
    assert logins == 'abc'

def test12(logins):
    print('这是用例2,token值={}'.format(logins))


@pytest.fixture(scope="session")
def open():
    # 会话前置操作setup
    print("===打开浏览器===")
    yield
    # 会话后置操作teardown
    print("===关闭浏览器===")


@pytest.fixture(scope='module')
def login_1(open):
    # 方法级别前置操作setup
    print("===登陆操作===")
    yield
    # 方法级别后置操作teardown
    print("===退出操作===")


def test_case1(login_1):
    print("===测试用例1===")


def test_case2(login_1):
    print("===测试用例2===")


@pytest.mark.parametrize("name", ["zhangsan", "lisi", "wangwu"])
def test_case1(name):
    print(name)


# 如果有多个参数，list包含tuple
@pytest.mark.parametrize(["name", "pwd"], [("zhangsan", "123456"), ("lishi", "85135506")])
def test_case2(name, pwd):
    print(name, pwd)


# 如果有多个参数，tuple包含list
@pytest.mark.parametrize(("name", "pwd"), (["zhangsan", "567890"], ["lisi", "123qwe"]))
def test_case3(name, pwd):
    print(name, pwd)


# 如果有多个参数，list包含list
@pytest.mark.parametrize("name, pwd", [["zhangsan", "123456"], ["lisi", "abc123"]])
def test_case4(name, pwd):
    print(name, pwd)


# 也可以将参数作为一个变量使用
data = [('zhangsan', '123456'), ('lisi', 'abc123'),pytest.param('wangwu','123bvc',)]

@pytest.mark.parametrize('name,pwd', data)
def test_case05(name, pwd):
    print(name, pwd)



#多个装饰器参数化
# my_data_1 = [1, 2, 3]
# my_data_2 = ["a", "b"]
#
# @pytest.mark.parametrize("a", my_data_1,ids=['q','w','e'])
# @pytest.mark.parametrize("b", my_data_2,ids=['m','n'])
# def test_parametrize_case(a, b):
#     print(f"测试数据为：{a}，{b}")

my_data = (
    {
        "user": "张三",
        "pwd": "123456"
    },
    {
        "user": "lisi",
        "pwd": "abc123"
    }
)
@pytest.mark.parametrize('dic', my_data)
def test_parametrize_case(dic):
    print(f'测试数据为\n{dic}')
    print(f'user:{dic["user"]}, pwd:{dic["pwd"]}')

#参数化标记
@pytest.mark.parametrize("str,expected", [
    ('a', 'a'),
    ('b', 'b'),
    pytest.param('c', 'd', marks=pytest.mark.xfail),  # 表示预期失败，
    pytest.param('e', 'e', marks=pytest.mark.xfail),#表示预期失败实际断言成功 结果为xpass
    pytest.param('f', 'f', marks=pytest.mark.skip)  # 表示无条件跳过用例
])
def test_mark(str, expected):
    assert str == expected

#indirect==True
@pytest.fixture(params=['a'])
def indir(request):
    print('这是{}'.format(request.param))
    return request.param


@pytest.mark.parametrize('indir',['zhangsan','lisi'],indirect=True)
def test_indir(indir):
    print(indir)


data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# ids = ['1','2','3']

ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]
@pytest.mark.parametrize('a, b, expect', data_1,ids=['别名1','别名2'])

class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect


