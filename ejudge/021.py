"""Runner"""
def repeat(word, number):
    """print 'word' 'number' line"""
    for _ in range(number):
        print(word)
 
repeat(input(), int(input()))