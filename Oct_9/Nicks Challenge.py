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


def main():
    test_figureToWords()

if __name__ == "__main__":
    main()