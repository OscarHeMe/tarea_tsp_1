import numpy as np
import mpmath as mp
from mpmath import *
from sympy import *
init_printing(use_unicode=True)

def mult (mat1,mat2):
    x=np.matrix(mat1)
    y=np.matrix(mat2)
    r=x*y
    return r

class Cinematica(object):
    """
    Esta clase tiene los atributos theta, distancia en z
    alpha y distancia en x, con los que se puede realizar
    el cálculo numérico de la transformación Denavit-Har-
    tenberg

    Cinematica([['theta1','d1','a1','alpha1'],['theta2','d2','a2','alpha2'],[...]])
    """
    def __init__(self,lista):
        self.juntas=len(lista)
        x=[]
        z=[]
        r=[]
        mat=Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        orig=Matrix(lista)
        for i in range(0,len(lista)):#len(lista)
            if len(lista[i])!=4:
                raise Exception('List must have all [theta, d, a, alpha] elements defined')
            theta, dist_z, dist_x, alpha = orig[i,0], orig[i,1], orig[i,2], orig[i,3]
            tr=Matrix([[cos(theta), -cos(alpha)*sin(theta), sin(alpha)*sin(theta), dist_x*cos(theta)],[sin(theta),cos(alpha)*cos(theta),-sin(alpha)*cos(theta),dist_x*sin(theta)],[0,sin(alpha),cos(alpha),dist_z],[0,0,0,1]])
            mat=mat*tr
            x.append(tr)
            a=mat.col(3)
            b=mat.col(2)
            a.row_del(3)
            b.row_del(3)
            r.append(a)
            z.append(b)
        self.R=r
        self.Z=z
        self.Tr=x
        self.A0n=simplify(mat)

'''
    def compute_dh(self):
        trans=np.matrix([[np.cos(self.theta), -np.cos(self.alpha)*np.sin(self.theta), np.sin(self.alpha)*np.sin(self.theta), self.dist_x*np.cos(self.theta)],[np.sin(self.theta),np.cos(self.alpha)*np.cos(self.theta),-np.sin(self.alpha)*np.cos(self.theta),self.dist_x*np.sin(self.theta)],[0,np.sin(self.alpha),np.cos(self.alpha),self.dist_z],[0,0,0,1]])
        return trans
        '''

    def compute_dh(self):
        trans=np.matrix([[np.cos(self.theta), -np.cos(self.alpha)*np.sin(self.theta), np.sin(self.alpha)*np.sin(self.theta), self.dist_x*np.cos(self.theta)],[np.sin(self.theta),np.cos(self.alpha)*np.cos(self.theta),-np.sin(self.alpha)*np.cos(self.theta),self.dist_x*np.sin(self.theta)],[0,np.sin(self.alpha),np.cos(self.alpha),self.dist_z],[0,0,0,1]])
        return trans

    def compute_jacobian(self, lista):
        '''self.compute_jacobian(list)
        list---> a list with r for rotational joint or t for translational joint
        '''
        r=self.R
        z=self.Z
        cero=Matrix([0,0,0])
        if len(lista)!=self.juntas:
            raise Exception('List must have same number of elements than number of joints')
        M=zeros(6,self.juntas)
        for i in range(0,len(lista)):
            if lista[i]=='r' or lista[i]=='R':
                pc=z[i].cross(r[self.juntas-1]-r[i])
                M[:,i]=z[i].row_insert(0,pc)
            elif lista[i]=='t' or lista[i]=='t':
                M[:,i]=cero.row_insert(0,z[i])
            else:
                raise Exception('List must have r or t characters by elements')
        return M

print(c.__doc__)
T=Cinematica([['theta1','l3','l1',0],['theta2','l4','l2',0],['theta3',0,0,0],[0,'theta4',0,0]])
print(T.A0n)
print()
print(T.Tr)
print()
print(T.Z)
print()
print(simplify(T.R))
m=T.compute_jacobian(['r','r','r','t'])
print()
print(simplify(m))
