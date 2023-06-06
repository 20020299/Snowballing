from collections import Counter


def majorityElement(nums):
    c = Counter(nums)
    n = len(nums)
    t = n // 2
    for count in c.keys():
        if c[count] > t:
            print(count)


def main():
    nums = [2,2,1,1,1,2,2]
    majorityElement(nums)


if __name__ == "__main__":
    main()