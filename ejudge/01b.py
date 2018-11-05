"""Circular I"""
def circle():
    """check radar"""
    core_x_me = float(input())
    core_y_me = float(input())
    mosq_machine = float(input())
    core_x_mosq = float(input())
    core_y_mosq = float(input())
    point_mosq = (((core_x_mosq - core_x_me)**2) + ((core_y_mosq - core_y_me)**2))**0.5
    if point_mosq <= mosq_machine:
        print("Yes")
    else:
        print("No")

circle()
