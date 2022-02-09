"""
@Author    : sidekick-boy
@Email     : sidekick_boy@outlook.com
"""

"""
1、dict 字典
    map
    key-value
    json
    
2、key不可重复，且必须是不可变对象
3、增删改查
"""

d = {"name": "王思德", "age": "27"}
print(d)

d["eng_name"] = "sidekick"
print(d)
print(d["name"])
print(d.get("addr", "fenggang"))

"""
1、 顺序、分支、循环
2、 分支 if
"""

age = 7

if age >= 18:
    print("成年了")
else:
    print("未成年")

score = 78

if score < 60:
    print("挂了")
elif score <= 75:
    print("及格")
elif score <= 85:
    print("良好")
else:
    print("优秀")

"""
三元表达式
"""

age = 18

result = "成年" if age >= 18 else "未成年"
print(18)

"""
1、while
2、break;continue
"""
idx = 0
while True:
    idx += 1
    print(idx)
    if idx < 100:
        pass
    else:
        break

idNum = 0

while idNum < 100:
    idNum += 1
    print(idNum)

id = 0
while id < 100:
    id += 1
    if id % 2 == 0:
        continue
    print(id)

"""
1、 for 循环
2、 计数类 循环
3、 遍历可迭代对象
"""

idx = 0
for idx in range(1, 100):
    print(idx)