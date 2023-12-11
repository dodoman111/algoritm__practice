def solution(s):
    max_num = 0
    length = len(s)
    for i in range(length):
        for j in range(length,i,-1):
            temp = s[i:j]
            if temp == temp[::-1]:
                temp_num = len(temp)
                if temp_num > max_num:
                    max_num = temp_num
    return max_num