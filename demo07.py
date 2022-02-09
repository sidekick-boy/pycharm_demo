"""
@Author    : sidekick-boy
@Email     : sidekick_boy@outlook.com
"""

"""
    1. 读取文件
    2. 打开 open
    3. 读 read
    4. 写 write
    5. 关闭 close
"""

FILE_PATH = 'data.csv'
f = open(file=FILE_PATH, mode="r", encoding="utf-8")
# data = f.read()
# print(data)


data = f.readlines()
print(data)
for line in data:
    ls = [int(num.strip()) for num in line.split(",")]
    print(ls)
f.close()

d = open(file="mydata.csv", mode="w", encoding="utf-8")
d.write("1,2,3,4,5")
d.close()
