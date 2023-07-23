def solution(N, stages):
    answer = []
    fail = []
    player = len(stages)

    for i in range(1, N+1):
        if player == 0:
            fail.append([i, 0])
        else:
            fail.append([i, stages.count(i) / player])
        player -= stages.count(i)
    
    for j in sorted(fail, key=lambda x:x[1], reverse=True):
        answer.append(j[0])

    return answer