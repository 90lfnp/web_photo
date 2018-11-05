"""SceneSwitch I"""
def switch():
    """find time warm light"""
    second0 = 0
    warm_count = 0
    while True:
        second1 = input()
        if second1 == "End":
            break
        second1 = float(second1)
        if second1 - second0 == 0:
            stat = "cool"
        if stat == "cool":
            if second1 - second0 > 0:
                stat = "off"
                second0 = second1
        elif stat == "off":
            if second1 - second0 <= 6:
                stat = "warm"
                second0 = second1
                warm_count += 1
            else:
                stat = "cool"
                second0 = second1
        elif stat == "warm":
            if second1 - second0 > 0:
                stat = "offcool"
                second0 = second1
        elif stat == "offcool":
            if second1 - second0 > 0:
                stat = "cool"
                second0 = second1


    print(warm_count)

switch()
