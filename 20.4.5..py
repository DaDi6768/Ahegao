import json
with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
print(orders)

max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2 Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order = ""
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_quantity = quantity
        max_order = order_num
print(f"2. Номер заказа {max_order} с самым большим количеством товара: {max_quantity}")

#В какой день в июле было сделано больше всего заказов?
max_date = {}
for order_num, orders_data in orders.items():
    date = orders_data["date"]
    max_date[date] = max_date.get(date,0) + 1
for date in sorted(max_date):
    max_value = max(max_date.values())
    if max_date[date] == max_value:
        print(f"3. больше всего заказов: {max_date[date]}, в {date}")
print(f"3. Больше всего заказов: {max_quantity} сделано в этот день: {max_date} июля")

#Какой пользователь сделал самое большое количество заказов за июль?
max_quantity = 0
max_user_id = {}
for order_num, orders_data in orders.items():
    user_id = orders_data["user_id"]
    max_user_id[user_id] = max_user_id.get(user_id, 0) + 1
    quantity_2 = max_user_id.get(user_id)
    if quantity_2 > max_quantity:
        max_quantity = quantity_2
print(f"4. Больше всего заказов: {max_quantity}, сделал пользователь: {user_id}")

#У какого пользователя самая большая суммарная стоимость заказов за июль?
max_price = 0
max_user_id = {}
for order_num, orders_data in orders.items():
    user_id = orders_data["user_id"]
    max_user_id[user_id] = max_user_id.get(user_id, 0) + orders_data["price"]
    price_2 = max_user_id.get(user_id)
    if price_2 > max_price:
        max_price = price_2
print(f"5. Пользователь: {user_id}, имеет самую большую стоимость заказа за июль: {max_price}")
#Какая средняя стоимость заказа была в июле?

#Какая средняя стоимость товаров в июле?
for order_num, orders_data in orders.items():
    price = orders_data["price"]
    quantity = orders_data["quantity"]
    sr_price = price / quantity
print(f"7.Средняя стоимость товара была в июле: {sr_price}")






