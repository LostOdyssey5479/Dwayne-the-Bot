from datetime import datetime

def DupeDeleter(UnsortedList):
    # Takes an already made list and deletes duplicates
    List = []
    for item in UnsortedList:
        if item not in List:
            List.append(UnsortedList)
    return List


def ValSetNum(Validation):
    # Turns a string into a list and compares to a list
    # of numbers to validate if that string is all numbers.
    ALLOWED_NUM = set("1234567890")
    Valid = True

    if not set(Validation).issubset(ALLOWED_NUM):
        Valid = False

    return Valid


def ValDigOnly(Value):
    # Validate for digits only
    IsValid = True
    if not Value.isdigit():
        IsValid = False
    elif len(Value) != 10:
        IsValid = False
    return IsValid


def ValPostal(Value):
    # Validate the postal code in the form L0L0L0
    IsValid = True
    if Value[0].isalpha() == False or Value[1].isdigit() == False or Value[2].isalpha() == False:
        IsValid = False
    elif len(Value) != 6:
        IsValid = False
    return IsValid


def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr


def FDateMFullYear(DateValue):
    # Function will accept a value and format it to dd-Mon-YYYY

    DateValueStr = DateValue.strftime("%d-%b-%Y")

    return DateValueStr

def FDateInput(InputValue):
    # Function will accept a value and format it to a date in this case YYYY-MM-DD

    DateValueStr = datetime.strptime(InputValue, "%Y-%m-%d")

    return DateValueStr

def EmptyVal(InputValue):

    Empty = False

    if InputValue == "" or InputValue == " ":
        Empty = True

    return Empty

