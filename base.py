"""
Number Base Conversion functions:
Because python doesn't have any for some reason
"""

# Converts Number to Base using NumberToSymbol
def NumberToBase(Number: int, Base: int, NumberToSymbol: list[str]):
    if Number != 0: 
        digits = [] # Digits to convert
        while Number:
            digits.append(int(Number % Base)) # Append reminder to digits
            Number //= Base # Set 1 to quotient
    else:
        digits = [0] # 0 is 0 in ANY BASE

    baseNumber: str = "" # Number to be returned
    for digit in digits[::-1]:
        baseNumber += NumberToSymbol[digit]
    return baseNumber 

# Converts NumberBase Base to Base 10 using NumberToSymbol
def BaseToNumber(Base: str, NumberBase: int, NumberToSymbol: list[str]):
    Number = 0 # Number to return
    for Place, Symbol in enumerate(Base[::-1]):
        # Translate symbol into number
        Value = NumberToSymbol.index(Symbol)

        # Use place to make value accurate
        Number += Value * (NumberBase * Place if NumberBase * Place != 0 else 1)
    return Number
