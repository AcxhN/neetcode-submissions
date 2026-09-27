class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen: 
                # seen[difference] is always an earlier index than i, so with this we will always return the answer with the smaller index first 
                return [seen[difference], i] 
            
            seen[nums[i]] = seen.get(nums[i], i)