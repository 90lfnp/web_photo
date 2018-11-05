"""weight of chicken"""
def number():
    """input number"""
    number_chicken = 0
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    number_chicken = number_chicken + check(int(input()))
    print(number_chicken)
def check(chicken):
    """check weight"""
    if chicken >= 50 and chicken <= 70:
        return 1
    if chicken < 50 or chicken > 70:
        return 0

number()
