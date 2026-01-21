while(True):
    sentence = input()
    if sentence == ".":
        break
    stack = []
    balance = True
    for i in sentence:
        if i == "(":
            stack.append(")")
        elif i == "[":
            stack.append("]")
        elif i == ")" or i == "]":
            if stack:
                if stack.pop() != i:
                    balance = False
                    break
            else:
                balance = False
                break
    print("yes" if not stack and balance else "no")
