import numpy as np

def inital_state(num_elements):
    base_matrix = np.zeros((num_elements, num_elements+2))
    first_pos = int(num_elements/2)
    base_matrix[0, first_pos] = 1
    return base_matrix

def rule_30(control):
    if (control == np.array([1, 1, 1])).all():
        return 0
    elif (control == np.array([1, 1, 0])).all():
        return 0
    elif (control == np.array([1, 0, 1])).all():
        return 0
    elif (control == np.array([1, 0, 0])).all():
        return 1
    elif (control == np.array([0, 1, 1])).all():
        return 1
    elif (control == np.array([0, 1, 0])).all():
        return 1
    elif (control == np.array([0, 0, 1])).all():
        return 1
    elif (control == np.array([0, 0, 1])).all():
        return 0











