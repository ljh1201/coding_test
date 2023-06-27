def solution(survey, choices):
    answer = ''
    mbti = {'RT':0,'CF':0,'JM':0,'AN':0}
    for idx in range(len(survey)):
        cho = choices[idx] - 4
        if survey[idx] in mbti:
            mbti[survey[idx]] += cho
        else:
            survey[idx] = survey[idx][1] + survey[idx][0]
            mbti[survey[idx]] -= cho

    for i, j in mbti.items():
        if j <= 0:
            answer+=i[0]
        else:
            answer+=i[1]

    return answer
