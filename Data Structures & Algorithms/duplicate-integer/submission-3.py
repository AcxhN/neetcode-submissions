class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen: # O(1) lookup
                return True  
            seen[i] = True # O(1) insert 
        return False 
# space is O(n) because worst case you store the entire list, like for no duplicate 