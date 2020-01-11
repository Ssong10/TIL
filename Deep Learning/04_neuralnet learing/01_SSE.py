# 오차 제곱 합
# sum squares error

import numpy as np
def sum_squares_error(y,t):
    return 0.5 * np.sum((y-t)**2)

t = [0,0,1,0,0,0,0,0,0,0]
## 2일 확률이 가장 높을떄
y = [0.1, 0.05, 0.6 , 0.0 , 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
a  = sum_squares_error(np.array(y),np.array(t))
print(a)
## 7일 확률이 가장 높을때
y = [0.1, 0.05, 0.1 , 0.0 , 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
b = sum_squares_error(np.array(y),np.array(t))
print(b)