# coding:utf-8
import os
import sys
from logbook import Logger, StreamHandler
from datetime import *  



class StrategyTemplate:
    def __init__(self, user):
        self.user = user
        self.log = Logger(os.path.basename(__file__))
        StreamHandler(sys.stdout).push_application()

    def strategy(self, event):
        """:param event event.data 为所有股票的信息，结构如下
        {'162411':
        {'ask1': '0.493',
         'ask1_volume': '75500',
         'ask2': '0.494',
         'ask2_volume': '7699281',
         'ask3': '0.495',
         'ask3_volume': '2262666',
         'ask4': '0.496',
         'ask4_volume': '1579300',
         'ask5': '0.497',
         'ask5_volume': '901600',
         'bid1': '0.492',
         'bid1_volume': '10765200',
         'bid2': '0.491',
         'bid2_volume': '9031600',
         'bid3': '0.490',
         'bid3_volume': '16784100',
         'bid4': '0.489',
         'bid4_volume': '10049000',
         'bid5': '0.488',
         'bid5_volume': '3572800',
         'buy': '0.492',
         'close': '0.499',
         'high': '0.494',
         'low': '0.489',
         'name': '华宝油气',
         'now': '0.493',
         'open': '0.490',
         'sell': '0.493',
         'turnover': '420004912',
         'volume': '206390073.351'}}
        """
        pass

    def run(self, event):
        try:
            self.strategy(event)
        except Exception as e:
            self.log.error(e)

    def initializeNull(self):
        self.initialize(self.user)

    def initialize(self,context):
        pass

    def handle_dataNull(self,event):
        startm = time(9,30,0)
        endm = time(11,30,0)
        starta = time(13,00,0)
        enda = time(14,50,0)
        now =  datetime.now().time()
        if (now >= startm and now <endm) or (now >= starta and now <enda):
            self.handle_data(self.user, event.data)

    def handle_data(self,context, data):
        self.log.info("handle_data")

    def before_trading_startNull(self,event):
        t = time(9,20,0)
        now =  datetime.now().time()
        if t.hour == now.hour and t.minute == now.minute and t.second == now.second:
            self.before_trading_start(self.user)


    def before_trading_start(self,context):
        self.log.info("before_trading_start is not define")

    def after_trading_endNull(self,event):
        t = time(15,10,0)
        now =  datetime.now().time()
        if t.hour == now.hour and t.minute == now.minute and t.second == now.second:
            self.after_trading_end(self.user)

    def after_trading_end(self,context):
        self.log.info("after_trading_end is not define")
