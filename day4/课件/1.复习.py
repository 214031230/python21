# 文件操作
    # 打开文件
        # f = open('文件路径')  默认的打开方式r ，默认的打开编码是操作系统的默认编码
        # r w a （r+ w+ a+） 以上6种加b  ，如果打开模式+b，就不需要指定编码了
        # 编码 UTF-8 ，gbk
    # 操作文件
        # 读
            # read 不传参数 意味着读所有
                # 传参，如果是r方式打开的，参数指的是读多少个字符
                # 传参，如果是rb方式打开的，参数指的是读多少个字节
            # readline
                # 一行一行读  每次只读一行，不会自动停止
            # for循环的方式
                # 一行一行读  从第一行开始 每次读一行 读到没有之后就停止
        # 写
            # write 写内容
    # 关闭文件
        # f.close()
    # with open() as f:
    # 修改文件 ：
        # import os
        # os.remove
        # os.rename
# 函数
    # 定义
        # 关键字 def 函数名(形参):
        # 参数 ：
            # 位置参数
            # *args  动态传参 ：接收在调用的时候传过来的多余的所有按位置传的参数
            # 关键字参数 默认参数，如果不传会有一个默认的值，如果传了会覆盖默认的值
            # **kwargs  动态传参 ：接收在调用的时候传过来的多余的所有按关键字传的参数
        # 返回值
            # return 停止一个程序的运行，返回参数
                # 没有返回值 默认返回None
                # 有一个返回值
                # 返回多个值
    # 调用
        # 调用的关键字 函数名(实参)
        # 传参数 ：
            # 按照位置传
            # 按照关键字传
        # 接收返回值
            # 没有返回值 不接受
            # 有一个返回值 用一个变量接收
            # 有多个返回值
                # 用一个变量接收 所用返回值都会被组织成一个元组
                # 用多个变量接收 有多少个返回值 就必须用多少个变量接收
# 函数是第一类对象的概念
    # 函数名 --> 函数的内存地址
    # 函数名可以作为 容器类型的元素 函数的参数、返回值 还能进行赋值  --> 变量

# 闭包和装饰器
    # 闭包的定义 : 内部函数引用外部函数的变量
    # 闭包的应用 ：装饰器