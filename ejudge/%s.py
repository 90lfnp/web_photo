"""percent s"""
def function():
    """print text"""
    word = input()
    print("|"+word+"|")
    print("|"+("%10s" % word)+"|")
    print("|"+("%-10s" % word)+"|")
    print("|"+word[:1]+" "+word[0:3]+" "+word[0:5]+"|")
function()
