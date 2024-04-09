from collections import Counter
answer = 0
def solution(s):
    '''
    s 문자열에서 x가 첫글자
    x와 x가 아닌 문자 구분
    둘을 나누어서 몇 개로 나누어지는 지 확인
    
    s = "banana" 
    ba / na / na
    
    풀이과정
    무조건 2개씩은 되어야지 분리
    2개 4개 6개 순으로 일치 여부 확인
    재귀 쓰면서 해결하면 좋을 듯
    '''
    def split_word(s, start, end):
        global answer
        if start >= len(s):
            return 0
        elif len(s)-start == 1:
            answer += 1
            return 0    
        word_list = s[start:end]
        word_dict = Counter(word_list)
        
        x_count = word_dict[s[start]]
        non_x_count = sum(count for char, count in word_dict.items()
                          if char != s[start])
        
        if x_count == non_x_count:
            answer += 1
            split_word(s, end, end+2)
        else:
            split_word(s, start, end+2)    
            
        return answer   
          
    answer = split_word(s,0,2)
    return answer


s = "abracadabra"
result = solution(s)
print(result)