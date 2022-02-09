"""
@Author    : sidekick-boy
@Email     : sidekick_boy@outlook.com
"""

"""
    字符串：str
    1、单引号、双引号、三单引号、三双引号【文档字符串】
    2、拼接：+ , 复制： *, 
    3、拼接：占位符
    4、索引
    5、切片：前闭后开
    6、编解码
"""

sidekick_str = "疫情添加2例"

print(sidekick_str)
print(type(sidekick_str))
print(sidekick_str + "坂田光雅花园")
print(sidekick_str * 3)

sidekick_str = "疫情添加{},在{}日"
print(sidekick_str.format(2,"01-16"))

print(sidekick_str[1])
print(sidekick_str[1:3])

sidekick_str = " 大数据分析 "
print(sidekick_str.strip())
print(sidekick_str.lstrip())
print(sidekick_str.rstrip())


print(sidekick_str.encode(encoding="gbk"))
print(sidekick_str.encode(encoding="utf=8"))
print(sidekick_str.encode(encoding="gbk").decode(encoding="gbk"))
print(sidekick_str.encode(encoding="utf-8").decode(encoding="utf-8"))