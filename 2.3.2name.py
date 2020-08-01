# title(),upper(),lower()
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name+' '+last_name
message = "hello,"+full_name.title()+"!"
print(message)

# 制表符和换行符
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

# rstrip()删除末尾空白
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print('h'+favorite_language+'t')
# lstrip()删除开头空白
favorite_language = ' python '
favorite_language = favorite_language.lstrip()
print('h'+favorite_language+'t')
# strip()删除两端空白
favorite_language = ' python '
favorite_language = favorite_language.strip()
print('h'+favorite_language+'t')
