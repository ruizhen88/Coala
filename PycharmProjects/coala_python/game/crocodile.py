import random

print("악어게임")
the_answer = random.randint(1, 20)
print(the_answer)

status = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
          "19", "20"]

your_answer = 0
while int(your_answer) != int(the_answer):

    print('''
              --------                      --------
                    0                       0
      --------------------------------------------------------
                O                               O
    ============================================================
    | {0} || {1} || {2} || {3} || {4} || {5} || {6} || {7} || {8} || {9} |
    ------------------------------------------------------------
    
    ------------------------------------------------------------
    | {10} || {11} || {12} || {13} || {14} || {15} || {16} || {17} || {18} || {19} |
    ============================================================
    '''.format(status[0], status[1], status[2], status[3], status[4],
               status[5], status[6], status[7], status[8], status[9],
               status[10], status[11], status[12], status[13], status[14],
               status[15], status[16], status[17], status[18], status[19]))

    your_answer = input("번호를 입력해주세요: ")

    if int(your_answer) == int(the_answer):
        print("Ooops!!!")
    else:
        n = int(your_answer)
        status[n - 1] = " "
