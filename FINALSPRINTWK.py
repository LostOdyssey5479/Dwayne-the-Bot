# HAB TAXI SERVICE
# A program that allows Hab Taxi service to record new employees, rent new vehicles, record
# employee payment, print profit reports, and print a sample maintenance report
# AUTHOR JONATHAN IVANY, TYLER STUCKLESS, ALEXANDER GILLESPIE
# DATE: 2022-12-12


# Import what functions we need
from matplotlib import pyplot as plt
from matplotlib import style
from datetime import datetime, timedelta
import FormatValues as fV

# Initialize some dates for validating
ProDay = datetime.today()
ProDay = fV.FDateS(ProDay)
JustDay = datetime.today().day

# Open and read our default files
f = open("Defaults.dat", "r")

NEXT_TRANS_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTH_STAND_FEE = float(f.readline())
DAY_RENT_FEE = float(f.readline())
WEEK_RENT_FEE = float(f.readline())
HST_RATE = float(f.readline())
NEXT_PAYMENT_ID = int(f.readline())
NEXT_RENTAL_ID = int(f.readline())
MONTH_PAY_VAL = int(f.readline())

# Close file as values are assigned
f.close()


def profit_report():
    # A program that calculates profit and loss via revenue and expenses file
    # Counters for later
    Mon_Stan_Fee_CTR = 0
    Cab_Fare_CTR = 0
    Rental_CTR = 0

    # Profit Report Program for Hab Taxi Company
    # Report will print year to date

    # Initialize ctrs, accs, lists
    LossAcc = 0
    ProfAcc = 0

    # Year value for validation in printing
    TheYear = datetime.now()
    TheYear = TheYear.strftime("%Y")

    # Print the Revenues
    print()
    print("HAB Taxi Services")
    print("Profit Listing")
    print(f"{TheYear} to Date")
    print(" " * 44, "*REVENUES*")
    print("  Transaction ID        Driver Number         Amount          HST          Total          Date")
    print("-" * 97)

    # Open Revenue.dat and retrieve data
    rD = open("Revenue.dat", "r")

    for TransAct in rD:

        TransAct = TransAct.split(",")
        TransID = int(TransAct[0].strip())
        TransDate = str(TransAct[1].strip())
        TransReason = str(TransAct[2].strip())
        if TransReason == "Monthly Stand Fees":
            Mon_Stan_Fee_CTR += 1
        elif TransReason == "Cab Fare":
            Cab_Fare_CTR += 1
        elif TransReason == "Rental":
            Rental_CTR += 1
        DriverNum = int(TransAct[3].strip())
        Subtotal = float(TransAct[4].strip())
        HST = float(TransAct[5].strip())
        GrandTotal = float(TransAct[6].strip())
        ProfAcc += GrandTotal

        if TransDate[0:4] == TheYear:
            print(f"     {TransID:^5d}            {DriverNum:>7d}                 {fV.FDollar2(Subtotal):>7s}     "
                  f"   {fV.FDollar2(HST):>6s}      {fV.FDollar2(GrandTotal):>8s}      {TransDate}")

    rD.close()

    # Print the Expenses
    print("-" * 97)
    print(" " * 44, "*EXPENSES*")
    print("  Invoice Number   Item Number   Item Cost    Item #   Subtotal     HST        Total     Date")
    print("-" * 97)

    # Open Expenses.dat and retrieve data
    e = open("Expenses.dat", "r")

    for Expenses in e:

        Expense = Expenses.split(",")
        InvoiceNum = int(Expense[0].strip())
        InvoiceDate = str(Expense[1].strip())
        PartNum = int(Expense[3].strip())
        PartCost = float(Expense[5].strip())
        NumOfParts = int(Expense[6].strip())
        Subtotal = float(Expense[7].strip())
        HST = float(Expense[8].strip())
        GrandTotal = float(Expense[9].strip())
        LossAcc += GrandTotal
        if TransDate[0:4] == TheYear:
            print(
                f"     {InvoiceNum:>6d}       {PartNum:>6d}        {fV.FDollar2(PartCost):>7s}         {NumOfParts:>2d}"
                f"     {fV.FDollar2(Subtotal):>7s}    {fV.FDollar2(HST):>7s}   {fV.FDollar2(GrandTotal):>8s}   "
                f"{InvoiceDate:>10s}")

    print("-" * 97)
    print(f"Total Profit : {fV.FDollar2(ProfAcc)}")
    print(f"Total Loss :   {fV.FDollar2(LossAcc)}")

    # !/usr/bin/python
    # Asking user if they would like to see the graph
    while True:
        DataView = input(f"Would you like to see analytic data for {TheYear}? Y/N: ").upper()
        if DataView == "Y":
            # Graph formatting
            style.use('ggplot')
            x = [0, 1]
            y = [ProfAcc, LossAcc]

            fig, ax = plt.subplots()

            ax.bar(x, y, align='center')

            ax.set_title("HAB TAXI FINANCIAL ANALYTICS")
            ax.set_ylabel('Dollar')
            ax.set_xlabel(f'For Year {TheYear}')
            ax.set_xticks(x)
            ax.set_xticklabels(("Profit", "Loss"))
            plt.bar(x, y, color=['green', 'red'])
            plt.show()
            break
        elif DataView == "N":
            main()
        else:
            print("Answer must be a Y or N. Please retry: ")
    # Ask user if they would like to use the menu again
    while True:
        ans = input("Would you like to go back to the menu? Please respond with (Y/N): ").upper()
        if ans == "Y":
            main()
        elif ans == "N":
            quit()
        else:
            print("Answer must be a Y or N. Please retry: ")


