# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg


def create_matrix():
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print("m={}\nm.T={}\nm.I={}\n".format(m, m.T, m.I))

    print("")

if __name__ == "__main__":
    create_matrix()
