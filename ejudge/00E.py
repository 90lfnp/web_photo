"""check mximum number"""
def mximum():
    """check mximumnumber"""
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())
    number_4 = int(input())
    number_5 = int(input())
    number_6 = int(input())
    number_7 = int(input())
    number_8 = int(input())
    mx_number = number_1
    if mx_number < number_2:
        mx_number = number_2
    if mx_number < number_3:
        mx_number = number_3
    if mx_number < number_4:
        mx_number = number_4
    if mx_number < number_5:
        mx_number = number_5
    if mx_number < number_6:
        mx_number = number_6
    if mx_number < number_7:
        mx_number = number_7
    if mx_number < number_8:
        mx_number = number_8
    print(mx_number)

mximum()
