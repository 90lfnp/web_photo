"""[>>>>======]"""
def write():
    """input number n, print number"""
    number_n = int(input())
    number_start = 0
    number_end = number_n
    count = 0
    for i in range(number_end, number_start, -1):
        count += 1
        print(str(i)+" ", end="")
        if count % 7 == 0:
            print("")

write()
