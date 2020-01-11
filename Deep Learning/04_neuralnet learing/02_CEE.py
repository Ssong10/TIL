# 교차 엔트로피 오차
# cross entropy error
import numpy as np

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

t = [0,0,1,0,0,0,0,0,0,0]
## 2일 확률이 가장 높을떄
y = [0.1, 0.05, 0.6 , 0.0 , 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
a  = cross_entropy_error(np.array(y),np.array(t))
print(a)
## 7일 확률이 가장 높을때
y = [0.1, 0.05, 0.1 , 0.0 , 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
b = cross_entropy_error(np.array(y),np.array(t))
print(b)