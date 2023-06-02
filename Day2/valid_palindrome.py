import re


def validPalindrome(s):
    s = s.lower()
    s = re.sub(r'[\W_]', '', s)
    tmp = s[::-1]
    if s == tmp :
        return True
    else:
        return False


def main():
    s = "race a car"
    print(validPalindrome(s))


if __name__ == "__main__":
    main()
