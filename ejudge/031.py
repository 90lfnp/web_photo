"""[>>>>>>====]"""
def write():
    """inpt number, print pyramid number"""
    number_n = int(input())
    number_m = number_n - 1
    for i in range(0, number_n):
        for j in range(1, i+2):
            print(str(j)+" ", end="")
        print("")
    while number_m != 0:
        for i in range(number_m, 0, -1):
            for j in range(1, i+1):
                print(str(j)+" ", end="")
            print("")
            number_m -= 1

write()
