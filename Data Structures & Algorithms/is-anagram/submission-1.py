class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if strings are diffrent size, they can't be anagrams 
            return False 
        
        s1_count = {}
        for i in s: # loop through string s, for each character increase count by 1 in hashmap 
            s1_count[i] = s1_count.get(i, 0)+1
        for i in t: # loop through string t, for each character decrease count by 1 in hashmap 
            s1_count[i] = s1_count.get(i, 0)-1 
            if s1_count[i] < 0: # if any count drops below 0, it's not anagram 
                return False 
        return True # strings are same length, so we would have returned false if not anagram, at this point it must be an anagram 

# O(n) time, O(n) space 
# alternative, more intuitive hashmap solution is to build two seperate dicts,
# one counting the chars of each string, 
# then check whether two dicts are equal with ==,
# Python compares dicts by their key/value pairs,
# so {"a": 2, "b": 1} equals {"b": 1, "a": 2} regardless of the order the keys were added