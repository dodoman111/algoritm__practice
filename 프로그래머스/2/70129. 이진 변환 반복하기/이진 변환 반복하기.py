def solution(s):
    cnt, bin_cnt = 0, 0
    while s!='1':
        bin_cnt += s.count('0')
        cnt += 1
        s = bin(s.count('1'))[2:]
    return [cnt,bin_cnt]