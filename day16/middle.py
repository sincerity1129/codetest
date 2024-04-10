def solution(s):
    '''
    (), [], {} 모두 올바른 괄호 문자열
    A가 올바른 괄호 문자열 -> (A), [A], {A} 올바른 문자
    A, B가 올바른 괄호 문자열 -> AB 올바른 괄호 문자
    {}, ([]) 올바른 괄호 문자열 -> {}([]) 올바른 괄호 문자
    
    s -> "[](){}" // "[](){}", "(){}[]", "{}[]()"
    s ->  "}]()[{" // "()[{}]", "[{}]()"
    s ->  "[)(]" // 괄호를 만들 수가 없음
    
    풀이과정 
    총 27가지 경우의 수가 나오고 이를 replace로 제거 하면 될 듯
    '''
    # all_case = [
    # "[{()}]", "[(())]", "[[()]]", "[{[]}]", "[([])]", "[[[]]]", "[{{}}]", "[({})]", 
    # "[[{}]]", "{[()]}", "{(())}", "{{()}}", "{[{}]}", "{({})}", "{{{}}}", "{[[]]}", 
    # "{([])}", "{{[]}}", "({()})", "([()])", "((()))", "({{}})", "([{}])", "(({}))", 
    # "({[]})", "([[]])", "(([]))", "[{}]", "[()]", "[[]]", "{[]}", "{()}", "{{}}",
    # "({})", "([])", "(())", "[]", "{}", "()"
    # ]

    # answer = 0
    # for idx in range(len(s)):
    #     tmp = s[idx:] + s[:idx]
    #     for case in all_case:
    #         tmp = tmp.replace(case, "")
    #         if tmp == "":
    #             break
    #     if tmp == "":
    #         answer += 1
    
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == '[' and s[i] == ']': stack.pop()
                elif stack[-1] == '{' and s[i] == '}': stack.pop()
                elif stack[-1] == '(' and s[i] == ')': stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))
    return answer

s = "({[]})"
solution(s)