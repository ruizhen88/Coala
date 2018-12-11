# 1. 문제 만들기: 랜덤한 숫자 4가지 & 중복 ㄴㄴ
# 2. 입력 받기
# 3. 채점하기: 존재 & 같은자리: S / 존재 & 같은자리 ㄴㄴ: B / 존재ㄴㄴ: OUT
# 4. 출력: S가 4개면 종료, 아니면 반복

import random
print("야구게임 시작")
the_answer = list()

while len(the_answer) != 4:
    num = random.randint(0, 9)
    if num not in the_answer:
        the_answer.append(num)

print(the_answer)
strike = 0
count = 0

while strike != 4:
    your_answer = input("숫자 네자리를 입력해주세요: ")

    strike = 0
    ball = 0
    count += 1

    for index, value in enumerate(your_answer):
        if int(value) == the_answer[index]:
            strike += 1
        elif int(value) in the_answer:
            ball += 1

    if strike == 0 and ball == 0:
        print("아웃입니다.")
    else:
        print("{0}스트라이크 {1}볼입니다.".format(strike, ball))

print("{0}회만에 정답입니다.".format(count))
