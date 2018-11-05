"""[>>>>>=====]"""
def write():
    """inpt number, print pyramid number"""
    number_n = int(input())
    for i in range(0, number_n):
        for j in range(1, i+2):
            print(str(j)+" ", end="")
        print("")

write()
