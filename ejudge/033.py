"""[>>>>>>>===]"""
def write():
    """print number"""
    number_n = int(input())
    space = number_n * 3 - 3
    back = 0
    for i in range(0, number_n):
        print(" " * space, end="")
        for j in range(1, i+2):
            print(("%02d" % j)+" ", end="")
        for k in range(back, 0, -1):
            if k != 0:
                print(("%02d" % k)+" ", end="")
        print("")
        space -= 3
        back += 1

write()

