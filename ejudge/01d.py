"""surprisingVote"""
def surprising():
    """show surprising if highscore > lowscore = 2"""
    total_score = float(input())
    high_score = float(input())
    remain_score = total_score - high_score
    low_score = remain_score / 2
    differance = high_score - low_score
    if differance > 2 or high_score - abs(remain_score - high_score) > 2:
        print("Surprising")
    else:
        print("Not surprising")

surprising()

