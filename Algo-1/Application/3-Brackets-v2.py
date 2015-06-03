def is_expression_valid(data):
    digits = "0123456789"
    brackets = []

    if data[0] in digits:
        return False

    if data[0] == '{' and data[-1] != '}':
        return False

    if data[0] == '{' and data[-1] == '}':
        if '{' in data[1:-1] or '}' in data[1:-1]:
            return False
        is_here = False
        for i in data:
            if i == "(" and is_here is False:
                return False
            if i == '[':
                is_here = True
            if i == ']':
                is_here = False

    if '{' in data[1:-1] or '}' in data[1:-1]:
            return False

    for i in data:
        if i in digits:
            continue
        else:
            brackets.append(i)

    if len(brackets) % 2 != 0:
        return False

    for i in range(0, len(brackets)):
        if brackets[i] == '(':
            for j in range(i + 1, len(brackets)):
                if brackets[j] == ')':
                    if '{' in brackets[i:j] or '}' in brackets[i:j]:
                        return False
                    if '[' in brackets[i:j] or ']' in brackets[i:j]:
                        return False
                    if '(' in brackets[i + 1:j] or ')' in brackets[i:j - 1]:
                        return False
                if brackets[j] == '(':
                    break
        if brackets[i] == '[':
            for j in range(i + 1, len(brackets)):
                if brackets[j] == ']':
                    if '{' in brackets[i:j] or '}' in brackets[i:j]:
                        return False
                    if '[' in brackets[i + 1:j] or ']' in brackets[i:j]:
                        return False
                if brackets[j] == '[':
                    break
    counter = 0
    length = 0

    for i in brackets:
        length += 1
        if i == '(' or i == '[' or i == '{':
            counter += 1
        if i == ')' or i == ']' or i == '}':
            counter -= 1
        if counter == 0 and length != len(brackets):
            return False

    return True


def main():

    while True:

        expression = input("Enter an expression: ")

        if is_expression_valid(expression):
            print("True")
        else:
            print("NO")


if __name__ == '__main__':
    main()
