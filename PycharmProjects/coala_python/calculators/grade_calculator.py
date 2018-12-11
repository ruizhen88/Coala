def calculate_grade():

    print("학점계산기입니다.")

    l_subject = list()
    l_credit = list()
    l_grade = list()

    num = int(input("과목 갯수를 입력해주세요: "))

    while len(l_subject) != num:

        subject = int(input("과목명을 입력해주세요: "))
        l_subject.append(subject)

        credit = int(input("학점수 입력해주세요: "))
        l_credit.append(credit)

        grade = int(input("성적을 입력해주세요: "))
        l_grade.append(grade)


    calculate = input("""
    학점 계산 방식을 선택해주세요.
    1. 4.5 만점
    2. 4.3 만
    """)

    score = 0
    l_score = list()



    if calculate == '1':
        for grade in l_grade:
            if grade == 'A+':
                score = 4.5
            elif grade == 'A0':
                score = 4.0
            elif grade == 'B+':
                score = 3.5
            elif grade == 'B0':
                score = 3.0
            elif grade == 'C+':
                score = 2.5
            elif grade == 'C0':
                score = 2.0
            elif grade == 'D+':
                score = 1.5
            elif grade == 'D0':
                score = 1.0
            elif grade == 'F':
                 score = 0
            l_score.append(int(score))


    elif calculate == '2':
        for grade in l_grade:
            if grade == 'A+':
                score = 4.3
            elif grade == 'A0':
                score = 4.0
            elif grade == 'A-':
                score = 3.7
            elif grade == 'B+':
                score = 3.3
            elif grade == 'D-':
                score = 0.7
            elif grade == 'F':
                score = 0
            else:
                score = "N/A"
            l_score.append(int(score))

    for index, credit in enumerate(l_credit):
        # (1, 2) (2, 3) (3, 1)

    l_total = list()
    for index, score in enumerate(l_score):
        total = score * l_credit[index]
        l_total.append(int(total))

    n = 0
    while n != num
        l_total[n] +

    GPA =

    print("""
    총 학점: {0}
    GPA: {1}
    """.format())

