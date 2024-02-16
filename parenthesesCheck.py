from stack import Stack


def parenthesesCheck(exp: str) -> bool:
    digits = exp.split()
    s = Stack(len(exp))
    for char in exp:
        if char == '(':
            s.Push(char)
        elif char == ')':
            if len(s):
                s.pop()
            else:
                return False
    return len(s) == 0
