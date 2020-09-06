# 复杂数据
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
'''

# 输出单项
'''
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      '.')
'''

# 输出全部
"""for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is " +
          language.title()+".")
"""

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())
