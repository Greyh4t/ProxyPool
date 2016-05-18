#!/usr/bin/env python
# coding:utf-8
from gevent import monkey
monkey.patch_all()
import datetime
import time
import threading
from logger import logger
from DB import DatabaseObject
from config import DB_CONFIG, PROXYPOOL_CONFIG, API_CONFIG
from crawler import Crawler
from validator import Validator
from api import ProxyServer


class ProxyPool:
    def __init__(self):
        self.sqlite = DatabaseObject(DB_CONFIG['SQLITE'])
        self.Validator = Validator()
        self.Crawler = Crawler()

    def _monitor(self):
        while True:
            self._update(PROXYPOOL_CONFIG['UPDATE_TIME'])
            self._delete(PROXYPOOL_CONFIG['DELETE_TIME'])
            self._crawl(PROXYPOOL_CONFIG['CRAWL_TIME'])
            time.sleep(1800)

    def _crawl(self, minutes):
        query = 'SELECT COUNT(*) FROM proxy WHERE updatetime>\'%s\'' % (
        (datetime.datetime.now() - datetime.timedelta(minutes=minutes)).strftime('%Y-%m-%d %H:%M:%S'))
        count = self.sqlite.executesql(query)[0]
        if int(count[0]) < PROXYPOOL_CONFIG['MIN_IP_NUM']:
            logger.info('Crawl proxy begin')
            proxies = self.Crawler.run()
            logger.info('Crawl proxy end')
            logger.info('Validate proxy begin')
            avaliable_proxies = self.Validator.run(proxies)
            logger.info('Validate proxy end')
            if DB_CONFIG['SQLITE']:
                self.save2sqlite(avaliable_proxies)

    def _delete(self, minutes):
        query = 'DELETE FROM proxy WHERE updatetime<\'%s\'' % (
        (datetime.datetime.now() - datetime.timedelta(minutes=minutes)).strftime('%Y-%m-%d %H:%M:%S'))
        self.sqlite.executesql(query)

    def _update(self, minutes):
        query = 'SELECT ip,port FROM proxy WHERE updatetime<\'%s\'' % (
        (datetime.datetime.now() - datetime.timedelta(minutes=minutes)).strftime('%Y-%m-%d %H:%M:%S'))
        proxies = ['%s:%s' % n for n in self.sqlite.executesql(query)]
        if proxies:
            avaliable_proxies = self.Validator.run(proxies)
            self.save2sqlite(avaliable_proxies)

    def save2sqlite(self, result):
        failed = self.sqlite.insert('proxy', result)
        if failed:
            failed = self.sqlite.update('proxy', failed)
        if failed:
            logger.info('Some ip failed to save: %s' % (str(failed)))

    def _api(self):
        ProxyServer(API_CONFIG['PORT'])

    def run(self):
        t1 = threading.Thread(target=self._api)
        t2 = threading.Thread(target=self._monitor)
        t1.start()
        t2.start()


if __name__ == '__main__':
    ProxyPool().run()
