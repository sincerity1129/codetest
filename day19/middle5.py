def solution(answers):
    '''
    수학 문제를 찍음
    수포자는 총 3명
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    가장 많이 맞힌 순서대로 배열 담아서 return 
    
    조건
    시험문제 -> 최대 만 문제
    정답 -> 1,2,3,4,5 중 하나
    높은 점수 여럿일 때 오름차순
    
    예시
    answers = [1,2,3,4,5]
    student1이 가장 높은 정답
    
    풀이 과정
    3명의 최소 공배수 값을 리스트에 담아줌
    student1 -> 5, student2 -> 8, student1 -> 10
    문제 수 + 1 만큼 반복 늘려줌
    '''
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    student1_length, student2_length, student3_length = len(answers) // len(student1) + 1, len(answers) // len(student2) + 1, len(answers) // len(student3) + 1
    std_answer= [0,0,0]
    for std1,std2,std3, ans in zip(student1*student1_length, student2*student2_length, student3*student3_length, answers):
        if std1 == ans:
            std_answer[0] += 1
        if std2 == ans:
            std_answer[1] += 1
        if std3 == ans:
            std_answer[2] += 1
    
    max_std = 0
    answer = []
    for idx, std in enumerate(std_answer):
        if std > max_std:
            answer = [idx+1]
            max_std = std
        elif std == max_std:
            answer.append(idx+1)
            max_std = std
    return answer

answers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
solution(answers)