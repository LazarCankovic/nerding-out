class Solution:

    # purpose is to go from ["hello", "world"]
    # to 5!hello5!world
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "!" + s
        return res

    # purpose is to go from 5!hello5!world
    # to ["hello", "world"]
    def decode(self, s: str) -> List[str]:
        solution, i = [], 0

        while i < len(s):
            temp_i = i
            while s[temp_i] != "!":
                temp_i += 1
            len_of_word = int(s[i: temp_i])
            solution.append(s[temp_i + 1 : temp_i + 1 + len_of_word])
            i = temp_i + 1 + len_of_word
        return solution











