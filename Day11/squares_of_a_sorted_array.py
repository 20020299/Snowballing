def sortedSquares(nums):
    ans = []
    n = len(nums)
    for i in nums:
        tmp = i*i
        ans.append(tmp)
    ans.sort()
    return ans


def main():
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))


if __name__ == "__main__":
    main()
