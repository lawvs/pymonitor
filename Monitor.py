#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
根据task
循环执行监控任务
创建时间: 2017-9-6 16:38:16
'''

import os
import time
import random
import logging
import multiprocessing

from curl_webSev import curl_webSev

logger = logging.getLogger()

class Monitor(multiprocessing.Process):
    def __init__(self, task):
        super(Monitor, self).__init__()

        self.name = task["name"]
        self.url = task["url"]
        self.interval = task["interval"]
        return

    def run(self):
        import logging.config
        config_path = "logging.ini"  # TODO 优化
        logging.config.fileConfig(config_path)
        logger.debug("pid:" + repr(os.getpid()) + " 进程加载日志配置完成 " + config_path)

        # 防止多进程同时并发
        time.sleep(random.randint(0, self.interval))
        work = 1
        while work:
            logger.debug("pid:" + repr(os.getpid()) +  " 正在监测 " + self.url)
            curl_webSev(self.url)
            logger.debug("pid:" + repr(os.getpid()) +  " 监测完成 " + self.url)
            time.sleep(self.interval)
        logger.debug("pid:" + repr(os.getpid()) +  " 监测任务结束 " + self.url)
        return

if __name__ == '__main__':
    task = {'url': 'www.github.com', 'interval': 5, 'name': 'github'}
    p = Monitor(task)
    p.start()
