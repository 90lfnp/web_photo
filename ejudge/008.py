"""calculate math"""
def func1():
    """input"""
    varx = int(input())
    vary = int(input())
    varz = int(input())
    ansfx = funcfx(varx)
    ansfy = funcfy(vary)
    ansfz = funcfz(varz)
    ansfxy = funcfxy(varx, vary)
    ansfxyz = funcfxyz(varx, vary, varz)
    print(ansfx)
    print(ansfy)
    print(ansfz)
    print(ansfxy)
    print(ansfxyz)
def funcfx(var_x):
    """cal functionx"""
    return var_x+1
def funcfy(var_y):
    """cal functiony"""
    return (7*(var_y**3))+(2*(var_y**2))-(31*var_y)+1
def funcfz(var_z):
    """cal functionz"""
    return var_z*(-1)
def funcfxy(var_x, var_y):
    """cal functionxy"""
    return (var_x+var_y)*(var_x-var_y)
def funcfxyz(var_x, var_y, var_z):
    """cal functionxyz"""
    return ((var_y)-(((var_y**2)-(4*var_x*var_z))**0.5))/(2*var_x)

func1()

