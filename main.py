import numpy as np
import matplotlib.pyplot as plt


def initial_state(num_elements):
    base_matrix = np.zeros((num_elements, num_elements+2))
    first_pos = int(num_elements/2+1)
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
    elif (control == np.array([0, 0, 0])).all():
        return 0
    else:
        print("array is not defined return none")
        return None


def strip_ends(matrix):
    index = [0, -1]
    return np.delete(matrix, index, 1)


def create_matrix(size):
    base_matrix = initial_state(size)
    for row in range(size-1):
        base_matrix[row]
        for col in range(1, size+1):
            control = base_matrix[row][col-1:col+2]
            base_matrix[row+1, col] = rule_30(control)
    return strip_ends(base_matrix)


def visualize(matrix):
    plt.matshow(matrix)
    plt.show()









