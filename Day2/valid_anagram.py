def validAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    else:
        return False


def main():
    s = "rat"
    t = "car"
    print(validAnagram(s, t))


if __name__ == "__main__":
    main()
