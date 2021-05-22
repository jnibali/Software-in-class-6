

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

def test_answer():
    assert leapyear(2004) == "is a leap year"
    assert leapyear(2012) == "is a leap year"
    assert leapyear(2007) == "is not a leap year"
    assert leapyear(2001) == "is not a leap year"