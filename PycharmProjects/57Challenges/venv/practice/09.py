while True:
    str_length = raw_input("How long is the ceiling? ")
    try:
        float(str_length)
    except ValueError:
        print("Please enter a number.")
    else:
        break

while True:
    str_width = raw_input("What is the width of the ceiling? ")
    try:
        float(str_width)
    except ValueError:
        print("Please enter a number.")
    else:
        break

length = float(str_length)
width = float(str_width)
area = length * width
liters = int(area) // 9 + 1

print ("You will need to purchase {} liters of paint to cover {} square meters.".format(liters, area))