"""table i"""
def table(number):
    """input number, show table 15 * n"""
    for i in range(1, number+1):
        print("15 x "+str(i)+" = "+str(15*i))

table(int(input()))
