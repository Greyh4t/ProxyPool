#!/usr/bin/env python
# coding:utf-8
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2693.2 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

PROXYPOOL_CONFIG = {
    'MIN_IP_NUM': 5000,  # 代理池中最小可用ip数量，若检测到小于此数量，启动爬虫
    'DELETE_TIME': 24 * 60,  # minutes, 删除该时间之前的ip
    'UPDATE_TIME': 10,  # minutes, 更新该时间之前的ip
    'CRAWL_TIME': 30  # minutes, 计算可用ip数量时取该时间之内
}

API_CONFIG = {
    'PORT': 8000
}

CRAWLER_CONFIG = {
    'THREAD_NUM': 20,
    'TIMEOUT': 5,
    'RETRY_TIMES': 5
}

VALIDATE_CONFIG = {
    'THREAD_NUM': 1000,
    'TIMEOUT': 20,
    'PROXY_TYPE': [0, 1, 2, 3],
    'TARGET': 'http://proxy.mimvp.com/check.php',
    # 'TARGET1': 'http://7xr8ng.com1.z0.glb.clouddn.com/a.txt',
    # 'TARGET2': 'http://www.stilllistener.com/checkpoint1/test11/'
}

DB_CONFIG = {
    'SQLITE': './data/proxy.db'
}

LOG_CONFIG = {
    'LOG_TO_FILE': False,
    'LOG_TO_PRINT': True,
    'FILE_PATH': './proxyPool.log'
}
