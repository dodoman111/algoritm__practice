def solution(s):
    a =  []
    for i in range(len(s)) :
        if s[i] =='(':
            a.append(s[i])
        if s[i] ==')':
            if len(a)==0 :
                return False
            else : 
                a.pop(-1)
    if len(a) == 0:
        return True
    else : 
        return False