# survey = ["AN", "CF", "MJ", "RT", "NA"]	
# choices = [5, 3, 2, 7, 5]	
# result = "TCMA"
survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
result = "RCJA"
# 성격 유형은 총 4개의 지표로 구성(16개조합)
# R,T // C,F // J,M // A,N
# survey -> 두글자로 된 문자열 데이터
# chices -> 선택지 결과 어떤 걸 택했는지
# 지표 번호 기준으로 작성
# [RT, CF, JM, AN]

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# chices = [5, 3, 2, 7, 5]

# 1번 질문 -> 5번 선택 N + 1
# 2번 질문 -> 3번 선택 C + 1
# 3번 질문 -> 2번 선택 M + 2
# 4번 질문 -> 7번 선택 T + 3
# 5번 질문 -> 5번 선택 A + 1


# A = N, C > F, M > J, R < T
# ANCMT이나 지표 순으로 나열 및 동점 시 알파벳 우선
# result = "TMCA"    
    
    
score_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
personality_types = ["RT", "CF", "JM", "AN"]
personality_score = [3,2,1,0,1,2,3]

for personality_type, choice in zip(survey, choices):
    if choice < 4:
        score_dict[personality_type[0]] += personality_score[choice-1]
    else:
        score_dict[personality_type[1]] += personality_score[choice-1]


for personality_type in personality_types:
    if score_dict[personality_type[0]] > score_dict[personality_type[1]]:
        del score_dict[personality_type[1]]
    elif score_dict[personality_type[1]] > score_dict[personality_type[0]]:
        del score_dict[personality_type[0]]
    else:
        personality_type_sorted = sorted(personality_type)
        del score_dict[personality_type_sorted[1]]

 
result_type = "".join([s for s in score_dict.keys()])

print(result_type)


    