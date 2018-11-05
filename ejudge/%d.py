"""percent d"""
def function():
    """print num"""
    num = input()
    print("|"+num+"|")
    print("|"+"+"+num+"|")
    print("|"+("%10d" % int(num))+"|")
    print("|"+("%-10d" % int(num))+"|")
    print("|"+("%05d" % int(num))+"|")
function()

