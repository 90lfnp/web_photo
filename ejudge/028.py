"""gift iii"""
def count():
    """show most weight 2nd"""
    lap = int(input())
    weight_most = 0
    weight_sec = 0
    for _ in range(lap):
        weight = int(input())
        if weight > weight_most:
            weight_sec = weight_most
            weight_most = weight
        if weight > weight_sec and weight < weight_most:
            weight_sec = weight
    if weight_sec == 0:
        print("Exit")
    else:
        print(weight_sec)


count()

