from easyquant import StrategyTemplate
from logbook import Logger
import os
log = Logger(os.path.basename(__file__))

class Strategy(StrategyTemplate):

	def initialize(self,context):
		print("demo2 initialize")

	def strategy(self, event):
		pass
        #print('\n\n策略2触发')
        #print('行情数据: 华宝油气', event.data['162411'])

	def handle_data(self,context, data):
		pass
		#log.info("demo2 handledata")