# 과제1
print("가위 바위 보\n")

first = input("Player1: \n1.가위\n2.바위\n3.보\n")
second = input("\nPlayer2: \n1.가위\n2.바위\n3.보\n")

if first == "1":
    first = "가위"
elif first == "2":
    first = "가위"
else:
    first = "보"

if second == "1":
    second = "가위"
elif second == "2":
    second = "가위"
else:
    second = "보"

print("\n첫번째 플레이어는 {0}를 냈습니다.".format(first))
print("두번째 플레이어는 {0}를 냈습니다.\n".format(second))

if first == second :
    print("동점입니다.\n")
elif first == "가위" and second == "바위" :
    print("두번째 플레이어가 {0}로 승리하였습니다!".format(second))
elif first == "가위" and second == "보" :
    print("첫번째 플레이어가 {0}로 승리하였습니다!".format(first))
elif first == "바위" and second == "가위" :
    print("첫번째 플레이어가 {0}로 승리하였습니다!".format(first))
elif first == "바위" and second == "보" :
    print("두번째 플레이어가 [0}로 승리하였습니다!".format(second))
elif first == "보" and second == "가위" :
    print("두번째 플레이어가 {0}로 승리하였습니다!".format(second))
else :
    print("첫번째 플레이어가 {0}로 승리하였습니다!".format(first))
