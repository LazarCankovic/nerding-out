class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(word)
        return list(my_dict.values())
        