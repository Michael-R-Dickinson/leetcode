class Solution:
    def compress(self, chars: List[str]) -> int:
        set_i = 0
        pointer_i = 0
        count = 0

        while True:
            count += 1
            if ((finish:= len(chars) == (pointer_i + 1)) or chars[pointer_i + 1] != chars[pointer_i]):
                chars[set_i] = chars[pointer_i]
                set_i += 1
                if (count != 1):
                    chars[set_i + 1] = count
                    set_i += 1

                if (finish):
                    continue

            pointer_i += 1
