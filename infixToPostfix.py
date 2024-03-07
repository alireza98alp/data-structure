from stack import Stack


def infixToPostFix(exp: str) -> str:
    """convert infix expression to postfix
    and return the answer as string"""
    s = Stack(maxsize=(len(exp)))
    ans = ''
    for char in exp:
        match char:
            case '(':
                s.push(char)
            case '*' | '/':
                while ((tmp := s.top()) in {'*', '/'}):
                    ans += tmp
                    s.pop()
                s.push(char)
            case '+' | '-':
                while (tmp := s.top()) in {'*', '/', '+', '-'}:
                    ans += tmp
                    s.pop()
                s.push(char)
            case ')':
                while (tmp := s.top()) != '(':
                    ans += tmp
                    s.pop()
                s.pop()
            case _:
                ans += char
    if len(s) > 0:
        ans += s.pop()
    return ans
