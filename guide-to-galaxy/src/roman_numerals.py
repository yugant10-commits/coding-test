class RomanNumerals:
    CURRENCY = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self):
        pass

    @staticmethod
    def check_roman_basic_symbols(roman_string:list)->bool:
        all_legal_symbols = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        if not roman_string or not all(c in all_legal_symbols for c in roman_string):
            return False
        else:
            return True

    @staticmethod
    def check_roman_repeat_rules(roman_string: list)->bool:
        can_never_be_repeated = ('D', 'L', 'V')
        can_be_repeated = ('I', 'X', 'C', 'M')
        MAX_REPEAT_COUNT_I = 3
        MAX_REPEAT_COUNT_X = 4 # this can only be repeated for 4 times while it's 'XXXIX'
        MAX_REPEAT_COUNT_C = 4 # this can only be repeated for 4 times while it's 'CCCXC'
        MAX_REPEAT_COUNT_M = 4 # this can only be repeated for 4 times while it's 'MMMCM'

        for item in can_never_be_repeated:
            if roman_string.count(item) > 1:
                return False
        if roman_string.count('I') > MAX_REPEAT_COUNT_I:
            return False
        if roman_string.count('X') > MAX_REPEAT_COUNT_X \
            or (roman_string.count('X') == 4 and 'XXXIX' not in roman_string):
            return False
        if roman_string.count('C') > MAX_REPEAT_COUNT_C \
            or (roman_string.count('C') == 4 and 'CCCXC' not in roman_string):
            return False
        if roman_string.count('M') > MAX_REPEAT_COUNT_M \
            or (roman_string.count('M') == 4 and 'MMMCM' not in roman_string):
            return False
        
        return True

    @staticmethod
    def check_roman_subtract_rules(roman_string :list)->bool:
        """Checks the following subtraction rules.
        1. I can be subtracted from V and X only.
        2. X can only be subtracted from L and C only.
        3. C can be subtracted from D and M only.
        4. V, L, D can never be subtracted.
        Parameters
        ----------
        roman_string : list
            [A list containing the user input but converted roman string.]

        Returns
        -------
        bool
            [True if the rule stands false otherwise.]
        """

        can_be_subtracted_from = { 'C': {'D', 'M'}, 'I': {'V', 'X'}, 'X': {'L', 'C'} }
        can_never_be_subtracted = ('V', 'L', 'D')
        last_subtract_roman = 0 
        last_arabic_value = 9999 # the last generated arabic value
        current_arabic_value = 0
        i = 0
        while i < len(roman_string):
            # the last symbol does not need to check with the subtract rules
            if (i < len(roman_string) - 1) and \
                RomanNumerals.CURRENCY[roman_string[i]] \
                    < RomanNumerals.CURRENCY[roman_string[i+1]]:
                # if the after symbol is bigger than the before one, meaning there's a subtract:
                if roman_string[i] in can_never_be_subtracted:
                    return False
                if roman_string[i+1] not in\
                     can_be_subtracted_from[roman_string[i]]:
                    return False
                current_arabic_value = RomanNumerals.CURRENCY[roman_string[i+1]]\
                     - RomanNumerals.CURRENCY[roman_string[i]]
                if current_arabic_value > last_arabic_value:
                    return False
                if last_subtract_roman != 0 and \
                    current_arabic_value + last_arabic_value >= last_subtract_roman:
                    return False
                else:
                    last_subtract_roman = RomanNumerals.CURRENCY[roman_string[i+1]]
                    last_arabic_value = current_arabic_value
                    i = i + 2 # skip the subtract one
            # if it's the last symbol or it's not followed by a bigger symbol
            else:
                current_arabic_value = RomanNumerals.CURRENCY[roman_string[i]]
                if current_arabic_value > last_arabic_value:
                    return False
                if last_subtract_roman != 0 and \
                    current_arabic_value + last_arabic_value >= last_subtract_roman:
                    return False
                else:
                    last_arabic_value = current_arabic_value
                    last_subtract_roman = 0
                    i = i + 1
            
        return True

    @staticmethod
    def check_roman(roman_string: list)->bool:
        return RomanNumerals.check_roman_basic_symbols(roman_string) \
            and RomanNumerals.check_roman_repeat_rules(roman_string) \
            and RomanNumerals.check_roman_subtract_rules(roman_string)


    @staticmethod
    def to_arabic(symbols: list)->int:
        """Checks if the given list of strings follow the standard rules.
        Computes the given value with the rules specified.

        Parameters
        ----------
        symbols : list
            [a list of strings]

        Returns
        -------
        int
            [a computed integer]
        """
        if not RomanNumerals.check_roman(symbols):
            return None
        numbers = [ RomanNumerals.CURRENCY[s] for s in symbols ]

        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                numbers[i] = -numbers[i]
        
        return sum(numbers)