# 1. theta(편향)과 w1, w2 (가중치)를 이용한 AND
# def AND(x1, x2):
#     w1, w2, theta = 0.5 , 0.5 , 0.7
#     tmp = x1 * w1 + x2 * w2
#     if tmp <= theta:
#         return print(0)
#     else:
#         return print(1)
# print(AND(0,0))
# print(AND(1,0))
# print(AND(0,1))
# print(AND(1,1))

# 2. np 를 활용한 AND
import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
# print(AND2(0,0))
# print(AND2(1,0))
# print(AND2(0,1))
# print(AND2(1,1))

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) +b
    if tmp <= 0 :
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) +b
    if tmp <= 0 :
        return 0
    else:
        return 1
        
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1, s2)
    return y

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))