"""Bring me some water"""
def function():
    """print bottle of water"""
    water = int(input())
    waterall = water
    if water % 5 >= 2:
        waterb = water // 5
        watterl = waterall - (waterb*5)
        print(waterb)
        waters = waterl // 2
        print(waters)
function()
