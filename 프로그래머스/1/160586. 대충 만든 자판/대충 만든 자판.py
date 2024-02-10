def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        flag = False
        for word in target:
            temp = 101
            for key in keymap:
                if word in key:
                    temp = min(key.index(word) + 1 ,temp)
            if temp == 101 :
                flag = True
            cnt += temp
        if flag:
            cnt = -1
        answer.append(cnt)
    return answer