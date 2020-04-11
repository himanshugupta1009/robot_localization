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

## discretize system

Ahat = np.hstack((A,B))
Ahat = np.concatenate((Ahat, np.zeros((4,10)) ))

eat = sp.expm(Ahat*dt)

F = eat[0:6,0:6]

G = eat[0:6,-4:]

H = C

M = D

## Noise Matrices
W = np.eye(6) #multiply by process noise vector

V = np.eye(5) #multiply by measurement noise vector

##we do not yet have information to calculate Rd or Qd for kalman filtering.

