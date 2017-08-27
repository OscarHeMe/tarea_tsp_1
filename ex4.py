"""ex4"""
#Cinematica class importation
from cinemat import Cinematica
import numpy as np

#parameters definition
t1=0
t2=np.pi/2
t3=-np.pi/2
t4=2
l1=1
l2=1
l3=2
l4=1

v1=Cinematica(t1,l3,l1,0)
v2=Cinematica(t2,l4,l2,0)
v3=Cinematica(t3,t4,0,0)

mat1=v1.compute_dh()
mat2=v2.compute_dh()
mat3=v3.compute_dh()

origen=np.matrix([[0],[0],[0],[1]])

T1=mat1*mat2*mat3*origen
print(T1)
