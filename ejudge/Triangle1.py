"""Triangle I"""
def triangle():
    """cul triangle with wood Yes or No"""
    wood_1 = float(input())
    wood_2 = float(input())
    wood_3 = float(input())
    wood_min = min(wood_1, wood_2, wood_3)
    wood_max = max(wood_1, wood_2, wood_3)
    wood_mid = (wood_1 + wood_2 + wood_3) - (wood_max + wood_min)
    include = (wood_min** 2) + (wood_mid** 2)
    infront = wood_max** 2
    if abs(infront - include) < 0.01:
        print("Yes")
    else:
        print("No")

triangle()
