def solution(s):
    '''
    s -> 문자열
    각단어는 하나 이상의 공백문자, 각 단어의 짝수번째 대문자, 홀수번째 소문자
    짝/홀은 인덱스가 아니라 공백 기준
    s = "try hello world"
    result = "TrY HeLlO WoRlD"
    
    풀이과정
    s를 공백 기준으로 split
    for문 통해서 문자열 빼서 적용
    '''
    word_list = s.split(" ")
    answer = []
    for idx, word in enumerate(word_list):
        new_word = []
        for idx, alphabet in enumerate(word):
            if idx == 0:
                new_word.append(alphabet.upper())
                continue
            elif idx % 2 == 0:
                new_word.append(alphabet.upper())
                continue
            new_word.append(alphabet.lower())
        answer.append("".join(new_word))
    return " ".join(answer)

s = "try hello world"
answer = solution(s)
print(answer)