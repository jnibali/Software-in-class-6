

def leapyear(val):
    if (val % 4) == 0:
        if (val % 100) == 0:
            if(val % 400) == 0:
                return ("is a leap year")
            else:
                return ("is not a leap year")
        else:
            return ("is a leap year")
    else:
        return ("is not a leap year")