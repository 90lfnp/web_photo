"""check score"""
def show_result():
    """print result"""
    score = core_function(float(input()))
    print(score)
    print("Process is terminated")
def core_function(marks):
    """
    return 1 if you passed the exam
           0 is failed
    """
    if marks >= 450:
        return when_passsed()
    else:
        return when_failed()
def when_passsed():
    """
    return string words "Pass"
    """
    return "Pass"
def when_failed():
    """
    return string words "Fail"
    """
    return "Fail"

show_result()
