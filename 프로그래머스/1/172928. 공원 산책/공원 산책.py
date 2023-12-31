def direct_loc(direct, n, s_loc):
        if direct == 'E':
            i, j  = s_loc[0], s_loc[1] + n
        elif direct == 'S':
            i, j  = s_loc[0] + n, s_loc[1]
        elif direct == 'W':
            i, j  = s_loc[0], s_loc[1] - n
        else :
            i, j  = s_loc[0] - n, s_loc[1]
        return i, j 
    
def solution(park, routes):
    answer = []
    park_lst = []
    length = len(park)
    width = len(park[0])
    for i, lst in enumerate(park):
        for j, item in enumerate(lst):
            if item == 'S':
                s_loc = (i, j)
                
    for route in routes:
        temp = route.split(" ")
        direct, num = temp[0], int(temp[1])
        if num >= width or num >= length:
            continue
        for n in range(1, num + 1):
            i, j  = direct_loc(direct, n, s_loc)
            
            if i > length-1 or j > width-1 or i < 0 or j < 0:

                print('break', length,width)
                break
            
            if park[i][j] == 'X':
                break
            if n == num:
                s_loc = (i, j)
                
    return list(s_loc)