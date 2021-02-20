from __future__ import annotations
from math import sqrt
from typing import List
import numpy as np


def oth_proj(v : np.array, u: np.array) -> np.array:
    """
    Calculate the projection of v onto u.
    """
    try: 
        v_pro = np.dot(u, v) / np.sqrt(sum(u**2)) * u
        return v_pro
    except ValueError:
        raise(ValueError)


def oth_proj_to_space(v: np.array, oth_basis: List[np.array]) -> np.array:
    """
    Find the vector project of v onto a vector space.
    The oth_basis should be a list of orthognal vectors.
    """
    try:
        v_pro = oth_proj(v, oth_basis[0])
        for i in range(1, len(oth_basis)):
            try: 
                v_pro += oth_proj(v, oth_basis[i])
            except ValueError:
                print("Dim doesn't match between " + str(i) + "th vector and v")
        return v_pro
    except:
        print("Dim doesn't match between the first vector in the basis and v")


if __name__ == "__main__":
    v = np.array([1/3, 2/3, 2/3])
    u = np.array([1, 1, 1])
    print(oth_proj(u, v))
    
    e_1 = np.array([1, 0, 0])
    e_2 = np.array([0, 1, 0])
    print(oth_proj_to_space(u, [e_1, e_2]))

