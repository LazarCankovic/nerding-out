class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            # gives me the sorted word together as a key
            # so that even for the next word if the key is the same,
            # I can append it to the values
            key = "".join(sorted(word))
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(word)
        return list(my_dict.values())
