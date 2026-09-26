# two pointer method, first try

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer method only works on sorted arrays but we have to return the indices of the given list
        # create a list of tuples [(index, element), ...]
        # example: say pairs = [(0, 3), (1, 2), (2, 4)]
        #   pairs[0]        # → (0, 3), the tuple at position 0 in the list pairs 
        #   pairs[0][0]     # → 0, the element at the 0th index of the tuple at the 0th index of list pairs
        #   pairs[0][1]     # → 3, the element at the 1st index of the tuple at the 0th index of list pairs
        pairs = []
        for i in range(len(nums)):
            pairs.append((i, nums[i]))
        
        # now we sort the array by the elements of the original array 
        # and because of what we did earlier we know the original index after sorting 
        pairs.sort(key=lambda pair: pair[1])
        # How do you sort by the element? since we have [(index, element), ...]
            # Python needs to compare (0, 3), (1, 2), and (2, 4) to figure out sort order
            # Instead of comparing the tuples directly, it runs each one through your lambda first: 
                # pair[1] on (0, 3) → 3; on (1, 2) → 2; on (2, 4) → 4
            # now it sorts [3, 2, 4] then applies that order to the original tuples in the list 
            # result: [(1, 2), (0, 3), (2, 4)] — sorted by pair[1]
        # Note 1:
            # .sort(key=...) 
                # tells python "run my function, and use the return value to sort"
            # sort(key=lamba ...)
                # lambda in Python is a way of writing a tiny throwaway function in one line, without formally naming it with def, it's called an anonymous function 
                # so 
                    # lambda pair: pair[1]
                # is the same as writing this out as a normal named function:
                    # def get_value(pair):
                    # return pair[1]
                # they do the same thing: given an input, return its element at the 1st index 
        # Note 2: 
            # without key: Python's default .sort() on a list of tuples compares the first element of each tuple first. So if we created pairs = [(element, index), ...] instead we could just do pairs.sort()
            # but lambda is very useful, so learn 

        # two pointer method 
        i = 0
        j = len(pairs)-1
        while i < j:
            if pairs[i][1] + pairs[j][1] == target:
                return sorted([pairs[i][0], pairs[j][0]]) # need to sort for negative numbers 
            elif pairs[i][1] + pairs[j][1] > target:
                j-=1
            elif pairs[i][1] + pairs[j][1] < target:
                i+=1
        raise ValueError("No two numbers sum to target")