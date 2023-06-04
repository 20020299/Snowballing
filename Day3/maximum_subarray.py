def maximumSubarray(nums):
    n = len(nums)
    max_now = nums[0]
    max_ending = 0

    for i in range(0, n):
        max_ending = max_ending + nums[i]
        if max_ending < 0:
            max_ending = 0
        elif max_now < max_ending:
            max_now = max_ending

    return max_now


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximumSubarray(nums))


if __name__ == "__main__":
    main()
