class Solution:
    def compress(self, chars: List[str]) -> int:
        read_i = 0
        set_i = 0

        while (read_i < len(chars)):
            letter = chars[read_i]
            count = 0
            while (read_i < len(chars) and chars[read_i] == letter):
                read_i += 1
                count += 1

            chars[set_i] = letter
            set_i += 1
            print (f'add char {read_i} {letter} {set_i} {count}')

            if (count > 1):
                for i in str(count):
                    chars[set_i] = i
                    set_i += 1

        return set_i
