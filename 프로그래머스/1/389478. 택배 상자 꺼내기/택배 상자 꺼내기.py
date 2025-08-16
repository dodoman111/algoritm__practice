def solution(n, w, num):
    # num의 (row, col) 계산
    r0, pos = divmod(num - 1, w)
    c0 = pos if r0 % 2 == 0 else w - 1 - pos

    rows = (n + w - 1) // w  # 총 행 수
    cnt = 0

    # 자신의 행부터 위쪽(더 큰 row)으로 같은 col에 상자가 있는지 센다
    for r in range(r0, rows):
        L = min(w, n - r * w)  # r행에 실제로 놓인 상자 개수
        if L <= 0:
            break
        if r % 2 == 0:  # 짝수 행: 좌→우
            if c0 < L:
                cnt += 1
        else:           # 홀수 행: 우→좌 (오른쪽 L칸만 유효)
            if c0 >= w - L:
                cnt += 1

    return cnt
