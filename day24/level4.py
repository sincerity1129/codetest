from collections import defaultdict
def solution(id_list, report, k):
    '''
    불량 이용자 신고 처리 메일 발송 시스템
    한 번에 한 명의 유저 신고 가능(신고 횟수 제한X)
    한 유저 여러 번 신고 -> 1회 신고
    k번 이상 신고된 유저 -> 게시판 이용 정지, 신고한 모든 유저에 메일 발송
    
    제한사항
    id_list 길이 -> 2 ~ 1000
    id_list 원소 길이 -> 1 ~ 10(알파벳 소문자, 아이디 중복X)
    report 길이 -> 1 ~ 20만
    report 원소 길이 -> 3 ~ 21("muzi frodo" -> muzi가 frodo 신고, 알파벳 소문자, 자기신고X)
    k의 길이 -> 1 ~ 200(자연수)
    유저가 받은 결과 메일 수 담기
    
    예시
    id_list=["muzi", "frodo", "apeach", "neo"]
    report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k=2
    
    frodo -> [muzi, apeach]
    neo -> [frodo, muzi]
    muzi -> 2 // frodo -> 1 // apeach -> 1 // neo -> 0 [2,1,1,0]
    
    풀이과정
    defaultdict 활용해서 두 개의 딕셔너리로 카운트 하면될 듯
    report에서 신고당한 사람을 key 나머지를 리스트 value로 dict 만들기
    대신 중복 비허용
    카운트 할 수 있는 dict 만들어서 카운트 후에 값 넣으면 될 듯
    '''
    
    report_dict = defaultdict(list)
    count_dict = defaultdict(int)
    
    for people in report:
        reporter, reported = people.split(" ")
        if reporter not in report_dict[reported]:
            report_dict[reported].append(reporter)
    
    for reporte, reporter in report_dict.items():
        if len(report_dict[reporte]) >= k:
            for person in reporter:
                count_dict[person] += 1
                
    answer = []
    for id in id_list:
        answer.append(count_dict[id])
    return answer

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

result=solution(id_list, report, k)

print(result)