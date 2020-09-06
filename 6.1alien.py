# 字典
"""
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_positon'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0['color'])
print(alien_0['points'])
"""

# 删除键-值对
'''
del alien_0['points']
'''

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: "+str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))
