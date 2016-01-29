positions = [{'income_balance': -152.8, 'position_str': '00062000000000040029378000200000000000157927148000728', 'cost_price': 17.186, 'last_price': '16.880', 'market_value': 8440.0, 'keep_cost_price': 17.186, 'stock_name': '国元证券', 'stock_code': '000728', 'current_amount': 500, 'enable_amount': 500}]

for position in positions:
	print("sell by cut lost:")
	print(position)
	r = (position['income_balance']/position['market_value'])*100
	if r < -10 and position['enable_amount'] >0:
	   self.user.sell(stock_code = osition['stock_code'],price = position['last_price'],amount = position['enable_amount'])