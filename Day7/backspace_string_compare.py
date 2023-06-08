def backspaceCompare(s, t):
    s_stack = []
    t_stack = []
    for i in s:
        if i == '#' and s_stack:
            s_stack.pop()
            continue
        if i != '#':
            s_stack.append(i)
    for j in t:
        if j == '#' and t_stack:
            t_stack.pop()
            continue
        if j != '#':
            t_stack.append(j)
    return s_stack == t_stack


def main():
    s = "a#c"
    t = "b"
    print(backspaceCompare(s, t))


if __name__ == "__main__":
    main()
