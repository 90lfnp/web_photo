"""calculate time"""
def func1():
    """calculate time"""
    sec = int(input())
    minu = sec//60
    sec %= 60
    hou = minu//60
    minu %= 60
    day = hou//24
    hou %= 24
    print(str(day)+" "+str(hou)+" "+str(minu)+" "+str(sec))

func1()
