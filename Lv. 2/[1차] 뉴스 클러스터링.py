def solution(str1, str2):
    answer = 0
    n1, n2 = [], []
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            n1.append(str1[i] + str1[i+1])
            
    for j in range(len(str2)-1):
        if (str2[j] + str2[j+1]).isalpha():
            n2.append(str2[j] + str2[j+1])
            
    n1_c = n1.copy()
    n2_c = n2.copy()
    
    for k in n1:
        if k in n2_c:
            answer += 1
            n1_c.remove(k)
            n2_c.remove(k)
            
    if len(n1)+len(n2)-answer == 0:
        return 65536
    
    return int(answer/(len(n1)+len(n2)-answer)*65536)