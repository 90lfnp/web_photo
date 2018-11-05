"""00D: regulation"""
def trans():
    """tranform word"""
    integer_a = int(input())
    floating_b = float(input())
    string_c = input()
    print("%30d" % (integer_a))
    print("%030d" % (integer_a))
    print("%.2f" % (floating_b))
    print("%.12f" % (floating_b))
    print("%40s" % (string_c))

trans()
