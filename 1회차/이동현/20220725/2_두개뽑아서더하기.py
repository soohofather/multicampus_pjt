# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for ii in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[ii])
            answer = sorted(list(set(answer)))
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))