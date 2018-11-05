"""001:grade I"""
def grade():
    """print pass if you pass"""
    score = float(input())
    if score >= 60:
        print("Pass")
    if score < 60:
        print("Fail")

grade()

