def solution(name, yearning, photo):
    answer = []
    dic = {nm:yearn for nm, yearn in zip(name, yearning)}
    for lst in photo:
        score = 0
        for nm in lst:
            if nm in dic:
                score += dic[nm]
        answer.append(score)
    return answer