def rental_tracker():

    # This function allows users to rent cars and store that info

    # Enable variables that are outside function
    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL

    # Initialize rent cost counter
    RentCost = 0
    # Variable for saving reasoning
    TransactDesc = "Rental"

    while True:
        print()
        print("_________________________________________")
        print("||   HAB Taxi Service Rental Tracker   ||  ")
        print("-----------------------------------------")
        print("     Please Enter Rental Information")
        print()

        # Validation loop for input
        while True:
            DriverNum = input("Driver number of renter: ")
            if fV.EmptyVal(DriverNum) is True:
                print("Please enter your driver number")
            elif fV.ValSetNum(DriverNum) is False:
                print("Driver number is numeric digits only. Please Re-Enter")
            else:
                break

        # Validation loop for input
        while True:
            RentStart = input("Start date of rental(YYYY-MM-DD): ")
            try:
                RentStart = datetime.strptime(RentStart, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format, please try again.")

        # Validation loop for input
        while True:
            CarNum = input("Car number 1, 2, 3, or 4: ")
            if fV.ValSetNum(CarNum) is False:
                print("Our cars are labeled 1 to 4, please enter digits only.")
            elif fV.EmptyVal(CarNum) is True:
                print("Please enter car number desired")
            elif int(CarNum) < 1 or int(CarNum) > 4:
                print("Bys, we only have four cars...")
            else:
                break

        # Validation loop for input
        while True:
            RentType = input("For a Day or a Week?(D,W): ").upper()
            if RentType == "D" or RentType == "DAY":
                RentType = "Day"
                RentDays = 1
                RentCost += DAY_RENT_FEE
                RentEnd = RentStart + timedelta(days=1)
                break
            elif RentType == "W" or RentType == "WEEK":
                RentType = "Week"
                RentDays = 7
                RentCost += WEEK_RENT_FEE
                RentEnd = RentStart + timedelta(days=7)
                break
            else:
                print("You must enter day or d, week or w")

        # Calculate our HST and then use that to find total cost
        HST = RentCost * HST_RATE
        TotalCost = RentCost + HST

        # Print receipt back to user showing input and calculated values
        print()
        print(" " * 20, "HAB TAXI SERVICES")
        print(" " * 15, "~" * 26)
        print(" " * 21, "RENTAL RECEIPT")
        print()
        print(f"    RENTAL ID #:{NEXT_RENTAL_ID:^6d}")
        print(" " * 3, "=" * 18)
        print(f"    DRIVER ID #: {DriverNum:^6s}               DATE: {ProDay}")
        print(" " * 3, "=" * 50)
        print(f"    START DATE:                             {fV.FDateS(RentStart)}")
        print(f"    END DATE:                               {fV.FDateS(RentEnd)}")
        print(f"    NUMBER OF DAYS:                                 {RentDays:>2d}")
        print(" " * 3, "-" * 50)
        print(f"    COST PER DAY:                            {fV.FDollar2(DAY_RENT_FEE):>9s}")
        print(f"    COST PER WEEK:                           {fV.FDollar2(WEEK_RENT_FEE):>9s}")
        print(" " * 3, "=" * 50)
        print(f"    RENTAL COST:                            {fV.FDollar2(RentCost):>10s}")
        print(f"    HST:                                       {fV.FDollar2(HST):>7s}")
        print(" " * 3, "-" * 50)
        print(f"    RENTAL TOTAL:                           {fV.FDollar2(TotalCost):>10s}")


        # Open rental file and add rental report
        r = open("Rental.dat", "a")

        r.write("{}, ".format(str(NEXT_RENTAL_ID)))
        r.write("{}, ".format(str(DriverNum)))
        r.write("{}, ".format(str(RentStart)))
        r.write("{}, ".format(str(CarNum)))
        r.write("{}, ".format(str(RentType)))
        r.write("{}, ".format(str(RentDays)))
        r.write("{}, ".format(str(RentCost)))
        r.write("{}, ".format(str(HST)))
        r.write("{}\n".format(str(TotalCost)))

        # Close rental file once rental report has been written
        r.close()

        # Let user know information been saved.
        print()
        print(f"              Rental ID: {NEXT_RENTAL_ID} for {CarNum} to driver {DriverNum}")
        print("                 Has been successfully saved")

        # Increase our rental ID by 1 for next rental
        NEXT_RENTAL_ID += 1

        # Open and write a revenue report from rental data
        r = open("Revenue.dat", "a")

        r.write("{}, ".format(str(NEXT_TRANS_NUM)))
        r.write("{}, ".format(str(ProDay)))
        r.write("{}, ".format(str(TransactDesc)))
        r.write("{}, ".format(str(DriverNum)))
        r.write("{}, ".format(str(RentCost)))
        r.write("{}, ".format(str(HST)))
        r.write("{}\n".format(str(TotalCost)))

        # Close file once report is written
        r.close()

        # Let user know transaction was a success
        print()
        print(f"                   Transaction {NEXT_TRANS_NUM} Success")
        print()

        # Increase our transaction number by one for the next transaction
        NEXT_TRANS_NUM += 1

        # Open our defaults file and write back default values
        e = open("Defaults.dat", "w")

        e.write("{}\n".format(str(NEXT_TRANS_NUM)))
        e.write("{}\n".format(str(NEXT_DRIVER_NUM)))
        e.write("{}\n".format(str(MONTH_STAND_FEE)))
        e.write("{}\n".format(str(DAY_RENT_FEE)))
        e.write("{}\n".format(str(WEEK_RENT_FEE)))
        e.write("{}\n".format(str(HST_RATE)))
        e.write("{}\n".format(str(NEXT_PAYMENT_ID)))
        e.write("{}\n".format(str(NEXT_RENTAL_ID)))
        e.write("{}\n".format(str(MONTH_PAY_VAL)))

        # Close file once values are written back
        e.close()

        # Validation loop for input
        while True:
            Continue = input("Another Rental? Y/N: ").upper()
            if fV.EmptyVal(Continue) is True:
                print("Enter Y or N")
            elif Continue == "Y":
                break
            elif Continue == "N":
                main()
            else:
                print("Enter Y for new report, or N for main menu")


def maintenance_report():

    # This program prints maintenance reports from the current year to the current day

    # Initialize a loss counter
    LossAcc = 0

    # Initialize today's year for validation
    CurrYear = datetime.now()
    CurrYear = CurrYear.strftime("%Y")

    print()
    print("HAB Taxi Service")
    print("Car Maintenance")
    print(f"Reports from Year to Date {CurrYear}")
    print()
    print("  ID  |   DATE   | CAR |    DAMAGE DESC    | DAMAGE DATE | PART NAME | SUBTOTAL | HST |  TOTAL")
    print("-" * 98)

    # Open maintenance file to read and put in for loop to separate lines
    m = open("Maintenance.dat", "r")

    for MaintainData in m:
        # Declare each line
        Maintain = MaintainData.split(",")
        # Assign indexes to variables
        MaintainID = int(Maintain[0].strip())
        MaintainDate = str(Maintain[1].strip())
        CarNum = int(Maintain[2].strip())
        DamageDesc = str(Maintain[3].strip())
        DamageDate = str(Maintain[4].strip())
        PartName = str(Maintain[5].strip())
        Subtotal = float(Maintain[6].strip())
        Hst = float(Maintain[7].strip())
        Total = float(Maintain[8].strip())

        # Check to see if record is in current year
        if MaintainDate[0:4] == CurrYear:
            # Add the totals from each record to losses
            LossAcc += Total
            print(f"{MaintainID:>6d} {MaintainDate}   {CarNum}   {DamageDesc:^20s}  {DamageDate:}    "
                  f"{PartName:<9s} {fV.FDollar2(Subtotal):>8s}   {fV.FDollar2(Hst):>5s} {fV.FDollar2(Total):>8s}")

    print("-" * 98)
    print(f"Total Maintenance Loss: {fV.FDollar2(LossAcc)}")
    # Close file once reports have been printed
    m.close()

    # Input to bring user back to main menu
    Continue = input("Press enter to continue.")
    if fV.EmptyVal(Continue) is True:
        main()
    else:
        main()


def record_employee_payment():

    # Enable variables that are outside function
    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL

    # Establish day the payment is made, formatted into a string using a function from another file
    PaymentDate = datetime.today()
    PaymentDate = fV.FDateS(PaymentDate)

    # Program is set in a loop for to be repeated
    while True:
        print("_________________________________________")
        print("||  HAB Taxi Service Payment Recorder  ||  ")
        print("-----------------------------------------")

        # Loop for input validation
        while True:
            DriverNum = input("Enter driver number of payee: ")
            if fV.EmptyVal(DriverNum) is True:
                print("Please re-enter the driver number")
            elif fV.ValSetNum(DriverNum) is False:
                print("Driver Number is numeric digits only.")
            else:
                break

        # Loop for input validation
        while True:
            PayAmt = input("Enter the payment amount: ")
            if fV.EmptyVal(PayAmt) is True:
                print("Please enter the amount to be paid down")
            elif fV.ValSetNum(PayAmt) is False:
                print("Please enter numeric digits only.")
            else:
                PayAmt = fV.FDollar2(int(PayAmt))
                break

        # Loop for input validation
        while True:
            PayReason = input("Enter the reason for the payment: ")
            if fV.EmptyVal(PayReason) is True:
                print("Please enter the reason for payment")
            else:
                break

        # Loop for input validation
        while True:
            PayMethod = input("Enter the payment method (Cash, Debit, or Visa): ").upper()
            if fV.EmptyVal(PayMethod) is True:
                print("Please enter the method of payment.")
            elif PayMethod == "CASH" or PayMethod == "C":
                PayMethod = "Cash"
                break
            elif PayMethod == "DEBIT" or PayMethod == "D":
                PayMethod = "Debit"
                break
            elif PayMethod == "VISA" or PayMethod == "V":
                PayMethod = "Visa"
                break
            else:
                print("Please enter valid payment method. (C,D,V) or (Cash, Debit, Visa)")

        # Print receipt to user
        print()
        print("==================================================")
        print("|", " " * 15, "HAB TAXI SERVICES              |")
        print("|", " " * 10, "~" * 26, "         |")
        print("|", " " * 16, "PAYMENT RECEIPT               |")
        print("|                                                |")
        print(f"|   Payment ID #: {NEXT_PAYMENT_ID:>5d}     DRIVER ID #: {DriverNum:>5s}   |")
        print("|   ==========================================   |")
        print(f"|   Payment Reason: {PayReason:*^26}   |")
        print(f"|   Payment amount:                 {PayAmt:>10s}   |")
        print(f"|   Payment method:                     {PayMethod:>6}   |")
        print("|   ==========================================   |")
        print(f"|   Date of Payment:                {PaymentDate}   |")
        print("|                                                |")
        print("==================================================")

        # Open payment data file and add payment record
        p = open("PaymentRec.dat", "a")

        p.write("{}, ".format(str(NEXT_PAYMENT_ID)))
        p.write("{}, ".format(DriverNum))
        p.write("{}, ".format(PaymentDate))
        p.write("{}, ".format(PayAmt))
        p.write("{}, ".format(PayReason))
        p.write("{}\n".format(PayMethod))

        # Close file once values are written
        p.close()

        # Let user know information has been saved
        print("Payment information has been saved.")

        # Increase payment ID by 1 for next payment
        NEXT_PAYMENT_ID += 1

        # Write default values back
        p = open("Defaults.dat", "w")

        p.write("{}\n".format(str(NEXT_TRANS_NUM)))
        p.write("{}\n".format(str(NEXT_DRIVER_NUM)))
        p.write("{}\n".format(str(MONTH_STAND_FEE)))
        p.write("{}\n".format(str(DAY_RENT_FEE)))
        p.write("{}\n".format(str(WEEK_RENT_FEE)))
        p.write("{}\n".format(str(HST_RATE)))
        p.write("{}\n".format(str(NEXT_PAYMENT_ID)))
        p.write("{}\n".format(str(NEXT_RENTAL_ID)))
        p.write("{}\n".format(str(MONTH_PAY_VAL)))

        # Close file once values are written back
        p.close()

        # Loop for input validation
        while True:
            Continue = input("Would you like to make another payment? Y/N: ").upper()
            if fV.EmptyVal(Continue) is True:
                print("Please enter Y or N")
            elif Continue == "Y":
                break
            elif Continue == "N":
                main()
            else:
                print("Enter Y for new report, or N for main menu")


def new_driver():

    # Enable variables that are outside function
    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL

    # Unnecessary but for shortened variable name
    DriverNum = NEXT_DRIVER_NUM

    # Establish our BalDue counter
    BalDue = 0
    print()
    print("_________________________________________")
    print("||          HAB Taxi Service           ||")
    print("-----------------------------------------")
    print("          ENTER A NEW EMPLOYEE           ")

    # Loop for input validation
    while True:
        DriverFName = input("First name: ").title()
        if DriverFName == "" or DriverFName == " ":
            print("Please enter drivers first name.")
        else:
            break

    # Loop for input validation
    while True:
        DriverLName = input("Last name: ").title()
        if DriverLName == "" or DriverLName == " ":
            print("Please enter drivers last name.")
        else:
            break

    # Loop for input validation
    while True:
        StAdd = input("Street Address: ").title()
        if StAdd == "" or StAdd == " ":
            print("Please enter the Driver's address.")
        else:
            break

    # Loop for input validation
    while True:
        PhoneNum = input("Phone Number: ")
        if len(PhoneNum) != 10:
            print("Please input a 10 digit phone number")
        elif not PhoneNum.isdigit():
            print("Phone number must be digits only.")
        else:
            break

    # Loop for input validation
    while True:
        LicenseNum = input("License Number: ")
        if fV.EmptyVal(LicenseNum) is True:
            print("Please enter the Driver's License number.")
        elif fV.ValSetNum(LicenseNum) is False:
            print("Please enter the numbers only.")
        else:
            break

    # Loop for input validation
    while True:
        ExpiryDate = input("Expiry Date(YYYY-MM-DD): ")

        try:   #
            ExpiryDate = fV.FDateInput(ExpiryDate)
            ExpDate = fV.FDateS(ExpiryDate)
            break
        except ValueError:
            print("Invalid date format, please re-enter")

    # Loop for input validation
    while True:
        InsurCompany = input("Insurance Company: ")
        if InsurCompany == "" or InsurCompany == " ":
            print("Please enter the insurance company.")
        else:
            break

    # Loop for input validation
    while True:
        PolicyNum = input("Policy Number: ")
        if not PolicyNum.isdigit():
            print("Policy numbers in this case are digit only. Please re-enter.")
        else:
            break

    # Loop for input validation
    while True:
        OwnCar = input("Whether or not you will use your own car (Y for Yes, N for No): ").upper()
        if OwnCar == "" or OwnCar == " ":
            print("Please specify yes or no.")
        elif OwnCar == "Y":
            OwnCar = "Yes"
            break
        elif OwnCar == "N":
            OwnCar = "No"
            break
        else:
            print("Please use Y or N to specify if you will use your own car.")

    # Print new employee info back to user
    print("Hab Taxi Services")
    print("Employee Information")
    print(f"Driver Number: {DriverNum:>6d}")
    print()
    print("EMPLOYEE INFORMATION")
    print("=" * 20)
    print("First Name     Last Name      Street Address     Phone Number")
    print("-------------------------------------------------------------")
    print(f"{DriverFName:^10s}  |  {DriverLName:^10s}  |  {StAdd:^15s}  |  {PhoneNum:^10s}")
    print("-------------------------------------------------------------")
    print()
    print("EMPLOYEE INSURANCE INFORMATION")
    print("=" * 30)
    print(" License #     Expiry Date     Insurance Company   Policy Number")
    print("----------------------------------------------------------------")
    print(f"{LicenseNum:^10s} |   {ExpDate}   |  {InsurCompany:^15s}  |  {PolicyNum:^10s}")

    # Loop for input validation
    if OwnCar == "Yes":
        print("This Employee will use their own car.")
    elif OwnCar == "No":
        print("This employee will need a rental.")

    # Open Employee data file and add new record
    e = open("EmployeeRec.dat", "a")

    e.write("{}, ".format(str(NEXT_DRIVER_NUM)))
    e.write("{}, ".format(DriverFName))
    e.write("{}, ".format(DriverLName))
    e.write("{}, ".format(StAdd))
    e.write("{}, ".format(PhoneNum))
    e.write("{}, ".format(LicenseNum))
    e.write("{}, ".format(ExpDate))
    e.write("{}, ".format(InsurCompany))
    e.write("{}, ".format(PolicyNum))
    e.write("{}, ".format(OwnCar))
    e.write("{}\n".format(BalDue))

    # Once written, close file
    e.close()

    print()
    print("Employee information has been saved.")
    # Increase driver number by 1 for next driver record
    NEXT_DRIVER_NUM += 1

    # Open defaults file, update values
    e = open("Defaults.dat", "w")

    e.write("{}\n".format(str(NEXT_TRANS_NUM)))
    e.write("{}\n".format(str(NEXT_DRIVER_NUM)))
    e.write("{}\n".format(str(MONTH_STAND_FEE)))
    e.write("{}\n".format(str(DAY_RENT_FEE)))
    e.write("{}\n".format(str(WEEK_RENT_FEE)))
    e.write("{}\n".format(str(HST_RATE)))
    e.write("{}\n".format(str(NEXT_PAYMENT_ID)))
    e.write("{}\n".format(str(NEXT_RENTAL_ID)))
    e.write("{}\n".format(str(MONTH_PAY_VAL)))

    # Close file once values are written
    e.close()

    # Loop for input validation
    while True:
        Continue = input("Add another employee?(Y,N): ").upper()
        if Continue == "Y":
            break
        elif Continue == "N":
            main()
        else:
            print("Enter Y for Yes or N for No")


def main():
    # This function represents the main menu and allows user to navigate between the other servicing functions

    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL, JustDay

    # Check to see if it's the first of month, if first of month
    # check monthly val to see if monthly stand fees have been charged, if not
    # charge month stand fees to employees with their own car
    if JustDay == 1 and MONTH_PAY_VAL == 0:
        MONTH_PAY_VAL += 1
        TransDesc = "Monthly Stand Fees"
        Hst = MONTH_STAND_FEE * HST_RATE
        Total = Hst + MONTH_STAND_FEE

        eR = open("EmployeeRec.dat", "r")

        for Drivers in eR:

            Driver = Drivers.split(", ")

            DriverNum = int(Driver[0].strip())
            OwnCar = str(Driver[9].strip())

            if OwnCar == "Y":
                r = open("Revenue.dat", "a")

                r.write("{}, ".format(str(NEXT_TRANS_NUM)))
                r.write("{}, ".format(str(ProDay)))
                r.write("{}, ".format(str(TransDesc)))
                r.write("{}, ".format(str(DriverNum)))
                r.write("{}, ".format(str(MONTH_STAND_FEE)))
                r.write("{}, ".format(str(Hst)))
                r.write("{}\n".format(str(Total)))

                r.close()

                NEXT_TRANS_NUM += 1

                d = open("Defaults.dat", "w")

                d.write("{}\n".format(str(NEXT_TRANS_NUM)))
                d.write("{}\n".format(str(NEXT_DRIVER_NUM)))
                d.write("{}\n".format(str(MONTH_STAND_FEE)))
                d.write("{}\n".format(str(DAY_RENT_FEE)))
                d.write("{}\n".format(str(WEEK_RENT_FEE)))
                d.write("{}\n".format(str(HST_RATE)))
                d.write("{}\n".format(str(NEXT_PAYMENT_ID)))
                d.write("{}\n".format(str(NEXT_RENTAL_ID)))
                d.write("{}\n".format(str(MONTH_PAY_VAL)))

                d.close()

    # If it's the 2nd of the month remove 1 from val to reset for next month
    if JustDay == 2 and MONTH_PAY_VAL == 1:
        MONTH_PAY_VAL -= 1

        e = open("Defaults.dat", "w")

        e.write("{}\n".format(str(NEXT_TRANS_NUM)))
        e.write("{}\n".format(str(NEXT_DRIVER_NUM)))
        e.write("{}\n".format(str(MONTH_STAND_FEE)))
        e.write("{}\n".format(str(DAY_RENT_FEE)))
        e.write("{}\n".format(str(WEEK_RENT_FEE)))
        e.write("{}\n".format(str(HST_RATE)))
        e.write("{}\n".format(str(NEXT_PAYMENT_ID)))
        e.write("{}\n".format(str(NEXT_RENTAL_ID)))
        e.write("{}\n".format(str(MONTH_PAY_VAL)))

        e.close()

    # Today's year for validation
    TodayYear = datetime.today().year

    print("---HAB Taxi Services---")
    print("Company Services System")
    print("")
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing")
    print("7. Print Driver Financial Listing.")
    print(f"8. Maintenance Report for {TodayYear}")
    print("9. Quit Program.")


    # Loop validation for input main menu options
    while True:
        Ans = input("Enter choice (1-9): ")
        # Option 1, 2 OR 3
        if Ans == "1":
            new_driver()
        elif Ans == "2":
            print("Unavailable")
        elif Ans == "3":
            print("Unavailable")
        # Option 4
        elif Ans == "4":
            rental_tracker()
        # Option 5
        elif Ans == "5":
            record_employee_payment()
        # Option 6 OR 7
        elif Ans == "6":
            profit_report()
        elif Ans == "7":
            print("Unavailable")
        # Option 8
        elif Ans == "8":
            maintenance_report()

        elif Ans == "9":
            quit()

        else:
            print("Options are (1-9). Please re-enter. ")


if __name__ == "__main__":    # Program will start on the main menu function
    main()
