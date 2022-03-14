import numpy as np

def inital_state(num_elements):
    base_matrix = np.zeros((num_elements,num_elements))
    first_pos = int(num_elements/2)
    base_matrix[0, first_pos] = 1
    return base_matrix