class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman_to_int_mapper = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        i = 0
        while i < len(s):
            if  i + 1 < len(s) and s[i:i+2] in roman_to_int_mapper:
                num += roman_to_int_mapper.get(s[i:i + 2] , 0)
                i += 2
                continue

            num += roman_to_int_mapper[s[i]]
            i += 1
            
        return num
