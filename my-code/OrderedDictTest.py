from collections import OrderedDict

# 创建一个有序字典并插入键值对
ordered_dict = OrderedDict()
ordered_dict['banana'] = 3
ordered_dict['apple'] = 5
ordered_dict['orange'] = 2

# 打印有序字典
for key, value in ordered_dict.items():
    print(f'{key}: {value}')
