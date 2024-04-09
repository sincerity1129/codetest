def solution(s, n):
    '''
    AB -> 1을 밀면 -> BC // -> 3을 밀면 -> DE
    z -> 1을 밀면 -> a
    '''
    upper_case_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    
    answer = ''
    for alphabet in s:
        if alphabet.isupper():
            index = (upper_case_alphabets.index(alphabet)+n)%26
            alphabet = upper_case_alphabets[index]     
        elif alphabet.islower():
            index = (lower_case_alphabets.index(alphabet)+n)%26
            alphabet = lower_case_alphabets[index]
            
        answer+= alphabet
    return answer

s="a B z"
n=4
answer = solution(s, n)
print(answer)
	