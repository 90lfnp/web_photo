"""leap year"""
def leap_year():
    """this function show yes if is leap year and show no if is not leap year"""
    year = int(input())
    if year % 400 == 0:
        print("Yes")
    elif year % 100 == 0:
        print("No")
    elif year % 4 == 0:
        print("Yes")
    else:
        print("No")

leap_year()
