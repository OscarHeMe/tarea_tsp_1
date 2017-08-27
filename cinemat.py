import numpy as np

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

    Cinematica(theta, d, a, alpha)
    """
    def __init__(self, t, d_z, d_x, a):
        self.theta=t
        self.dist_z=d_z
        self.alpha=a
        self.dist_x=d_x

    def compute_dh(self):
        trans=np.matrix([[np.cos(self.theta), -np.cos(self.alpha)*np.sin(self.theta), np.sin(self.alpha)*np.sin(self.theta), self.dist_x*np.cos(self.theta)],[np.sin(self.theta),np.cos(self.alpha)*np.cos(self.theta),-np.sin(self.alpha)*np.cos(self.theta),self.dist_x*np.sin(self.theta)],[0,np.sin(self.alpha),np.cos(self.alpha),self.dist_z],[0,0,0,1]])
        return trans

c=Cinematica(1,3,4,5)
print(c.__doc__)
