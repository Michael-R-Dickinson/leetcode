class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c: str):
            return c.lower() in ['a', 'e', 'i', 'o', 'u']

        new = list(s)

        left = 0
        right = len(s) - 1
        while left < right:
            if not isVowel(s[right]):
                right -= 1
            if not isVowel(s[left]):
                left += 1

            if isVowel(s[left]) and isVowel(s[right]):
                new[left], new[right] = s[right], s[left]
                right = 1
                left += 1

        return ''.join(new)
