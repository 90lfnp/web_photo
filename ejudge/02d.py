"""[>>========]"""
def write():
    """print number"""
    number_n = int(input())
    number_start = 2
    number_end = number_n + 2
    for i in range(number_n):
        for i in range(number_start, number_end):
            print(str(i)+" ", end="")
        number_end += 1
        number_start += 1
        print("")


write()
