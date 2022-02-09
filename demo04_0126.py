"""
@Author    : sidekick-boy
@Email     : sidekick_boy@outlook.com
"""
"""
1、 Set
2、 不可重复
3、 没有前后顺序
4、 不可变对象
5、 增删改查
"""

s1 = {1, 2, 3}
print(s1)
print(type(s1))

s1 = {1, 2, 3, 4, 2, 3, True, 0, False, 0}
print(s1)

# s2 = s1.pop(False)
s2 = s1.remove(False)
print(s2)
print(s1)

s2 = s1.pop()

print(s2)

s1.clear()
s1.add("花和尚")

print(s1)

s4 = {1, 2, 3.14, False, (1, 2)}
print(s4)

age = 18
print(id(age))
print(type(age))
age = "Hello"
print(id(age))
print(type(age))

"""
  可变对象：修改数值，地址不变，还是原来的对象
"""

ls = [1,2,3,True,False,3.14]
ls.remove(2)
print(ls)
print(id(ls))
ls.append(888)
print(ls)
print(id(ls))





