def get_max_pairwiser(nums):
    nums.sort()
    return nums[-1] * nums[-2]