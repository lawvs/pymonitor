#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
根据task
循环执行监控任务
创建时间: 2017-9-6 16:38:16
'''

import os
import sys
import time
import random
import logging
import multiprocessing
import pycurl

# 解决中文编码问题
if sys.version < "3":  # python2
    reload(sys)
    sys.setdefaultencoding( "utf-8" )

logger = logging.getLogger()

class Monitor(multiprocessing.Process):  # TODO 类优化
    def __init__(self, task):
        super(Monitor, self).__init__()
        self.task = task
        self.name = task["name"]
        self.url = task["url"]
        self.interval = task["interval"]
        return

    # 探测
    def curl_webSev(self):
        # TODO 封装
        _Curl = pycurl.Curl()
        _Curl.setopt(pycurl.CONNECTTIMEOUT,10)
        _Curl.setopt(pycurl.TIMEOUT,10)
        _Curl.setopt(pycurl.NOPROGRESS,1)
        _Curl.setopt(pycurl.FORBID_REUSE,1)
        _Curl.setopt(pycurl.MAXREDIRS,1)
        _Curl.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
        _Curl.setopt(pycurl.URL,self.url)
        _Curl.setopt(pycurl.HTTPHEADER,["user-agent: pymonitor"])

        try:
            with open(os.path.dirname(os.path.realpath(__file__)) + "/cache/" + self.name + ".tmp",'wb') as outfile:
                _Curl.setopt(pycurl.WRITEHEADER,outfile)
                _Curl.setopt(pycurl.WRITEDATA,outfile)
                _Curl.perform()
        except Exception as e:
            logger.exception(e)
            return None
        return _Curl


    def run(self):
        import logging.config
        config_path = "logging.ini"  # TODO 优化
        logging.config.fileConfig(config_path)
        logger.debug("pid:" + repr(os.getpid()) + " " +self.name + " 进程加载日志配置完成 " + config_path)

        # 防止多进程同时并发
        time.sleep(random.randint(0, self.interval))
        work = 1
        while work:
            logger.debug("pid:" + repr(os.getpid()) + " " +self.name + " 正在监测 " + self.url)
            result = self.curl_webSev()  # 监测
            logger.debug("pid:" + repr(os.getpid()) + " " +self.name + " 监测完成 ")
            handleResult(result)  # 结果处理
            time.sleep(self.interval)
        logger.debug("pid:" + repr(os.getpid()) +  " 监测任务结束 " + self.url)
        return


# 监控结果处理
def handleResult(_Curl):
    if not _Curl:
        return
    # TODO 优化输出
    logger.info("URL:\t%s" %_Curl.getinfo(_Curl.EFFECTIVE_URL))
    logger.info("Http Code:\t%s" %_Curl.getinfo(_Curl.HTTP_CODE))
    logger.info("DNS lookup time:\t%s ms" %(_Curl.getinfo(_Curl.NAMELOOKUP_TIME) * 1000))
    logger.info("Create conn time:\t%s ms" %(_Curl.getinfo(_Curl.CONNECT_TIME) * 1000))
    logger.info("Ready conn time:\t%s ms" %(_Curl.getinfo(_Curl.PRETRANSFER_TIME) * 1000))
    logger.info("Tran Star time:\t%s ms" %(_Curl.getinfo(_Curl.STARTTRANSFER_TIME) * 1000))
    logger.info("Tran Over time:\t%s ms" %(_Curl.getinfo(_Curl.TOTAL_TIME) * 1000))
    logger.info("Download size:\t%d bytes/s" %_Curl.getinfo(_Curl.SIZE_DOWNLOAD))
    logger.info("HTTP header size:\t%d byte" %_Curl.getinfo(_Curl.HEADER_SIZE))
    logger.info("Avg download speed:\t%s bytes/s" %_Curl.getinfo(_Curl.SPEED_DOWNLOAD))
    # TODO 保存/发送服务器
    return

# TEST
if __name__ == '__main__':
    task = {'url': 'www.github.com', 'interval': 5, 'name': 'github监测任务'}
    p = Monitor(task)
    p.start()
