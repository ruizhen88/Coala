def calculate_pay():

    print("급여계산기입니다.\n")

    pay = input("시급이 얼마입니까? ")
    time_of_day = input("하루에 몇시간 일하나요? ")
    day_of_month = input("한달에 며칠 일하나요? ")

    profit = int(pay) * int(time_of_day) * int(day_of_month)

    # 수습 적용 여부
    practice = input("""
수습을 적용 하나요?
1. 적용
2. 미적용
""")

    # 수습 적용
    if practice == 1:
        practice_price = profit // 10
    else:
        practice_price = 0

    # 세금 적용 여부
    tax = input("""
세금을 적용하나요?
1. 미적용
2. 4대 보험료 공제
3. 소득세 공제
4. 모두 적용
""")

    # 세금 적용
    if tax == '2':
        tax_price = profit * 841 // 10000
    elif tax is '3':
        tax_price = profit * 33 // 1000
    elif tax == '4':
        tax_price = profit * 841 // 10000 + profit * 33 // 1000
    else:
        tax_price = 0

    profit = profit - practice_price - tax_price

    print("\n예상 월급은: {0}원입니다.".format(profit))


    # # 할 수 있는 일
    # pc = 1200
    # lunch = 7000
    # movie = 11000
    # karaoke = 20000
    #
    # p_pc = profit // pc
    # p_lunch = profit // lunch
    # p_movie = profit // movie
    # p_karaoke = profit // karaoke
    #
    # print("""
    # {0}원으로 할 수 있는 일!
    # PC방(1200원): {1}시간
    # 점심(7000원): {2}끼
    # 영화(11000원): {3}편
    # 노래방(20000원): {4}시간
    # """.format(profit, p_pc, p_lunch, p_movie, p_karaoke))
