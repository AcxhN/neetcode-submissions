class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = {}
        result = []

        for word in strs:
            temp = "".join(sorted(word))
            if not temp in signatures:
                signatures[temp] = [word]
            else:
                signatures[temp].append(word)
                
        return list(signatures.values())
        # does same thing as
            #for group in signatures.values():
            #    result.append(group)
            #return result 