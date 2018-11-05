"""timig II"""
def time():
    """calculate time"""
    sec = int(input())
    minu = sec//60
    sec %= 60
    hou = minu//60
    minu %= 60
    day = hou//24
    hou %= 24
    if day > 9999:
        print("ERR_:__:__:__")
    if day <= 9999:
        print("%04d:%02d:%02d:%02d" % (day, hou, minu, sec))

time()
