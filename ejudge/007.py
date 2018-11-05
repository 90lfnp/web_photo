"""cal math"""
def func1():
    """cal"""
    var_x = int(input())
    math1 = var_x
    func2(math1)
    math2 = var_x+5
    func2(math2)
    math3 = var_x-17
    func2(math3)
    math4 = var_x*32
    func2(math4)
    math5 = ((5*(var_x**2))+(10*5*var_x)+3)
    func2(math5)
def func2(out):
    """print output"""
    print(out)

func1()

