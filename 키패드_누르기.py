def solution(numbers, hand):
    answer = ''
    keypad = {1:[0,0],2:[0,1],3:[0,2],
              4:[1,0],5:[1,1],6:[1,2],
              7:[2,0],8:[2,1],9:[2,2],
              '*':[3,0],0:[3,1],'#':[3,2]}
    
    R = keypad['#']
    L = keypad['*']
    for num in numbers:
        if num % 3 == 1:
            L = keypad[num]
            answer += 'L'
        elif num % 3 == 0 and num > 0:
            R = keypad[num]
            answer += 'R'
        else:
            key = keypad[num]
            R_dist = abs(key[0] - R[0]) + abs(key[1] - R[1])
            L_dist = abs(key[0] - L[0]) + abs(key[1] - L[1])
            if R_dist < L_dist:
                R = keypad[num]
                answer += 'R'
            elif R_dist > L_dist:
                L = keypad[num]
                answer += 'L'
            else:
                if hand == 'right':
                    R = keypad[num]
                    answer += 'R'
                else:
                    L = keypad[num]
                    answer += 'L'

    return answer
