total_price = 0
number = int(input("Number of items"))
while number <= 0:
    print("Invalid number of items")
    number = int(input("Number of items"))
for i in range(1, number + 1):
    price_of_item = float(input('Price of item: $'))
    total_price += price_of_item
if total_price > 100:
    total_price -= (total_price * 0.1)
print("Total price for {} items is ${:.2f}".format(number, total_price))
