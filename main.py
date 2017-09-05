#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
单机服务质量监控脚本
创建时间: 2017-9-3 14:20:21
'''
from __future__ import unicode_literals
from config import config
import logging
import sys
from curl_webSev import curl_webSev

def monitor():
    url="www.github.com"
    logging.info("开始监测 " + url)
    curl_webSev(url)
    logging.info("监测完成 " + url)
    return

#初始化日志
def initLog():
    import logging.config
    # 日志配置文件位置
    config_path=config.get( "log", "config_path")
    logging.config.fileConfig(config_path)
    logging.debug("加载日志配置 " + config_path)
    return

#主函数
def main():
    initLog()
    monitor()
    print(config.get( 'defaults', 'test'))
    return

#start
if __name__ == '__main__':
    main()
