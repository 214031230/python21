# #!/usr/bin/env python3
#
#
#
# 1. 有两个文件A.txt和B.txt,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# with open("day1.py", encoding="utf-8") as f1, open("day2.py", encoding="utf-8") as f2, open("test", mode="a", encoding="utf-8") as f3:
#     for i in f1:
#         f3.write(i)
#     for i in f2:
#         f3.write(i)


# 2. 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# res = input("请输入字母：")
# with open("test1", "a", encoding="utf-8") as f1:
#     f1.write(res.upper())
# 3. 用户输入账号 密码，判断用户密码是否在文件中，连续输错3次后程序终止，连续三次是同一个用户错误，锁定用户。

# 4、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(argv):
#     return [i for i, v in enumerate(argv, 1) if i % 2 == 1]
# l = [1,2,3,4,5]
# t = (1,2,3,4,5)
# print(func(t))
# 5、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def func(argv):
#     if len(argv) > 5:
#         return True
# func1 = lambda x: True if len(x) > 5 else 0
# dic = {1:[1,2,3,4],
#        2:3,
#        3:4}
# print(dic[1])
#
# dic[1][-1] = "alex"
# print(dic)


# 6、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(argv):
#     if len(argv) > 2:
#         return argv[:2]
# lst = [1,2,3,4]
# print(func(lst))
# 7、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数，并返回结果。

# 8、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容，并返回结果。
# 9、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# 	PS:字典中的value只能是字符串或列表
# 10、写函数，接收两个数字参数，返回比较大的那个数字。
#
# 11、文件操作: （编程）
#
#      文件 demo.txt 如下:
#
#     ```
#         global
#         log 127.0.0.1 local2
#         daemon
#         maxconn 256
#
#         backend www.luffycity.com
#            server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
#            server 100.1.7.8 100.1.7.8 weight 20 maxconn 3000
#            server 100.1.7.7 100.1.7.6 weight 20 maxconn 3000
#         backend buy.luffycity.com
#            server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000
#     ```
#     a. 用户input输入  www.luffycity.com 则将其以下内容添加到列表返回给用户(终端)
#         既:
#
#     ```
#     li = [
#         "server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000"
#         "server 100.1.7.8 100.1.7.8 weight 20 maxconn 3000"
#         "server 100.1.7.7 100.1.7.6 weight 20 maxconn 3000"
#     ]
#     ```
#     b.  设置内容, 用户通过输入 input输入
#
#     ```
#         {"backend": "www.luffycity.com","record":{"server": "100.1.7.6","weight": 20,"maxconn": 30}}
#     ```
#     则在文件的 backend www.luffycity.com 下新加入一条记录
#
#     ```
#     backend www.luffycity.com
#     server 100.1.7.6 100.1.7.6 weight 20 maxconn 3000
#     ```
#     注: 由于文件直接修改时会覆盖原有内容, 所以可利用同时打开俩个文件, 边读边写到达指定位置时, 插入此数据。
