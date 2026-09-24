class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# sorted(...) goes through the thing you gave it one at a time like a for loop would, 
# it collects those items into a new list, sorts that list, and returns the list 

# i.e.
    # sorted([3, 1, 2])      [1, 2, 3]
    # sorted("cat")          ['a', 'c', 't']
    # sorted({5, 2, 9})      [2, 5, 9]

# in python, == commpares contents element by element like std::vector in cpp,
# recall for raw c arrays:
    # int a[] = {1, 2, 3};
    # int b[] = {1, 2, 3};
    # a == b;   // false!
# because the arrays turn into pointers to their first element when used like this, so == compares memory addresses, no the contents 