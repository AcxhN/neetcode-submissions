class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # sorting takes O(nlogn) time 
        for i in range(len(nums)-1): # for loop is O(n)
            if(nums[i] == nums[i+1]):
                return True 
        return False
# so overall O(nlogn) time
# O(n) space complexity because we're just storing a list 

# let nums = [1, 2, 3, 4]
# len(nums) returns 4
# range(len(nums)) returns 0, 1, 2, 3

# then
# i    nums[i]    nums[i+1]
# 0    1          2
# 1    2          3
# 2    3          4
# 3    4          OUT OF BOUNDS 
# hence range(len(nums)-1) for the for loop
# we're done checking after comparing the second last element with the last one 