"""
@Author    : sidekick-boy
@Email     : sidekick_boy@outlook.com
"""

"""
1、 container 容器
2、 list 列表 ： 类型不限；有前后顺序；可重复
3、 增删改查
4、 切片：[起：止（不含）: 步长]
"""

list = ["珠穆朗玛峰",1,2,True,False,0,"第一次爱的人"]
print(list)
list.append("塘朗山")
print(list)
list.insert(2,"错位时空")
print(list)
list.pop(len(list) - 1)
print(list)
list.remove(False)
print(list)
list[0] = "纳木措"
print(list)
print(len(list))
print(list[3])
print(list[2:4])
print(list[:5:2])

"""
tuple: 元组（不可变裂变）
可重复，任意类型，不支持增删改
支持索引和切片
"""

t = (1,2,3,True,False,"sidekick_boy","girl")
print(t)
print(len(t))
print(t[4])
print(t[2:6])
print(t[:len(t) + 1 : 2])