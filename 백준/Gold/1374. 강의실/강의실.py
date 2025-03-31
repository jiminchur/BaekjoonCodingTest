import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
lectures = []

for _ in range(N):
    # 강의 번호는 사용하지 않으므로 시작시간과 종료시간만 저장합니다.
    _, start, end = map(int, input().split())
    lectures.append((start, end))

# 강의 시작시간 기준으로 정렬
lectures.sort(key=lambda x: x[0])

# 최소 힙을 사용하여 현재 진행 중인 강의의 종료시간을 저장합니다.
heap = []
max_rooms = 0

for start, end in lectures:
    # 현재 강의의 시작 시간보다 이전에 끝난 강의가 있다면, 해당 강의실은 재사용할 수 있습니다.
    while heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    max_rooms = max(max_rooms, len(heap))

print(max_rooms)