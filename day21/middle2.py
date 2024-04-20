def solution(today, terms, privacies):
    '''
    약관 동의 얻어 수집된 1 ~ n
    특정 유효기간 지난 다음날 파기
    모든 달은 28일 까지
    
    예시
    (유효기간) -> A(6달), B(12달), C(3달)
    번호(약관종류, 개인정보 수집 일자) -> 
    1(A, 2021.05.02), 2(B, 2021.07.01), 3(C, 2022.02.19), 4(C, 2022.02.20)
    오늘 날짜 -> 2022.05.19
    1 -> 2021.11.01까지 유효
    2 -> 2022.06.28까지 유효
    3 -> 2022.05.18까지 유효
    4 -> 2022.05.19까지 유효 
    [1,3] 파기
    
    today -> 오늘 날짜
    terms -> 약관의 유효기간(길이 1 ~ 20),(약관 종류와 유효기간은 공백으로 구분),
            (A~Z 대문자), (약관 종류 중복X), (유효기간 1 ~ 100)
    privacies -> 개인정보의 정보를 담은 1차원 배열(길이 1 ~ 100),
            (날짜와 약관 종류는 공백으로 구분)
            
    풀이과정
    날짜를 어떻게 다루는지가 관건인 문제
    12월 지나면 1월이 되어야 하고, 일이 01로 끝날 경우 28일까지 허용으로 인정
    먼저 년도 -> 월 -> 일 순으로 파기 여부 판단해서 결과 값
    
    일단 테스트 케이스에서는 오류가 나지 않는데 실제 제출 시 실패
    다른 풀이 접근 필요할 듯
    먼저 했던 접근은 년, 월, 일로 나눠서 해결했는데 조건 주는 과정에서 미스가 있었던 듯
    근데 생각의 전환하는 게 어렵긴 함...
    2000<= year <=2022 // 1<= month <=12 // 1<= day <= 28
    
    today = 2022.05.19 -> 2022 / 05 / 19
    privacies = 2021.05.02 // A -> 2021 / 05 + A(06) / 02 - 01 == 2021 / 11 / 01
    변경할 때 제약 사항
    2022.01.01 -->  2021.12.28
    만료일 기준으로 하루 빼주면 day: 01 -> 28, month: 01 -> 12, year: 2022 -> 2021  
    만료기한이 6개월 --> 2022.06.28
    day: 28 -> 28, month: 12 -> 6, year: 2021 -> 2022
    '''
    
#     terms_dict = {term.split(" ")[0]:int(term.split(" ")[1]) for term in terms}
#     year, month, day = today.split(".")
    
#     answer = []
#     expired_year, expired_month, expired_day = 0,0,0
#     for idx, privace in enumerate(privacies):
#         date, term_sort = privace.split(" ")
#         now_year, now_month, now_day = date.split(".")
        
#         if now_day == "01":
#             expired_day = "28"
#             if now_month == "01":
#                 now_year, now_month = int(now_year)-1, "12"
#             else:
#                 now_month = int(now_month) - 1
#         else:
#             expired_day = int(now_day) - 1
            
#         if int(now_month)+terms_dict[term_sort] > 12:
#             expired_year = int(now_year) + (int(now_month)+terms_dict[term_sort]) // 12
#             if (int(now_month)+terms_dict[term_sort]) % 12 == 0:
#                 expired_month = 12
#             else:
#                 expired_month = (int(now_month)+terms_dict[term_sort]) % 12
            
#         else:
#             expired_year = int(now_year)
#             expired_month = (int(now_month)+terms_dict[term_sort]) % 12
        
#         if int(year) > int(expired_year):
#             answer.append(idx+1)
#         elif int(month) > int(expired_month):
#             answer.append(idx+1)
#         elif int(day) > int(expired_day):
#             answer.append(idx+1)

    terms_dict = {term.split(" ")[0]:int(term.split(" ")[1]) for term in terms}
    year, month, day = today.split(".")
    expired_year, expired_month, expired_day = 0,0,0
    
    answer = []
    for idx, privace in enumerate(privacies):
        # 년, 월, 일로 나눠주기
        date, term_sort = privace.split(" ")
        now_year, now_month, now_day = date.split(".")
        
        # 만료기한 날짜 생각 안하고 정하기 
        expired_year = int(now_year)
        expired_month = int(now_month) + terms_dict[term_sort]
        expired_day = int(now_day) - 1
        
        # 날짜 기준으로 변경
        # 일자 변경
        if expired_day == 0:
            expired_day = 28
            expired_month = expired_month - 1
        # 월 및 년도 변경
        if expired_month > 12:
            expired_year += expired_month//12
            expired_month %= 12
        if expired_month == 0:
            expired_month = 12
            
        # 만료기한 비교하기
        if int(year) > expired_year:
            answer.append(idx+1)
        elif int(year) == expired_year and int(month) > expired_month:
            answer.append(idx+1)
        elif int(year) == expired_year and int(month) == expired_month and int(day) > expired_day:
            answer.append(idx+1)
    return answer

today="2022.05.19"
terms=["A 6", "B 12", "C 3"]
privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# today = "2020.01.01"
# terms = ["Z 3", "D 12"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

today="2020.12.17"
terms=["A 12"]
privacies=["2010.01.01 A", "2019.12.17 A"]

solution(today, terms, privacies)