import math

def dayOfWeek(month, day, year):
    # Zeller's Congruence algorithm to calculate the day of the week
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    K = year % 100
    J = year // 100
    f = q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)
    day = (f % 7 + 7) % 7
    if day == 0:
        day = 7
    return day

def testDayOfWeek():
    print('Testing dayOfWeek()...', end='')
    # On 6/15/1215, the Magna Carta was signed on a Monday!
    assert(dayOfWeek(6, 15, 1215) == 2)
    # On 3/11/1952, the author Douglas Adams was born on a Tuesday!
    assert(dayOfWeek(3, 11, 1952) == 3)
    # on 4/12/1961, Yuri Gagarin became the first man in space, on a Wednesday!
    assert(dayOfWeek(4, 12, 1961) == 4)
    # On 7/4/1776, the Declaration of Independence was signed on a Thursday!
    assert(dayOfWeek(7, 4, 1776) == 5)
    # on 1/2/1920, Isaac Asimov was born on a Friday!
    assert(dayOfWeek(1, 2, 1920) == 6)
    # on 10/11/1975, Saturday Night Live debuted on a Saturday (of course)!
    assert(dayOfWeek(10, 11, 1975) == 7)
    # On 2/5/2006, the Steelers won Super Bowl XL on a Sunday!
    assert(dayOfWeek(2, 5, 2006) == 1)
    print('Passed!')

def main():
    testDayOfWeek()

main()