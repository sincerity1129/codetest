def solution(progresses, speeds):
    '''
    진도 -> 100% 서비스 반영
    progresses -> 배포되어야 하는 순서대로 정수 배열 
    speeds -> 각 작업의 개발 속도가 적힌 정수 배열
    각 배포마다 몇 개의 기능이 배포 되는지
    progresses, speeds 길이 -> 100개 이하
    progresses -> 1 ~ 99
    speeds -> 1 ~ 100
    
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    앞에 있는 순서대로 배포되어야 배포 가능
    
    풀이 과정
    전체 배열에서 앞에 있는 것 기준으로 값을 적용
    100이 넘는 경우에 값을 빼고 카운트
    이런 식으로 여러번 진행
    '''
def solution(progresses, speeds):
    def performance_rate(progresses, speeds, answer, day):
        if len(progresses) == 0:
            return 0
        
        work_cnt = 0
        while True:
            if progresses[0]+(speeds[0]*day) >= 100:
                for progress, speed in zip(progresses, speeds):
                    if progress+(speed*day) < 100:
                        break
                    work_cnt += 1
                answer.append(work_cnt)
                break
            day += 1
            
        performance_rate(progresses[work_cnt:], speeds[work_cnt:], answer, day)
        return answer
    
    answer = []
    day = 1
    answer = performance_rate(progresses, speeds, answer, day)
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
answer = solution(progresses, speeds)
print(answer)