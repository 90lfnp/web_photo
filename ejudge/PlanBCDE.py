"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def func_1():
    """If Else Ues"""
    word = str(input())
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_top = 0
    num_down = 0
        num_top = num_1
    if num_2 > num_1 and num_2 > num_3:
        num_top = num_2
    elif num_3 > num_1 and num_3 > num_2:
        num_top = num_3
    num_down = num_3
    if num_2 < num_3 and num_2 < num_1:
        num_down = num_2
    elif num_1 < num_2 and num_1 < num_3:
        num_down = num_1
    num_mid = (num_1 + num_2 + num_3) - (num_top + num_down)
    if word == "Ascend":
         DownAscend(num_1, num_2, num_3, num_top, num_down)
    elif word == "Descend":
         TopDescend(num_1, num_2, num_3, num_top, num_down)
 
def DownAscend(num_1, num_2, num_3, num_top, num_down):
    """If Ascend true"""
    print("%.2f" % num_down + ", " + "%.2f" % num_mid + ", " + "%.2f" % num_top)
 
def TopDescend(num_1, num_2, num_3, num_top, num_down):
    """If Descend True"""
    print("%.2f" % num_top + ", " + "%.2f" % num_mid + ", " + "%.2f" % num_down)

func_1()
