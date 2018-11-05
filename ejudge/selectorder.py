"""selectorder"""
def function():
    """print oder"""
    count = int(input())
    countn = 0
    nam = []
    while countn < count:
        countn = countn + 1
        nam.append(input())
    num = input()
    num = num.split(" ")
    countnn = 0
    while countnn < count:
        countnn = countnn + 1
        print("Name : "+nam[num[countnn]]+" Price : "+num[num[(countnn+1)]])
function()
