import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

X = np.array([1.0,0.5]) # ( 2, ) 값
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) # (2,3 ) 가중치
B1 = np.array([0.1,0.2,0.3])  # (3, ) 편향

A1 = np.dot(X,W1) + B1
print('A1 출력값', A1)  
Z1 = sigmoid(A1)
print('A1 시그모이드', Z1)

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2) + B2
print('A2 출력값',A2)
Z2 = sigmoid(A2)
print('A2 시그모이드',Z2)

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])
A3 = np.dot(Z2, W3) + B3
print('A3 출력값',A3)
Z3 = sigmoid(A3)
print('A3 시그모이드',Z3)