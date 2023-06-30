def solution(board, moves):
    answer = 0
    board.reverse()
    board2 = [[] for _ in range(len(board))]
    hold = []
    for b in board:
        for i in range(len(b)):
            if b[i] != 0:
                board2[i].append(b[i])

    for m in moves:
        m -= 1
        if board2[m]:
            h = board2[m].pop()
            if len(hold) > 0 and hold[-1] == h:
                hold.pop()
                answer += 2
            else:
                hold.append(h)

    return answer