def is_paired(input_string):
    if not input_string:
        return True
    brac = {"}": "{", "]": "[", ")": "("}
    stack = []
    for char in input_string:
        if char in "{}[]()":
            if char in brac:
                if not stack or stack[-1] != brac[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
    return not stack
