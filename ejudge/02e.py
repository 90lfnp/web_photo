"""[>>>=======]"""
def write():
    """print number"""
    number_n = int(input())
    number_start = 1
    number_end = number_n + 1
    for i in range(number_n):
        for i in range(number_start, number_end):
            print(str(i)+" ", end="")
        number_start += number_n
        number_end += number_n
        print("")

write()
