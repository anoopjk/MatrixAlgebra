# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 06:50:42 2017

@author: Anoop
"""

"""cholesky factorization"""
import numpy as np
from scipy import random



def pos_semidef_generator(matrix_size):
    A = random.rand(matrix_size, matrix_size)
    A = np.dot(A,A.T)
    return A

matrix_size = 10
A = pos_semidef_generator(matrix_size)
#A = np.array([[18, 22, 54, 42], [22, 70, 86, 62], [54, 86, 174, 134], [42, 62, 134, 106]]) #np.array([[25, 15, -5], [15, 18, 0], [-5, 0, 11]])
L = np.zeros((A.shape))  #cholesky factor lower triangular matrix





for i in range(A.shape[0]):

    for k in range(A.shape[1]):
        diagonalterm = 0
        lowerdiagterm = 0
        for j in range(k): 
            if k<i:
                #lower diagonal part
                lowerdiagterm += L[i,j]*L[k,j]
                print "lowerdiagterm: ", lowerdiagterm
            elif k==i:
                #diagonal part
                diagonalterm += np.square(L[k,j])
                print "diagonalterm: ", diagonalterm
        if k < i:                
            L[i,k] = (1.0/L[k,k])*(A[i,k]- lowerdiagterm )
        
        elif (i == k):
            L[i,k] = np.sqrt(A[i,k] - diagonalterm)
            
print "original matrix, A: ", A       
print "cholesky factor, L: ", L       
        

