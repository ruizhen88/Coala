def calculate_normal():

    print("일반 계산기입니다.")

    first = input("계산할 첫번째 값을 입력해주세요: ")
    second = input("계산할 두번째 값을 입력해주세요: ")

    print("\n두 개의 값: {0}와 {1}".format(first,second))

    calculate = input("""
원하는 연산을 선택하시오.
1. 더하기
2. 빼기
3. 곱하기
4. 정수 나누기
5. 실수 나누기
6. 나머지 구하기
""")

    plus = int(first) + int(second)
    minus = int(first) - int(second)
    multiple = int(first) * int(second)
    a_divide = int(first) // int(second)
    b_divide = int(first) / int(second)
    left = int(first) % int(second)

    if calculate == "1":
        print("더하기 값 (a + b) : {0}".format(plus))
    elif calculate == "2":
        print("빼기 값 (a - b) : {0}".format(minus))
    elif calculate == "3":
        print("곱하기 값 (a * b) : {0}".format(multiple))
    elif calculate == "4":
        print("정수 나누기 값 (a // b) : {0}".format(a_divide))
    elif calculate == "5":
        print("실수 나누기 값 (a / b) : {0}".format(b_divide))
    elif calculate == "6":
        print("나머지 값 (a % b) : {0}".format(left))
