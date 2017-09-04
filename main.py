#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
单机服务质量监控脚本
创建时间: 2017-9-3 14:20:21
'''
from config import config
import logging

def monitor():

    return

#初始化日志
def initLog():
    import logging.config
    # 日志配置文件位置
    config_path=config.get( 'log', 'config_path')
    logging.config.fileConfig(config_path)
    logging.debug("加载日志配置文件 " + config_path)
    return

#主函数
def main():
    initLog()
    monitor()
    return

#start
if __name__ == '__main__':
    main()
