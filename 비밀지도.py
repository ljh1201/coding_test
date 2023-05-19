def solution(n, arr1, arr2):
    answer = []
    pwd = ''
    
    for i in range(n):
        _list = list(format(arr1[i] | arr2[i], 'b'))
        for j in _list:
            pwd += '#' if j == '1' else ' ' 
            
        while len(pwd) < n:
                pwd = ' ' + pwd  
        answer.append(pwd)
        pwd = ''
        
    return answer