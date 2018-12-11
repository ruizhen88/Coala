import random

print("\n로또 추첨기입니다!")
print("당첨 번호: ", end="")

lotto = list()

while len(lotto) != 7:
    new_number = random.randint(1, 45)
    if new_number not in lotto:
        lotto.append(new_number)

for index, value in enumerate(lotto):
    if index == len(lotto)-1:
        print("\n2등 보너스볼 : {0}".format(value))
    else:
        print(value, end='')

# print("당첨 번호: {0}, {1}, {2}, {3}, {4}, {5}"
#       .format(lotto[0], lotto[1], lotto[2], lotto[3], lotto[4], lotto[5]))
# print("2등 보너스 볼: {0}".format(lotto[6]))

