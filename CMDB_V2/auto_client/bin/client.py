#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys

# 配置模块的加载路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    """
    导出主函数，并执行主函数
    """
    from src.script import run
    run()
