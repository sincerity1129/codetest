import numpy as np
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
answer = np.dot(np.array(arr1),np.array(arr2))

print(answer.tolist())