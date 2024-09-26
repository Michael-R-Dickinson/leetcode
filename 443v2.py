class Solution:
    def compress(self, chars: List[str]) -> int:
        read_i = 0
        set_i = 0
        count = 0

        while True:
            count += 1
            if (read_i == 0 or chars[read_i] != chars[read_i - 1]):
