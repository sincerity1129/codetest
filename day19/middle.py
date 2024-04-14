def solution(k, scores):
    '''
    매일 1명의 가수, 문자 투표
    매일 출연한 가수의 점수는 지금까지 출연 가수들의 점수 중 상위 k번째면 명예의 전당
    k일 다음부터 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 높으면
    출연 가수의 점수가 명예의 전당에 오름
    기존의 k번째 순위의 점수는 명예의 전당 내려옴
    
    k = 3, score = [10, 100, 20, 150, 1, 100, 200]
    k가 3이므로 3번째 값이 발표 값이므로
    10, 10, 10, 20, 20, 100, 100
    
    풀이 과정
    k를 기준으로 리스트 값을 채움
    k값을 넘어가면 가장 마지막 값을 제거하는 방식으로 리스트 유지
    정렬해서 가장 첫번째 값을 result 뽑아내는 방식
    '''
    answer = []
    score_list = []
    for score in scores:
        score_list.append(score)
        if len(score_list) <= k:
            score_list = sorted(score_list)
            answer.append(score_list[0])
        elif len(score_list) > k:
            score_list = sorted(score_list)
            score_list.remove(score_list[0])
            answer.append(score_list[0])
    return answer