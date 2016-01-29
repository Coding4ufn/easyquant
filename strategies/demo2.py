from easyquant import StrategyTemplate


class Strategy(StrategyTemplate):

	def initialize(self,context):
		print("demo2 initialize")

	def strategy(self, event):
		pass
        #print('\n\n策略2触发')
        #print('行情数据: 华宝油气', event.data['162411'])
