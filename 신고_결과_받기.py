def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dic = {_id:[0] * len(id_list) for _id in id_list}
    report_set = set()

    for rp in report:
        if rp in report_set:
            continue
        else:
            report_set.add(rp)
        
        A, B = rp.split()
        id_dic[B][id_list.index(A)] += 1

    for i in id_list:
        if sum(id_dic[i]) >= k:
            for j in range(len(id_list)):
                answer[j] += id_dic[i][j]
        
    return answer
