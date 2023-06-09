from collections import Counter


def singleNumber(nums):
    c = Counter(nums)
    n = len(nums)
    for count in c.keys():
        if c[count] == 1:
            print(count)


def main():
    nums = [4, 1, 2, 1, 2]
    singleNumber(nums)


if __name__ == "__main__":
    main()
