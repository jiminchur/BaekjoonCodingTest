import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    
    while n > 0:
        n -= 1
        work = heapq.heappop(works)
        if work == 0:
            break
        heapq.heappush(works, work + 1)
    return sum(work ** 2 for work in works)
