import heapq

def solution(scoville,K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            cnt = 0
            break
        if len(scoville) <=1 and scoville[0]<K:
            cnt = -1
            break
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            c = a + 2*b
            heapq.heappush(scoville,c)
            cnt += 1
            if scoville[0] >= K : 
                break
    return cnt