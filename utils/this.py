# @project:pytest_project
# @File:this.py9
# @IDE:PyCharm
# @Author:fangyixiong
# @Date:2023/7/19 23:06

import os

import pytest
import yaml
import json

# def read():
#     lists = []
#     with open(r'./attachment_file_type/txt01/test03.txt', 'r', encoding='utf-8') as f:
#         file_object = f.readlines()
#         for i in file_object:
#             lists.append(i[:-1])
#     return lists

#     # print(lists)
#     # data = f.read().splitlines()
#     # print(data)
#     data = f.readlines()
#     print(data)
#     lists = []
#     for ip in data:
#         if ip != None:
#         #从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
#             lists.append(ip.strip("\n"))
#     print(lists)


# with open(r'../attachment_file_type/txt01/test02.txt', 'a',encoding='utf8') as f:
#     f.write('5.这是第五行数据\n')
#     f.write('6.这是第六行数据\n')
#
# lists = ['7.这是第七行数据\n','8.这是第8行数据','9.这是第9行数据\n']
# with open(r'../attachment_file_type/txt01/test02.txt', 'a',encoding='utf8') as f:
#     f.writelines(lists)


# with open(r'../attachment_file_type/txt01/test02.txt', 'a', encoding='utf8') as f:
#     print('10.这是第十行数据',file=f)
#     print('11.这是第十一行数据',file=f)

# with open(r'../attachment_file_type/pyyaml01/ymal.yaml') as y:
#     yaml_read = yaml.safe_load(y)
#     print(yaml_read)
#     users = yaml_read.get('user')
#     print(users)
#     print(users[0].get('username'))

# with open(r'../attachment_file_type/pyyaml01/ymal.yaml') as y:
#     yaml_read = yaml.safe_load(y)
#     print(yaml_read)
#     print(yaml_read.get('school'))
#     for i in yaml_read.get('school'):
#         print(i.get('schoolname'))

# config = {
#     'database': {
#         'host': 'localhost',
#         'port': 3306,
#         'username': 'root',
#         'password': 'password'
#     }
# }
#
# string_config = {key: str(value) for key, value in config.items()}
# with open(r'../attachment_file_type/pyyaml01/ymal.yaml', 'a',encoding='utf8') as f:
#     yaml.dump(config, f)

# with open(r'../attachment_file_type/json01/test_json.json',encoding='utf8') as j:
#     data = json.load(j)
#     print("读取json文件数据为:\n{}\n数据类型为: {}".format(data, type(data)))

# dic = {
#     "student":
#         [
#             {
#                 "name": "zhangsan",
#                 "age": "22"
#             }
#         ]
# }
# with open(r'../attachment_file_type/json01/test_json02.json', 'w', encoding='utf-8') as f:
#     json.dump(dic,f)



