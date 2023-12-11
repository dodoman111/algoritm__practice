def solution(s):
    lst = list(map(lambda x: int(x),s.split()))
    return f'{min(lst)} {max(lst)}'