class Solution:
    def myAtoi(self, s: str) -> int:
        # Define valid characters
        my = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lead = ['-', '+']
        s = s.lstrip()
        if not s:
            return 0
        aux = []
        index = 0
        sign = 1
        if s[index] in lead:
            if s[index] == '-':
                sign = -1
            index += 1

        while index < len(s) and s[index] in my:
            aux.append(s[index])
            index += 1

        if not aux:
            return 0

        st = "".join(aux)
        result = int(st) * sign

        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        
        return result





        
