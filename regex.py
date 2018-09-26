import re

# pattern = r'(ab)cd(ef)'
# s = 'abcdefghijklmn'

# # re模块直接调用
# l = re.findall(pattern, s)
# print(l)

# # compile对象调用
# regex=re.compile(pattern)
# l=regex.findall(s,0)
# print(l)


# l = re.split(r'\s+','Hello    world nihao China')
# print(l)

s = re.subn(r'\s+','##','hello world nihao china',2)
print(s)