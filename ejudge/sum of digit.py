"""sum of digit"""
import math
def function():
    """print sum of digit"""
    num = int(input())
    fir = math.floor(num/10000)
    sec = math.floor(num/1000)%10
    thi = math.floor(num/100)%10
    fou = math.floor(num/10)%10
    fif = num%10
    print(fir+sec+thi+fou+fif)
function()

