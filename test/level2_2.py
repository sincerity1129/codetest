def solution(s):
    '''
    JadenCase -> 첫 문자 대문자, 그 외 소문자
    
    제한 조건
    s -> 1 ~ 200(숫자, 알파벳, 공백문자), (첫 문자는 숫자 또는 알파벳)
    
    풀이과정
    첫문자를 대문자로 변경하는 방식
    숫자인지 알파벳인지 확인하여 알파벳이면 대문자 변경
    '''
    
    answer = ''
    for word in list(s.split(" ")):
        for idx, string in enumerate(word):
            try:
                if int(string) or idx == 0:
                    answer += string
            except:
                if idx == 0:
                    answer += string.upper()
                    continue
                answer += string.lower()
        answer += " "
    return answer[:-1]

s = "3people unFollowed me"	

solution(s)