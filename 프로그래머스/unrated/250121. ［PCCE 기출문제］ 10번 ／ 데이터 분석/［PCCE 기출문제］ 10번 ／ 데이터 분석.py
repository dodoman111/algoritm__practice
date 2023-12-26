def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    temp_answer = []
    for ind, dt in enumerate(data):
        if dt[dic[ext]] <= val_ext:
            temp_answer.append(dt)
    answer = sorted(temp_answer, key=lambda item: item[dic[sort_by]])
    
    return answer