"""
Challenge: Convert figures to words:
1367 -> "One thousand three hundred and sixty seven"

18934345 -> "Eighteen million nine hundred and thirty four thousand three hundred and forty five"

You can assume that the numbers are below 1 trillion and must be positive integers.

1st solution: english numbering system
2nd solution: indian numbering system (lakh, crore)
"""

def figureToWords(figure: int) -> str:
    if len(str(figure)) > 12:
        return "Figure too large, must be less than 1 trillion"
    if len(str(figure)) == 0:
        return "Figure cannot be empty"
    if figure < 0:
        return "Figure must be a positive integer"
    else:
        if figure == 0:
            return "Zero"
        else:
            return capitalizeFirstLetterOnly(twelveDigitConvertor(figure))

def singleDigitConvertor(digit: int) -> str:
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return units[digit]
def twoDigitConvertor(digits: int) -> str:
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if digits < 10:
        return singleDigitConvertor(digits)
    elif 10 <= digits < 20:
        return teens[digits - 10]
    else:
        ten_part = tens[digits // 10]
        unit_part = units[digits % 10]
        if unit_part:
            return f"{ten_part} {unit_part}"
        else:
            return ten_part
def threeDigitConvertor(digits: int) -> str:
    if digits < 100:
        return twoDigitConvertor(digits)
    else:
        hundred_part = singleDigitConvertor(digits // 100) + " Hundred"
        rest = digits % 100
        if rest:
            return f"{hundred_part} and {twoDigitConvertor(rest)}"
        else:
            return hundred_part
def fourDigitConvertor(digits: int) -> str:
    if digits < 1000:
        return threeDigitConvertor(digits)
    else:
        thousand_part = singleDigitConvertor(digits // 1000) + " Thousand"
        rest = digits % 1000
        if rest:
            return f"{thousand_part} {threeDigitConvertor(rest)}"
        else:
            return thousand_part
def fiveDigitConvertor(digits: int) -> str:
    if digits < 10000:
        return fourDigitConvertor(digits)
    else:
        ten_thousand_part = twoDigitConvertor(digits // 1000) + " Thousand"
        rest = digits % 1000
        if rest:
            return f"{ten_thousand_part} {threeDigitConvertor(rest)}"
        else:
            return ten_thousand_part
def sixDigitConvertor(digits: int) -> str:
    if digits < 100000:
        return fiveDigitConvertor(digits)
    else:
        hundred_thousand_part = threeDigitConvertor(digits // 1000) + " Thousand"
        rest = digits % 1000
        if rest:
            return f"{hundred_thousand_part} {threeDigitConvertor(rest)}"
        else:
            return hundred_thousand_part
def sevenDigitConvertor(digits: int) -> str:
    if digits < 1000000:
        return sixDigitConvertor(digits)
    else:
        million_part = singleDigitConvertor(digits // 1000000) + " Million"
        rest = digits % 1000000
        if rest:
            return f"{million_part} {sixDigitConvertor(rest)}"
        else:
            return million_part
def eightDigitConvertor(digits: int) -> str:
    if digits < 10000000:
        return sevenDigitConvertor(digits)
    else:
        ten_million_part = twoDigitConvertor(digits // 1000000) + " Million"
        rest = digits % 1000000
        if rest:
            return f"{ten_million_part} {sixDigitConvertor(rest)}"
        else:
            return ten_million_part
def nineDigitConvertor(digits: int) -> str:
    if digits < 100000000:
        return eightDigitConvertor(digits)
    else:
        hundred_million_part = threeDigitConvertor(digits // 1000000) + " Million"
        rest = digits % 1000000
        if rest:
            return f"{hundred_million_part} {sixDigitConvertor(rest)}"
        else:
            return hundred_million_part
def tenDigitConvertor(digits: int) -> str:
    if digits < 1000000000:
        return nineDigitConvertor(digits)
    else:
        billion_part = singleDigitConvertor(digits // 1000000000) + " Billion"
        rest = digits % 1000000000
        if rest:
            return f"{billion_part} {nineDigitConvertor(rest)}"
        else:
            return billion_part
def elevenDigitConvertor(digits: int) -> str:
    if digits < 10000000000:
        return tenDigitConvertor(digits)
    else:
        ten_billion_part = twoDigitConvertor(digits // 1000000000) + " Billion"
        rest = digits % 1000000000
        if rest:
            return f"{ten_billion_part} {nineDigitConvertor(rest)}"
        else:
            return ten_billion_part
def twelveDigitConvertor(digits: int) -> str:
    if digits < 100000000000:
        return elevenDigitConvertor(digits)
    else:
        hundred_billion_part = threeDigitConvertor(digits // 1000000000) + " Billion"
        rest = digits % 1000000000
        if rest:
            return f"{hundred_billion_part} {nineDigitConvertor(rest)}"
        else:
            return hundred_billion_part 
def capitalizeFirstLetterOnly(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:].lower()
        
def test_figureToWords():
    print("Testing figureToWords()...", end='')
    assert(figureToWords("") == "Figure cannot be empty")  # Empty input
    assert(figureToWords(-5) == "Figure must be a positive integer")  # Negative input
    assert(figureToWords(1000000000000) == "Figure too large, must be less than 1 trillion") # Too large input
    assert(figureToWords(0) == "Zero")
    assert(figureToWords(5) == "Five")
    assert(figureToWords(10) == "Ten")
    assert(figureToWords(32) == "Thirty two")
    assert(figureToWords(99) == "Ninety nine")
    assert(figureToWords(100) == "One hundred")
    assert(figureToWords(101) == "One hundred and one")
    assert(figureToWords(500) == "Five hundred")
    assert(figureToWords(600) == "Six hundred")
    assert(figureToWords(999) == "Nine hundred and ninety nine")
    assert(figureToWords(1000) == "One thousand")
    assert(figureToWords(1001) == "One thousand one")
    assert(figureToWords(1101) == "One thousand one hundred and one")
    assert(figureToWords(1110) == "One thousand one hundred and ten")
    assert(figureToWords(1500) == "One thousand five hundred")
    assert(figureToWords(1567) == "One thousand five hundred and sixty seven")
    assert(figureToWords(10000) == "Ten thousand")
    assert(figureToWords(12345) == "Twelve thousand three hundred and forty five")
    assert(figureToWords(100000) == "One hundred thousand")
    assert(figureToWords(123456) == "One hundred and twenty three thousand four hundred and fifty six")
    assert(figureToWords(1000000) == "One million")
    assert(figureToWords(1234567) == "One million two hundred and thirty four thousand five hundred and sixty seven")
    assert(figureToWords(10000000) == "Ten million")
    assert(figureToWords(12345678) == "Twelve million three hundred and forty five thousand six hundred and seventy eight")
    assert(figureToWords(100000000) == "One hundred million")
    assert(figureToWords(123456789) == "One hundred and twenty three million four hundred and fifty six thousand seven hundred and eighty nine")
    assert(figureToWords(1000000000) == "One billion")
    assert(figureToWords(1234567890) == "One billion two hundred and thirty four million five hundred and sixty seven thousand eight hundred and ninety")
    assert(figureToWords(10000000000) == "Ten billion")
    assert(figureToWords(12345678901) == "Twelve billion three hundred and forty five million six hundred and seventy eight thousand nine hundred and one")
    assert(figureToWords(100000000000) == "One hundred billion")
    assert(figureToWords(123456789012) == "One hundred and twenty three billion four hundred and fifty six million seven hundred and eighty nine thousand twelve")
    assert(figureToWords(999999999999) == "Nine hundred and ninety nine billion nine hundred and ninety nine million nine hundred and ninety nine thousand nine hundred and ninety nine")
    print('Passed!')


def figureToWordsIndian(figure: int) -> str:
    if len(str(figure)) > 12:
        return "Figure too large, must be less than 1 trillion"
    if len(str(figure)) == 0:
        return "Figure cannot be empty"
    if figure < 0:
        return "Figure must be a positive integer"
    else:
        if figure == 0:
            return "Zero"
        else:
            print(repr(capitalizeFirstLetterOnlyIndian(twelveDigitConvertorIndian(figure))))
            return capitalizeFirstLetterOnlyIndian(twelveDigitConvertorIndian(figure))

def singleDigitConvertorIndian(digit: int) -> str:
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return units[digit]
def twoDigitConvertorIndian(digits: int) -> str:
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if digits < 10:
        return singleDigitConvertorIndian(digits)
    elif 10 <= digits < 20:
        return teens[digits - 10]
    else:
        ten_part = tens[digits // 10]
        unit_part = units[digits % 10]
        if unit_part:
            return f"{ten_part} {unit_part}"
        else:
            return ten_part
def threeDigitConvertorIndian(digits: int) -> str:
    if digits < 100:
        return twoDigitConvertorIndian(digits)
    else:
        hundred_part = singleDigitConvertorIndian(digits // 100) + " Hundred"
        rest = digits % 100
        if rest:
            return f"{hundred_part} and {twoDigitConvertorIndian(rest)}"
        else:
            return hundred_part
def fourDigitConvertorIndian(digits: int) -> str:
    if digits < 1000:
        return threeDigitConvertorIndian(digits)
    else:
        thousand_part = singleDigitConvertorIndian(digits // 1000) + " Thousand"
        rest = digits % 1000
        if rest:
            return f"{thousand_part} {threeDigitConvertorIndian(rest)}"
        else:
            return thousand_part
def fiveDigitConvertorIndian(digits: int) -> str:
    if digits < 10000:
        return fourDigitConvertorIndian(digits)
    else:
        ten_thousand_part = twoDigitConvertorIndian(digits // 1000) + " Thousand"
        rest = digits % 1000
        if rest:
            return f"{ten_thousand_part} {threeDigitConvertor(rest)}"
        else:
            return ten_thousand_part
def sixDigitConvertorIndian(digits: int) -> str:
    if digits < 100000:
        return fiveDigitConvertorIndian(digits)
    else:
        hundred_thousand_part = threeDigitConvertorIndian(digits // 100000) + " Lakh"
        rest = digits % 1000
        if rest:
            return f"{hundred_thousand_part} {threeDigitConvertorIndian(rest)}"
        else:
            return hundred_thousand_part
def sevenDigitConvertorIndian(digits: int) -> str:
    if digits < 1000000:
        return sixDigitConvertorIndian(digits)
    else:
        million_part = singleDigitConvertorIndian(digits // 1000000) + " Million"
        rest = digits % 1000000
        if rest:
            return f"{million_part} {sixDigitConvertorIndian(rest)}"
        else:
            return million_part
def eightDigitConvertorIndian(digits: int) -> str:
    if digits < 10000000:
        return sevenDigitConvertorIndian(digits)
    else:
        ten_million_part = twoDigitConvertorIndian(digits // 1000000) + " Million"
        rest = digits % 1000000
        if rest:
            return f"{ten_million_part} {sixDigitConvertorIndian(rest)}"
        else:
            return ten_million_part
def nineDigitConvertorIndian(digits: int) -> str:
    if digits < 100000000:
        return eightDigitConvertorIndian(digits)
    else:
        hundred_million_part = threeDigitConvertorIndian(digits // 1000000) + " Million"
        rest = digits % 1000000
        if rest:
            return f"{hundred_million_part} {sixDigitConvertorIndian(rest)}"
        else:
            return hundred_million_part
def tenDigitConvertorIndian(digits: int) -> str:
    if digits < 1000000000:
        return nineDigitConvertorIndian(digits)
    else:
        billion_part = singleDigitConvertorIndian(digits // 1000000000) + " Billion"
        rest = digits % 1000000000
        if rest:
            return f"{billion_part} {nineDigitConvertorIndian(rest)}"
        else:
            return billion_part
def elevenDigitConvertorIndian(digits: int) -> str:
    if digits < 10000000000:
        return tenDigitConvertorIndian(digits)
    else:
        ten_billion_part = twoDigitConvertorIndian(digits // 1000000000) + " Billion"
        rest = digits % 1000000000
        if rest:
            return f"{ten_billion_part} {nineDigitConvertorIndian(rest)}"
        else:
            return ten_billion_part
def twelveDigitConvertorIndian(digits: int) -> str:
    if digits < 100000000000:
        return elevenDigitConvertorIndian(digits)
    else:
        hundred_billion_part = threeDigitConvertorIndian(digits // 1000000000) + " Billion"
        rest = digits % 1000000000
        if rest:
            return f"{hundred_billion_part} {nineDigitConvertorIndian(rest)}"
        else:
            return hundred_billion_part
def capitalizeFirstLetterOnlyIndian(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

def test_figureToWordsIndian():
    print("Testing figureToWordsIndian()...", end='')
    # assert(figureToWordsIndian("") == "Figure cannot be empty")  # Empty input
    # assert(figureToWordsIndian(-5) == "Figure must be a positive integer")  # Negative input
    # assert(figureToWordsIndian(1000000000000) == "Figure too large, must be less than 1 trillion") # Too large input
    # assert(figureToWordsIndian(0) == "Zero")
    # assert(figureToWordsIndian(5) == "Five")
    # assert(figureToWordsIndian(10) == "Ten")
    # assert(figureToWordsIndian(32) == "Thirty two")
    # assert(figureToWordsIndian(99) == "Ninety nine")
    # assert(figureToWordsIndian(100) == "One hundred")
    # assert(figureToWordsIndian(101) == "One hundred and one")
    # assert(figureToWordsIndian(500) == "Five hundred")
    # assert(figureToWordsIndian(600) == "Six hundred")
    # assert(figureToWordsIndian(999) == "Nine hundred and ninety nine")
    # assert(figureToWordsIndian(1000) == "One thousand")
    # assert(figureToWordsIndian(1001) == "One thousand one")
    # assert(figureToWordsIndian(1101) == "One thousand one hundred and one")
    # assert(figureToWordsIndian(1110) == "One thousand one hundred and ten")
    # assert(figureToWordsIndian(1500) == "One thousand five hundred")
    # assert(figureToWordsIndian(1567) == "One thousand five hundred and sixty seven")
    # assert(figureToWordsIndian(10000) == "Ten thousand")
    # assert(figureToWordsIndian(12345) == "Twelve thousand three hundred and forty five")
    #assert(figureToWordsIndian(100000) == "One lakh")
    assert(figureToWordsIndian(123456) == "One lakh twenty three thousand four hundred and fifty six")
    assert(figureToWordsIndian(1000000) == "Ten lakh")
    assert(figureToWordsIndian(1234567) == "Twelve lakh thirty four thousand five hundred and sixty seven")
    assert(figureToWordsIndian(10000000) == "One crore")
    assert(figureToWordsIndian(12345678) == "Twelve crore thirty four lakh fifty six thousand seven hundred and eighty six")
    assert(figureToWordsIndian(100000000) == "Ten crore")
    assert(figureToWordsIndian(123456789) == "Twelve crore thirty four lakh fifty six thousand seven hundred and eighty nine")
    # 1 kharab = 10^12
    assert(figureToWordsIndian(1000000000000) == "One kharab")
    # 1 neel = 10^16
    assert(figureToWordsIndian(10000000000000000) == "One neel")

def main():
    #test_figureToWords(), 
    test_figureToWordsIndian()

if __name__ == "__main__":
    main()