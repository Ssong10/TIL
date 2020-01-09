import numpy as np
print('#1 2차원 배열')
X = np.array([[51,55],[14,19],[0,4]])
print(X)
print('0행')
print(X[0])
print('0행 1열')
print(X[0][1])

print('#1 1차원 배열')
X = X.flatten() # X를 1차원 배열로 변환
print(X)
print('0,2,4 인덱스 접근')
print(X[np.array([0,2,4])])

print('#2 조건문 필터링')
# 특정 조건을 만족하는 원소만
print(X>15) # boolean 형 값으로 나오게 된다
print(X[X>15])