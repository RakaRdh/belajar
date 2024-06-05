from food import Food
from drink import Drink

food1 = Food('Cangcimen', 5, 100)
food2 = Food('Permen', 2, 30)
food3 = Food('CingCongFan', 9, 200)

foods = [food1, food2, food3]

drink1 = Drink('Kopi Susu', 3, 100)
drink2 = Drink('Air Putih', 2, 50)
drink3 = Drink('Starbak', 10, 200)

drinks = [drink1, drink2, drink3]

print('Makanan')
index = 0
for food in foods:
    print(str(index) +'. '+ food.info())
    index += 1

print('Minuman')
index = 0
for drink in drinks:
    print(str(index) +'. '+ drink.info())
    index += 1

food_order = int(input('Masukkan nomor makanan: '))
selected_food = foods[food_order]

drink_order = int(input('Masukkan nomor minuman: '))
selected_drink = drinks[drink_order]

count = int(input('Mau berapa paket makanan? (Diskon 10% untuk 3 atau lebih): '))

selected_food.get_total_price(count)
selected_drink.get_total_price(count)
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print('Total harga : $ '+ str(result))