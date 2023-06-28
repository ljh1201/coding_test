def solution(new_id):
    answer = ' '
    recom_id = list(new_id.strip('.').lower())
    check = ['-','_','.'] + [chr(a) for a in range(97, 123)] + [f'{i}' for i in range(0, 10)]
    for r in range(len(recom_id)):
        if recom_id[r] in check and recom_id[r] + answer[-1] != '..':
            answer += recom_id[r]
    answer = answer.replace(' ', '').strip('.')

    if len(answer) > 15:
        answer = answer[:15]

    answer = answer.strip('.')

    while len(answer) < 3:
        try:
            answer += answer[-1]
        except:
            answer += 'a'

    return answer