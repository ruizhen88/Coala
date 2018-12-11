def calculate_obesity():

    print("비만도 계산기입니다.\n")

    input("당신의 성별을 입력해주세요.\n1.남자\n2.여자\n")

    height = int(input("\nHow tall are you? "))
    weight = int(input("몸무게가 어떻게 되시나요? "))
    age = int(input("How old are you? "))

    bmi = weight / (height * height / 10000)
    print("\n당신의 BMI 수치는 {0}입니다.".format(bmi))

    if bmi > 35:
        print("고도 비만입니다.")
    elif bmi > 30:
        print("중등도 비만입니다.")
    elif bmi > 25:
        print("경도 비만입니다.")
    elif bmi > 23:
        print("과체중입니다.")
    elif bmi > 18.5:
        print("정상입니다.")
    else:
        print("저체중입니다.")
