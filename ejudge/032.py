"""[>>>>>>-===]"""
def write():
    """print number"""
    number_n = int(input())
    space = number_n * 3 - 3
    for i in range(0, number_n):
        print(" " * space, end="")
        for j in range(1, i+2):
            print(("%02d" % j)+" ", end="")
        print("")
        space -= 3

write()
