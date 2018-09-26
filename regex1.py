import re

# it=re.finditer(r'\d+','2008-2018 10年中国发生了翻天覆地的变化')
# for i in it:
#     print(i.group())
# try:
#     obj=re.fullmatch(r'\w+\W+','abcdef123#')
#     print(obj.group())
# except AttributeError as e:
#     print(e)

# obj =re.match(r'foo','foo,food on the table')
# print(obj.group())

obj=re.search(r'foo','Foo,food on thr table')
print(obj.group())