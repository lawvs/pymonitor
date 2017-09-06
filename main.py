#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
单机服务质量监控脚本
创建时间: 2017-9-3 14:20:21
'''
from __future__ import unicode_literals
import logging
import logging.config
import yaml

from Monitor import Monitor

logger = logging.getLogger()
config={}  #  配置文件 TODO 相关异常处理
process_list = []  # 进程列表

# 任务管理
def manage():
    # 新建任务
    global process_list
    logger.debug("任务个数 " + str(len(config["monitor"]["tasks"])))
    for task in config["monitor"]["tasks"]:
        p = Monitor(task)
        process_list.append(p)
        p.start()
        logger.debug("开始任务 " + repr(p) + " " + repr(task))

    return

# TODO 停止所有进程
def stop():
    for process in process_list:
        #p.join()  # 等待进程结束
        p.terminate()  # TODO 强行终止

#初始化日志
def initLog():
    # 日志配置文件位置logging.ini
    config_path = config["log"]["config_path"]
    logging.config.fileConfig(config_path)
    logger.debug("加载日志配置完成 " + config_path)
    return

# 读取yaml配置文件
def initConfig():
    global config
    CONFIG_PATH = "config.yml"
    yml = open(CONFIG_PATH, "r")
    config = yaml.load(yml)

#主函数
def main():
    initConfig()
    initLog()
    manage()
    return

#start
if __name__ == '__main__':
    main()
