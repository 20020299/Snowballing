from collections import Counter


def containDuplicate(nums):
    c = Counter(nums)
    n = len(nums)
    for count in  c.values():
        if count >= 2:
            return True
        else:
            return False


def main():
    nums = [1, 2, 3, 4]
    print(containDuplicate(nums))


if __name__ == "__main__":
    main()

