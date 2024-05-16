import heapq

def solution(jobs):
    jobs.sort()
    count, last, answer = 0, -1, 0
    wait = []
    time = jobs[0][0]
    
    while count < len(jobs):
        for job in jobs:
            if last < job[0] <= time:
                heapq.heappush(wait, (job[1], job[0]))
        if len(wait) > 0:
            current = heapq.heappop(wait)
            last = time
            time += current[0]
            answer += (time - current[1])
            count += 1
        else:
            time += 1
    return int(answer / len(jobs))
