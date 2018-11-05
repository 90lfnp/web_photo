"""stepper ii"""
def repeat(number_m, number_n):
    """print number m to n"""
    if number_m == number_n:
        print(number_m)
    elif number_m < number_n:
        for i in range(number_m, number_n+1):
            print(i)
    elif number_m > number_n:
        for i in range(number_m, number_n-1, -1):
            print(i)

repeat(int(input()), int(input()))
