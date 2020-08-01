# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
# 直接复制列表，这行不通
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite food are:")
print(my_foods)
print("\nMy friends' favorite foods are:")
print(friend_foods)