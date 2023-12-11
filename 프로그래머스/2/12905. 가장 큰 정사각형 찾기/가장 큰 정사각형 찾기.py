import numpy as np

def solution(board):
    array = np.array(board)
    ni,nj= array.shape[0], array.shape[1]
    for i in range(1,ni):
        for j in range(1,nj):
            if array[i,j] == 1:
                point = min(array[i-1,j-1], array[i-1,j], array[i,j-1])
                if  point >=1:
                    array[i,j] = point + 1
    return int(np.max(array)) ** 2