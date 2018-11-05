"""compose number"""
def option():
    """input command"""
    command = input()
    number_1 = float(input())
    number_2 = float(input())
    number_3 = float(input())
    total = number_1 + number_2 + number_3
    high = first(number_1, number_2, number_3)
    low = third(number_1, number_2, number_3)
    medium = second(high, low, total)
    if command == "Ascend":
        print(str("%.2f" % low)+", "+str("%.2f" % medium)+", "+str("%.2f" % high))
    if command == "Descend":
        print(str("%.2f" % high)+", "+str("%.2f" % medium)+", "+str("%.2f" % low))
def first(number1, number2, number3):
    """check first number"""
    low = number3
    if low < number2:
        low = number2
    if low < number1:
        low = number1
    return low
def second(high, low, total):
    """check second number"""
    return total - (high + low)
def third(number1, number2, number3):
    """check third number"""
    high = number1
    if high > number2:
        high = number2
    if high > number3:
        high = number3
    return high

option()
