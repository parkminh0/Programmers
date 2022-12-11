def solution(n, words):
    answer = []
    for i in range(n):
        answer.append([])
        
    idx = 1
    tmp = [words[0]]
    answer[0].append(words[0])
    for j in range(1, len(words)):
        answer[idx % n].append(words[j])
        tmp.append(words[j])
        if tmp.count(words[j]) == 2 or tmp[-2][-1] != words[j][0]:
            return[(idx % n)+1, answer[idx%n].index(words[j])+1]
        idx += 1
        
    return [0, 0]