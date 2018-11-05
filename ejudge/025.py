"""grade iii"""
def grade():
    """input grade"""
    count = int(input())
    grade_all = 0
    for _ in range(count):
        score = cal_grade(float(input()))
        grade_all += score
    grade_aver = grade_all / count
    print("%.4s" % str("%.3f" % (grade_aver)))

def cal_grade(score):
    """calculate grade"""
    calculate_grade = 0
    if score >= 95 and score <= 100:
        calculate_grade = 4
    elif score >= 90 and score < 95:
        calculate_grade = 3.5
    elif score >= 85 and score < 90:
        calculate_grade = 3
    elif score >= 80 and score < 85:
        calculate_grade = 2.5
    elif score >= 75 and score < 80:
        calculate_grade = 2
    elif score >= 70 and score < 75:
        calculate_grade = 1.5
    elif score >= 65 and score < 70:
        calculate_grade = 1
    elif score >= 60 and score < 65:
        calculate_grade = 0.5
    elif score >= 0 and score < 60:
        calculate_grade = 0
    return calculate_grad

grade()
