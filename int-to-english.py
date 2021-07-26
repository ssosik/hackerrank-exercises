
digitsMap = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        }

tensMap = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        }

teensMap = {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'forteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        }

# Add more here, *descending order*
places = [(1000000000, 'billion'), (1000000, 'million'), (1000, 'thousand'), (1, '')]

def processTriplet(n, place):
    s = '' # string to accumulate

    h = int(n/100) # handle hundreds
    if h > 0:
        s += f"{digitsMap[h]} hundred "

    t = n % 100 # tens
    i = n % 10  # single digit

    # Look up special cases
    if t in teensMap:
        # 11, 12 .... 19
        s += f"{teensMap[t]} "

    elif t in tensMap:
        # 10, 20 ..... 90
        s += f"{tensMap[t]} "

    elif int(t/10) * 10 in tensMap:
        # Handle other numbers greater than 9 not already handled
        i = t % 10
        t = int(t/10) * 10
        s += f"{tensMap[t]} {digitsMap[i]} "

    else:
        # else, handle the single digit
        s += f"{digitsMap[i]} "
    
    # emit place identifier, e.g. thousands
    s += f"{place} "

    return s

def toEnglish(n):
    s = ''
    orig = n
    # Loop over places in descending order and process each tripet
    for d, place in places:
        if n >= d:
            s += processTriplet(int(n/d), place)
            n = n % d
    print(orig, s)

toEnglish(1)
toEnglish(9)
toEnglish(10)
toEnglish(11)
toEnglish(19)
toEnglish(20)
toEnglish(21)

toEnglish(101)
toEnglish(109)
toEnglish(110)
toEnglish(111)
toEnglish(119)
toEnglish(120)
toEnglish(121)
toEnglish(987)
toEnglish(999)

toEnglish(1001)
toEnglish(1101)
toEnglish(1109)
toEnglish(1110)
toEnglish(1111)
toEnglish(1119)
toEnglish(1120)
toEnglish(1121)
toEnglish(1987)
toEnglish(1999)
toEnglish(1999)

toEnglish(41101)
toEnglish(41109)
toEnglish(41110)
toEnglish(41111)
toEnglish(41119)
toEnglish(41120)
toEnglish(41121)
toEnglish(41987)
toEnglish(41999)
toEnglish(41999)

toEnglish(941101)
toEnglish(941109)
toEnglish(941110)
toEnglish(941111)
toEnglish(941119)
toEnglish(941120)
toEnglish(941121)
toEnglish(941987)
toEnglish(941999)
toEnglish(941999)

toEnglish(9941101)
toEnglish(9941109)
toEnglish(9941110)
toEnglish(9941111)
toEnglish(9941119)
toEnglish(9941120)
toEnglish(9941121)
toEnglish(9941987)
toEnglish(9941999)
toEnglish(9941999)

toEnglish(2349941999)
toEnglish(82349941999)

toEnglish(82000010001)
