"""the function within"""
def function():
    """input number"""
    vara = float(input())
    varb = float(input())
    varc = float(input())
    vard = float(input())
    ansfff = funcff(funcff(vara))
    ansffg = funcfg(funcff(vara - varb))
    ansffh = funcfh(funcff(vara+varb), funcff(vara+varc), funcfg(funcff(vard**2)))
    ansffi = funcfi(funcfh(funcff(vara+varb), funcff(vara-varc), funcfg(funcff(vard**2))), \
        funcfg(funcff(vara-varb)), funcff(funcff(funcff(funcff(funcff(varc))))), vard**8)
    print(ansfff)
    print(ansffg)
    print(ansffh)
    print(ansffi)
def funcff(varx):
    """cal f(x)"""
    return varx*2
def funcfg(varx):
    """cal f(g)"""
    return (3*(varx**4))-(varx**3)+(2*(varx**2))+10
def funcfh(varx, vary, varz):
    """cal f(h)"""
    return ((varz+varx)**2)-(varx*vary)+(vary**2)
def funcfi(vara, varb, varc, vard):
    """cal f(i)"""
    return ((vara**2)+(varb**2)-(varc**2))/((vard**2)-(2*vara*vard)+(2*vara))

function()
