def is_correct_bracket_seq(sequence):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for bracket in sequence:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return False
        else:
            return False

    return len(stack) == 0


input = input("Введите строку \n")
print(is_correct_bracket_seq(input))