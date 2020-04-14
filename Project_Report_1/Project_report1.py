# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:35:35 2020

@author: Himanshu and Jamie

Project report 1 5044 Statistical Estimation
Spring 2020
"""

import numpy as np
import scipy.linalg as sp

## contants
L = 0.5
dt = 0.1

x0 = np.transpose(np.array([10,0,np.pi/2, 60,0,-np.pi/2
        
        ]))

##Initialize linearized CT system

A = np.array([
        [0,0,-2,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,12],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])

B = np.array([
        [0,0,0,0],
        [1,0,0,0],
        [np.tan(-np.pi/18)/L, 2/(L*np.cos(-np.pi/18)**2), 0,0],
        [0,0,0,0],
        [0,0,-1,0],
        [0,0,0,1]
        ])

C = np.array([
        [0,1/70,-1,0,-1/70,0],
        [1,0,0,-1,0,0],
        [0,1/70,0,0,-1/70,-1],
        [0,0,0,1,0,0],
        [0,0,0,0,1,0]
        ])

D = 0

Ga = np.eye(6)

## discretize system

F = np.eye(6) + dt*A

G = dt*B

H = C

M = D

## Noise Matrices
Om = dt*Ga #multiply by process noise vector

V = np.eye(5) #multiply by measurement noise vector

##we do not yet have information to calculate Rd or Qd for kalman filtering.

## Observability of the system

#construct observability gramian
temp = H

O_ = temp

for i in range(0,5):
    temp = np.matmul(temp,F)
    O_ = np.concatenate((O_, temp))

#print the rank of the observability gramian
print (np.linalg.matrix_rank(O_))

## Stability 
eigs = np.linalg.eig(F)
print (max(eigs[0]))
    
#construct nxnr matrix, curlyC
    
temp = G

curlyC = temp

for i in range(0,5):
    temp= np.matmul(F,G)
    curlyC = np.hstack((curlyC, temp))

#print the rank of curlyC
print (np.linalg.matrix_rank(np.transpose(curlyC)))