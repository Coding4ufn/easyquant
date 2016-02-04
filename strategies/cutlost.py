from easyquant import StrategyTemplate
from logbook import Logger
import os
log = Logger(os.path.basename(__file__))

class Strategy(StrategyTemplate):

    def initialize(self,context):
        print("cutlost initialize")

    def strategy(self, event):
        #print(self.user.balance)
        #log.info(self.user.position)

        positions = self.user.position

        for position in positions:
            r = (position['income_balance']/position['market_value'])*100
            if r < -10 and position['enable_amount'] >0:
                print("sell by cut lost:")
                print(position)
                self.user.sell(stock_code = position['stock_code'],price = position['last_price'],amount = position['enable_amount'])

    def handle_data(self,context, data):
        pass
        #log.info("cutlost handledata")