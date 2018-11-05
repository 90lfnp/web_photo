"""Triangle I"""
def triangle():
    """this function show yes if can make triangle
        or no if can't make triangle"""
    line_1 = float(input())
    line_2 = float(input())
    line_3 = float(input())
    first = min(line_1, line_2, line_3)
    third = max(line_1, line_2, line_3)
    second = (line_1 + line_2 + line_3) - (first + third)
    firstdb = first ** 2
    seconddb = second ** 2
    thirddb = third ** 2
    if line_1 == 0 or line_2 == 0 or line_3 == 0:
        print("No")
    elif abs(thirddb - (firstdb + seconddb)) <= 0.1:
        print("Yes")
    else:
        print("No")

triangle()
