class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "!" + s 
        return res

        # so now I have 5!world5!hello
    def decode(self, s: str) -> List[str]:
        solution, i = [], 0

        while i < len(s):
            temp_i = i
            while s[temp_i] != "!":
                temp_i += 1
                length = int(s[i: temp_i])
            solution.append(s[temp_i + 1 : temp_i + 1 + length])
            i = temp_i + 1 + length
        return solution