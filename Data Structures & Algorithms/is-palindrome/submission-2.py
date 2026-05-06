class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringng = ""
        for c in s:
            if c.isalnum():
                stringng += c.lower()
        return stringng == stringng[::-1]