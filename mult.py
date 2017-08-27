"""-*-Modulo multiplicacion de matrices-*-"""

def mult (mat1,mat2):
    import numpy as np
    x=np.matrix(mat1)
    y=np.matrix(mat2)
    r=x*y
    return r
