"""inflation"""
def increase_money():
    """input money ,year and print fv_money"""
    money = float(input())*100
    year = int(input())
    for _ in range(year):
        money = int((money * 10000) + (money * 381)) // 10000
    print("%01d.%02d" %  (money//100, money%100))

increase_money()
