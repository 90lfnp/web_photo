"""weight station"""
def weight():
    """find weight at point 4"""
    average = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight4 = (average*4) - weight1 - weight2 - weight3
    all_weight = weight1 + weight2 + weight3 + weight4
    half_average = average / 2
    minn_weight = average - half_average
    maxx_weight = average + half_average
    if all_weight > 15000:
        print("Overweight")
    if all_weight <= 15000:
        if weight1 < minn_weight or weight1 > maxx_weight or \
        weight2 < minn_weight or weight2 > maxx_weight or \
        weight3 < minn_weight or weight3 > maxx_weight or \
        weight4 < minn_weight or weight4 > maxx_weight:
            print("Unbalance")
        if weight1 > minn_weight and weight1 < maxx_weight and \
        weight2 > minn_weight and weight2 < maxx_weight and \
        weight3 > minn_weight and weight3 < maxx_weight and \
        weight4 > minn_weight and weight4 < maxx_weight:
            print("Pass "+("%.2f" % (weight4)))

weight()

