# 2023 KAKAO BLIND RECRUITMENT - 개인정보 수집 유효기간
def solution(today, terms, privacies):
    answer = []
    
    terms2 = [i.split(' ') for i in terms]
    privacies2 = [j.split(' ') for j in privacies]
    today2 = list(map(int, today.split('.')))
    
    for p in range(len(privacies2)):
        i = privacies2[p]
        for j in terms2:
            if i[1] == j[0]:
                year = int(i[0].split('.')[0])
                month = int(i[0].split('.')[1]) + int(j[1])
                day = int(i[0].split('.')[2])
                if month > 12:
                    year += (month-1) // 12
                    month = 12 if month % 12 == 0 else month % 12
            
                if year < today2[0]:
                    answer.append(p+1)
                elif year == today2[0] and month < today2[1]:
                    answer.append(p+1)
                elif year == today2[0] and month == today2[1] and day <= today2[2]:
                    answer.append(p+1)
    
    return answer