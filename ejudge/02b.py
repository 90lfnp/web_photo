"""[==========]"""
def write():
    """write table number n*n"""
    lap = int(input())
    for _ in range(lap):
        for i in range(lap):
                print(str(i+1)+" ", end="")
        print("")

write()
