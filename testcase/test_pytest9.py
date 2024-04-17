import  pytest
import allure
from selenium import webdriver
import  time

@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-注册测试')
class Test_epic_feature_story:

      @allure.title('用例标题1')
      def test_epic_feature_story_01(self):
          pass

      @allure.title('用例标题2')
      def test_epic_feature_story_02(self):
          pass

      @allure.title('用例标题3')
      def test_epic_feature_story_03(self):
          pass


# @allure.epic('商城项目')
# @allure.feature('登录模块')
# @allure.story('用户故事-登录测试')
# @allure.title('用例标题4')
# def test_epic_feature_story_04():
#     pass


login_data = [
   ("登录成功用例", "zhangsan", "password", "success"),
   ("密码错误用例", "zhangsan", "passwd", "failed_password"),
   ("用户不存在用例", "lisi", "password", "user_not_exists")
]

@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@pytest.mark.parametrize("case_title,username,password,expect_result", login_data)
def test_login(case_title, username, password, expect_result):
    print("登录测试")
    allure.dynamic.title(case_title)
    allure.dynamic.description(f"测试用例描述：此条用例期待结果：{expect_result}")


@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@allure.severity(allure.severity_level.BLOCKER)
class Test_severity_01:

      def test_severity_01(self):
          pass

      def test_severity_02(self):
          pass

@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
class Test_severity_02:

      @allure.severity(allure.severity_level.BLOCKER)
      def test_severity_03(self):
          pass

      def test_severity_04(self):
          pass


@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@allure.severity(allure.severity_level.BLOCKER)
def test_severity_05():
    pass


@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@allure.description('这是用例描述')
class Test_description_01:

      def test_description_01(self):
          pass

      def test_description_02(self):
          pass

@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
class Test_description_02:

      @allure.description('这是用例描述')
      def test_description_03(self):
          pass

      def test_description_04(self):
          pass


@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@allure.description('这是用例描述')
def test_description_05():
    pass


@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@allure.link(url='https://www.baidu.com',name='自定义链接')
@allure.issue(url='https://www.baidu.com',name='bug管理链接')
@allure.testcase(url='https://www.baidu.com',name='测试用链接')
class Test_link_testcase_issue_01:

      def test_link_testcase_issue_01(self):
          pass

      def test_link_testcase_issue_02(self):
          pass

@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
class Test_description_02:

      @allure.link(url='https://www.baidu.com', name='自定义链接')
      @allure.issue(url='https://www.baidu.com', name='bug管理链接')
      @allure.testcase(url='https://www.baidu.com', name='测试用链接')
      def test_link_testcase_issue_03(self):
          pass

      def test_link_testcase_issue_04(self):
          pass


@allure.epic('商城项目')
@allure.feature('登录模块')
@allure.story('用户故事-登录测试')
@allure.link(url='https://www.baidu.com',name='自定义链接')
@allure.issue(url='https://www.baidu.com',name='bug管理链接')
@allure.testcase(url='https://www.baidu.com',name='测试用链接')
def test_link_testcase_issue_05():
    pass


login_data_link = [
    ("登录成功用例", "zhangsan", "password", "success","https://www.baidu.com"),
    ("密码错误用例", "zhangsan", "passwd", "failed_password", "https://www.bilibili.com/"),
    ("用户不存在", "lisi", "password", "user_not_exists", "https://www.qq.com/")
]


@allure.link(url="https://passport.jd.com/new/login.aspx", name="登录地址")
@allure.issue(url="https://www.google.com", name="bug列表地址1")
@allure.testcase(url="https://testlink.org/", name="测试用例地址1")
@pytest.mark.parametrize("case_title,username,password,expect_result,test_url", login_data_link)
def test_login_link(case_title, username, password, expect_result, test_url):
    print("登录测试")
    allure.dynamic.link(url=test_url, name="登录链接")
    allure.dynamic.issue(url=test_url, name="bug列表地址2")
    allure.dynamic.testcase(url=test_url, name="测试用例地址2")


@allure.epic("商城项目")
@allure.feature("购物车模块")
@allure.story("测试添加购物车方法")
class TestCart:
    @allure.step("第一步，测试加入购物车")
    def test_add_cart01(self):
        # 第一步，登录
        with allure.step("第一步，登录"):
            print("登录成功")
        # 第二步，搜索商品
        with allure.step("第二步,搜索商品"):
            print("搜索成功")
        # 第三步，将商品加入购物车
        with allure.step("第三步，加入购物车"):
            print("加入购物车成功")
        # 第四步，打开购物车
        with allure.step("第四步，打开购物车"):
            print("打开购物车成功")
        # 第五步，断言验证是否添加成功
        with allure.step("第五步，断言验证是否加入成功"):
            print("验证加入购物车通过")

    def test_add_cart02(self):
        # 第一步，登录
        with allure.step("第一步，登录"):
            print("登录成功")
        # 第二步，搜索商品
        with allure.step("第二步,搜索商品"):
            print("搜索成功")
        # 第三步，将商品加入购物车
        with allure.step("第三步，加入购物车"):
            print("加入购物车成功")
        # 第四步，打开购物车
        with allure.step("第四步，打开购物车"):
            print("打开购物车成功")
        # 第五步，断言验证是否添加成功
        with allure.step("第五步，断言验证是否加入成功"):
            print("验证加入购物车通过")

@allure.epic("商城项目")
@allure.feature("购物车模块")
@allure.story("测试添加购物车方法")
@allure.step("第一步，测试加入购物车")
def test_add_cart03():
        # 第一步，登录
    with allure.step("第一步，登录"):
         print("登录成功")
        # 第二步，搜索商品
    with allure.step("第二步,搜索商品"):
         print("搜索成功")
        # 第三步，将商品加入购物车
    with allure.step("第三步，加入购物车"):
         print("加入购物车成功")
        # 第四步，打开购物车
    with allure.step("第四步，打开购物车"):
         print("打开购物车成功")
        # 第五步，断言验证是否添加成功
    with allure.step("第五步，断言验证是否加入成功"):
         print("验证加入购物车通过")


@allure.step("第一步，打开百度")
def test_attach():

    with open("./attachment_file_type/png01/baidu.png","rb") as f:
        allure.attach(body=f.read(),name="打开百度",attachment_type=allure.attachment_type.PNG)

@allure.step("第一步，打开百度")
def test_attach_file():
    allure.attach.file(source="./attachment_file_type/png01/baidu.png",name="打开百度",
                       attachment_type=allure.attachment_type.PNG)


@allure.step("第一步，打开百度")
def test_attach_csv():

    with open("./attachment_file_type/csv01/工作薄6.csv","rb") as f:
        allure.attach(body=f.read(),name="打开百度",attachment_type=allure.attachment_type.CSV)

@allure.step("第一步，打开百度")
def test_attach_file_pdf():
    allure.attach.file(source="./attachment_file_type/pdf01/Python编程从入门到实践.pdf",name="打开百度",
                       attachment_type=allure.attachment_type.PDF)



