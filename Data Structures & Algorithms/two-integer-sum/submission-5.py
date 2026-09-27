# two pointer second try
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intuition: 
            # two pointer method
            # problems:
                # i need to sort for this two pointer approach, but I need to return original indices
                    # I'll pair each value with its index before sorting, so i still have original indices after sorting 
                # recognize problem contraints: "return the answer with the smaller index first"
        
        pairs = sorted(enumerate(nums), key=lambda pair: pair[1])
        # high level explanation:
            # enumerate runs, returns a sequence of tuples 
            # sorted calls your key function on each tuple to figure out what to sort by 
                # key basically tells sort: "for each item, ask the key function what vlaue to actually compare, then sort based off those results"
            # sorted returns a new, ordered list which is then assigned to pairs 

        # enumerate(nums) returns a sequence of tuples (index, element), ...
        # sorted(...) sorts the sequence of tuples based on the lambda function 
        # if we didn't use a lambda function it would look like this:
            # def get_value(pair):
            #    return pair[1]
            # pairs = sorted(enumerate(nums), key=get_value)
        # so sorted calls the function you give it via key:
            # get_value((index, element)), and does that for all tuples 
        # sorted() is going to call this lambda once for every item coming out of enumerate(nums)

        i = 0
        j = len(pairs)-1
        while i < j:
            sum = pairs[i][1] + pairs[j][1]
            if sum == target:  
                return sorted([pairs[i][0], pairs[j][0]]) # to "return the answer with the smaller index first"
            elif sum > target:  
                j-=1
            elif sum < target: 
                i+=1