"""Circular II"""
def circle():
    """check area overlap"""
    point_x_me = float(input())
    point_y_me = float(input())
    r_mosq_machine_me = float(input())
    point_x_f = float(input())
    point_y_f = float(input())
    r_mosq_machine_f = float(input())
    line_me_to_f = (((point_x_f - point_x_me)**2) + ((point_y_f - point_y_me)**2))**0.5
    r_mosq_machine_me_and_f = r_mosq_machine_me + r_mosq_machine_f
    if line_me_to_f < r_mosq_machine_me_and_f:
        print("Yes")
    else:
        print("No")

circle()
