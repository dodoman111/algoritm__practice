from itertools import permutations 

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons,len(dungeons)):
        temp = 0
        temp_k = k 
        for j in range(len(dungeons)):
            if temp_k >= i[j][0]:
                temp_k -= i[j][1]
                temp += 1 
        if temp > answer:
            answer = temp
            
    return answer