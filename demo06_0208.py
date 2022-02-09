"""
@Author    : sidekick-boy
@Email     : sidekick_boy@outlook.com
"""

"""
   列表生成器
"""

ls = [idx for idx in range(0, 101)]
print(ls)

"""
    1. 函数
"""


def show():
    pass


def show1(name):
    print("welcome, {}.".format(name))


show1("Tom")
show1("sidekick")


def show2(age1, age2):
    return age1 + age2


num = show2(6, 8)
print(num)


def show3(*nums):
    s = 0
    print(type(nums))
    for num in nums:
        s += num
    return s


sum = show3(1, 2, 3, 4, 5)
print(sum)


def show4(num, a=2):
    """
    求一个幂次运算
    :param num: 底数
    :param a: 指数
    :return: 返回值
    """
    return num ** a


print(show4(2, 3))
print(show4(2))


def operate_nums(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2


print(type(operate_nums(2, 1)))

"""
    1. package 和 module
    2. 包的本质就是一个文件夹
    3. 模块的本质就是一个py文件
    4. 引入方式为：from import as 
"""

import math as m

print(m.fabs(-3.14))
print(m.sqrt(10))

from math import sqrt as sq

print(type(sq))
print(sq(10))

from package import module as pk

ls = pk.PRICE
print(ls)
ld = pk.comminicate("Ke Hong", "25", "23")
print(ld)

"""
   1.异常处理
"""

a = 10
b = 2

print(a + b)
print(a * b)
print(a - b)

try:
    print(a / b)
except Exception as ex:
    print(ex)
finally:
    print("Hello World~")