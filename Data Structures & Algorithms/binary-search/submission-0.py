class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        right = length - 1
        left = 0

        while nums and left < right:
            middle = (right + left) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1

            

        return left if nums[left] == target else -1



#[-1,0,2,4,6,8]

# middle = 3 (4)
# right = 3 (4)
# left = 2 (2)
# target = 4



