def validParentheses(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        if i == ")":
            count -= 1
        if i == "[":
            count += 2
        if i == "]":
            count -= 2
        if i == "{":
            count += 3
        if i == "}":
            count -= 3
    if count != 0:
        return False
    else:
        return True


def main():
    s = "(]"
    print(validParentheses(s))


if __name__ == "__main__":
    main()
