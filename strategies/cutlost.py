from easyquant import StrategyTemplate
from logbook import Logger
import os
log = Logger(os.path.basename(__file__))

class Strategy(StrategyTemplate):

    def initialize(self,context):
        print("cutlost initialize")

    def strategy(self, event):
        pass
        #print(sina().all)
        # for k,v in event.data.items():
        #     if(v['ask1_volume'] != 0 and v['ask2_volume']  == 0 
        #         and v['ask3_volume']  == 0 and v['ask4_volume']  == 0 
        #         and v['ask5_volume']  == 0 and not v['name'].startswith('ST')
        #         and not v['name'].startswith('*ST') and not k.startswith('300') ):
        #         print(k)
        #         print(v)
        #         self.user.buy(stock_code = k,price = v['ask1'],volume = self.user.balance[0]['current_balance'])
        #log.info("self.user.balance")
        #log.info(self.user.balance[0]['current_balance'])
        #log.info(self.user.position)

        # positions = self.user.position

        # for position in positions:
        #     if position['market_value'] == 0 or position['enable_amount'] <=0 :
        #         continue
        #     r = (position['income_balance']/position['market_value'])*100
        #     if r < -3 and position['enable_amount'] >0:
        #         print("sell by cut lost:")
        #         print(position)
        #         self.user.sell(stock_code = position['stock_code'],price = position['last_price'],amount = position['enable_amount'])

    def handle_data(self,context, data):
        for k,v in data.items():
            if(v['ask1_volume'] != 0 and v['ask2_volume']  == 0 
                and v['ask3_volume']  == 0 and v['ask4_volume']  == 0 
                and v['ask5_volume']  == 0 and not v['name'].startswith('ST')
                and not v['name'].startswith('*ST') and not k.startswith('300')
                and v['ask1'] < 50):
                self.user.buy(stock_code = k,price = v['ask1'],volume = self.user.balance[0]['enable_balance'])
                print(k)
                print(v)
                print(k)
                print(v['ask1'])
                print(self.user.balance[0]['enable_balance'])
        #print(data.data)
        #log.info("cutlost handledata")
        positions = self.user.position

        for position in positions:
            if position['market_value'] == 0 or position['enable_amount'] <=0 :
                continue
            r = (position['income_balance']/position['market_value'])*100
            if r < -3 and position['enable_amount'] >0:
                self.user.sell(stock_code = position['stock_code'],price = position['last_price'],amount = position['enable_amount'])
            if (data[position['stock_code']]['ask1_volume'] != 0 and position['enable_amount'] > 0):
                 self.user.sell(stock_code = position['stock_code'],price = position['last_price'],amount = position['enable_amount'])