import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        new = x + y*2
        heapq.heappush(scoville, new)
        cnt += 1

    return cnt