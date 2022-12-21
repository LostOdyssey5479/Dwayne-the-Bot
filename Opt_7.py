#!/usr/bin/python

from matplotlib import pyplot as plt
from matplotlib import style
from datetime import datetime
import FormatValues as fV

# Profit Report Program for Hab Taxi Company
# Report will print year to date

# Initialize ctrs, accs, lists
LossAcc = 0
ProfAcc = 0

# Year value for validation in printing
TheYear = datetime.now()
TheYear = TheYear.strftime("%Y")



print()
print("HAB Taxi Services")
print("Profit Listing")
print(f"{TheYear} to Date")
print(" " * 44, "*REVENUES*")
print("  Transaction ID        Driver Number         Amount          HST          Total          Date")
print("-" * 97)

f = open("Revenue.dat", "r")


for TransAct in f:


    TransAct = TransAct.split(",")
    TransID = int(TransAct[0].strip())
    TransDate = str(TransAct[1].strip())
    TransReason = str(TransAct[2].strip())
    DriverNum = int(TransAct[3].strip())
    Subtotal = float(TransAct[4].strip())
    HST = float(TransAct[5].strip())
    GrandTotal = float(TransAct[6].strip())

    ProfAcc += GrandTotal

    if TransDate[0:4] == TheYear:
        print(f"     {TransID:^5d}            {DriverNum:>7d}                 {fV.FDollar2(Subtotal):>7s}     "
              f"   {fV.FDollar2(HST):>6s}      {fV.FDollar2(GrandTotal):>8s}      {TransDate}")

f.close()

print("-" * 97)
print(" " * 44, "*EXPENSES*")
print("  Invoice Number   Item Number   Item Cost    Item #   Subtotal     HST        Total     Date")
print("-" * 97)


e = open("Expenses.dat", "r")


for Expenses in e:

    Expense = Expenses.split(",")
    InvoiceNum = int(Expense[0].strip())
    InvoiceDate = str(Expense[1].strip())
    DriverNum = int(Expense[2].strip())
    PartNum = int(Expense[3].strip())
    PartName = str(Expense[4].strip())
    PartCost = float(Expense[5].strip())
    NumOfParts = int(Expense[6].strip())
    Subtotal = float(Expense[6].strip())
    HST = float(Expense[6].strip())
    GrandTotal = float(Expense[6].strip())

    LossAcc += GrandTotal

    if TransDate[0:4] == TheYear:

        print(f"     {InvoiceNum:>6d}       {PartNum:>6d}        {fV.FDollar2(PartCost):>7s}         {NumOfParts:>2d}"
              f"       {fV.FDollar2(Subtotal):>6s}     {fV.FDollar2(HST):>6s}  {fV.FDollar2(GrandTotal):>8s}   {InvoiceDate}")


print("-" * 97)
print(f"Total Profit : {fV.FDollar2(ProfAcc)}")
print(f"Total Loss : {fV.FDollar2(LossAcc)}")

while True:
    style.use('ggplot')

    x = [0, 1, 2, 3, 4, 5]
    y = [46, 38, 29, 22, 13, 11]

    fig, ax = plt.subplots()

    ax.bar(x, y, align='center')

    ax.set_title('Olympic Gold medals in London')
    ax.set_ylabel('Gold medals')
    ax.set_xlabel('Countries')

    ax.set_xticks(x)
    ax.set_xticklabels(("USA", "China", "UK", "Russia",
    "South Korea", "Germany"))

    plt.show()

    ans = input("Would you like to select another menu option?").upper()
    while True:
        ans = input("Would you like to select another menu option?").upper()
        if ans == "Y":
            continue
        elif ans == "N":
            quit()
        else:
            print("Answer has to be (Y/N)")
