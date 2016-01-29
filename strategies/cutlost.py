from easyquant import StrategyTemplate


class Strategy(StrategyTemplate):
    def strategy(self, event):
        #print(self.user.balance)
        #print(self.user.position)

        positions = self.user.position

        for position in positions:
            r = (position['income_balance']/position['market_value'])*100
            if r < -10 and position['enable_amount'] >0:
                print("sell by cut lost:")
                print(position)
                self.user.sell(stock_code = position['stock_code'],price = position['last_price'],amount = position['enable_amount'])
