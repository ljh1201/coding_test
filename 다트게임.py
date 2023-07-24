def solution(dartResult):
    answer = [0]
    score = 0
    area = {'S':lambda x:x, 'D':lambda x:x**2, 'T':lambda x:x**3}
    
    for idx in range(len(dartResult)):
        dart = dartResult[idx]
        try:
            if dartResult[idx:idx+2] == '10':
                continue
            elif dartResult[idx-1:idx+1] == '10':
                score = int(dartResult[idx-1:idx+1])
            else:
                score = int(dart)
        except:
            if dart in area:
                score = (area[dart])(score)
            elif dart == '*':
                score = answer.pop()*2
                answer.append(answer.pop()*2)
            elif dart == '#':
                score = answer.pop()*(-1)

            answer.append(score)

    return sum(answer)