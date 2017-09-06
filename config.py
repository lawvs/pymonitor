#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
配置相关
封装ConfigParser
从固定路径读取配置文件

配置文件路径CONFIG_PATH
更改值后需调用save保存

常用函数
config.sections()  # 返回配置文件中节序列
config.options(section)  # 返回某个项目中的所有键的序列
config.get(section,option)  # 返回section节中，option的键值
config.add_section(str)  # 添加一个配置文件节点str
config.set(section,option,val)  # 设置section节点中，键名为option的值val
config.remove_option(section,option)  # 删除 option
config.has_section(section)  # 判断 section 是否存在
config.save()  # 保存配置文件

创建时间: 2017-9-4 11:37:39
'''

import logging
import sys
if sys.version < "3":  # python2
    import ConfigParser
else:  # python3
    import configparser
# 配置文件路径
CONFIG_PATH="config.ini"

# 创建ConfigParser实例
if sys.version < "3":  # python2
    config=ConfigParser.ConfigParser()
else:  # python3
    config=configparser.ConfigParser()

# 读取配置文件
config.read(CONFIG_PATH)

# 封装ConfigParser的write方法
def save(self):
    file=open(CONFIG_PATH, "w")
    self.write(file)
    # config.write(sys.stdout)
    logging.debug("保存配置文件 " + CONFIG_PATH)
    return

# 动态添加save方法
from types import MethodType
config.save = MethodType(save, config)

# 设置配置文件
def set_file(self, filename):
    global CONFIG_PATH
    CONFIG_PATH=filename
    self.read(CONFIG_PATH)
    logging.debug("重新加载配置文件 " + CONFIG_PATH)
    return

# 动态添加set_file方法
from types import MethodType
config.set_file = MethodType(set_file, config)


#初始化日志
def initLog():
    import logging.config
    config_path=config.get( "log", "config_path")
    logging.config.fileConfig(config_path)
    logging.debug("加载日志配置 "+config_path)
    return

#主函数 TEST
def main():
    # 初始化日志
    initLog()

    #TEST
    print("config测试")
    config.set_file("config.ini")
    print(CONFIG_PATH)
    section = 'defaults'
    print(config.sections())
    config.set( "log", "config_path", "logging.ini")
    print("test:"),
    print(config.get( "defaults", "test"))
    config.set(section,"test","test2")
    #config.add_section(section)
    config.save()
    return

#start
if __name__ == '__main__':
    main()
