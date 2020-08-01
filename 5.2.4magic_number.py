# 数字比较
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 使用and检查多个条件
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_1 = 22
age_0 >= 21 and age_1 >= 21

# 使用or检查多个条件
age_0 = 22
age_1 = 18
age_0 >= 22 or age_1 >= 21
age_0 = 18
age_0 >= 21 or age_1 >= 21

# 使用in检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings
