import numpy as np
A = np.array([[1,2],[3,4],[5,6]])
# 차원수
print(np.ndim(A))

# 3*2 배열
print(A.shape)

# 행렬의 곱
# (2*2) * (2*2)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))

# (2,3) * (3,2) = (2,2)
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])
print(np.dot(A,B))