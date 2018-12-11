import random

print("\n점심 메뉴 추천기입니다.\n")

menu = ["갈비탕", "떡볶이", "오뎅", "감자탕", "김치찌개", "제육볶음", "김치볶음밥"]
price = [10000, 7000, 5000, 8000, 8000, 7000]
price.append(5000)

print("메뉴판")
print("======================")
for index, value in enumerate(menu):
    print("{0:<10}{1:>10}{won}".format(value, price[index], won='원'))
print("======================")

lunch = random.randrange(0,len(menu))

print("\n오늘의 메뉴: {0}".format(menu[lunch]))
print("메뉴의 가격: {0}".format(price[lunch]))
