print('輸入q終止程式。')
products = []
while True:
	name = input('請輸入商品名稱。')
	if name == 'q':
		break
	price = input('請輸入商品價格。')
	products.append([name, price])
print(f'你輸入的商品有{products}。')
for p in products:
	print(f'{p[0]}是{p[1]}元。')