def well_formed(s):
    stack = []
    open_parentheses = '('
    closed_parentheses = ')'
    open_curly_bracket = '{'
    closed_curly_bracket = '}'
    open_square_bracket = '['
    closed_square_bracket = ']'
    for char in s:
        if char == open_curly_bracket or char == open_square_bracket or char == open_parentheses:
            if len(stack) != 0:
                if stack[-1] == char:
                    continue
            stack.append(char)
            continue
        if char == closed_square_bracket:
            bracket = stack.pop()
            if bracket == open_square_bracket:
                return True
            else:
                stack.append(bracket)
        if char == closed_curly_bracket:
            bracket = stack.pop()
            if bracket == open_curly_bracket:
                return True
            else:
                stack.append(bracket)
        if char == closed_parentheses:
            bracket = stack.pop()
            if bracket == open_parentheses:
                return True
            else:
                stack.append(bracket)
    return False


s = '[(){}'
print(well_formed(s))