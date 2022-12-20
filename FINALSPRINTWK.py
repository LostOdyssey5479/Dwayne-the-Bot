# HAB TAXI SERVICE
# AUTHOR JONATHAN IVANY, TYLER STUCKLESS, ALEXANDER GILLESPIE
# DATE: 2022-12-12

from datetime import datetime, timedelta
import FormatValues as fV

ProDay = datetime.today()
ProDay = fV.FDateS(ProDay)
JustDay = datetime.today().day

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

f.close()


def rental_tracker():

    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL


    RentCost = 0

    TransactDesc = "Rental"

    print()
    print("_________________________________________")
    print("||   HAB Taxi Service Rental Tracker   ||  ")
    print("-----------------------------------------")
    print("     Please Enter Rental Information")
    print()

    while True:
        DriverNum = input("Driver number of renter: ")
        if fV.EmptyVal(DriverNum) is True:
            print("Please enter your driver number")
        elif fV.ValSetNum(DriverNum) is False:
            print("Driver number is numeric digits only. Please Re-Enter")
        else:
            break

    while True:
        RentStart = input("Start date of rental(YYYY-MM-DD): ")
        try:
            RentStart = datetime.strptime(RentStart, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format, please try again.")

    while True:
        CarNum = input("Car number 1, 2, 3, or 4: ")
        if fV.ValSetNum(CarNum) is False:
            print("Our cars are labeled 1 to 4, please enter digits only.")
        else:
            break

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

    HST = RentCost * HST_RATE
    TotalCost = RentCost + HST

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

    r.close()

    print()
    print(f"              Rental ID: {NEXT_RENTAL_ID} for {CarNum} to driver {DriverNum}")
    print("                 Has been successfully saved")

    NEXT_RENTAL_ID += 1

    r = open("Revenue.dat", "a")

    r.write("{}, ".format(str(NEXT_TRANS_NUM)))
    r.write("{}, ".format(str(ProDay)))
    r.write("{}, ".format(str(TransactDesc)))
    r.write("{}, ".format(str(DriverNum)))
    r.write("{}, ".format(str(RentCost)))
    r.write("{}, ".format(str(HST)))
    r.write("{}\n".format(str(TotalCost)))

    r.close()

    print()
    print(f"                   Transaction {NEXT_TRANS_NUM} Success")
    print()

    NEXT_TRANS_NUM += 1

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

    while True:
        Continue = input("Press Enter to Continue")
        if fV.EmptyVal(Continue) is True:
            main()


def view_defaults_file():

    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL

    print("            HAB Taxi Service")
    print("            ~~~~~~~~~~~~~~~~")
    print("             Default Values")
    print("----------------------------------------------")
    print(f" Next transaction ID:              {NEXT_TRANS_NUM:>10s}")
    print(f" Next Payment ID:                  {NEXT_PAYMENT_ID:>10s}")
    print(f" Next driver ID:                   {NEXT_DRIVER_NUM:<10}")
    print("----------------------------------------------")
    print(f" Monthly stand fee:                {fV.FDollar2(MONTH_STAND_FEE):<10}")
    print(f" Daily rental fee:                 {fV.FDollar2(DAY_RENT_FEE):<10}")
    print(f" Weekly rental fee:                {fV.FDollar2(WEEK_RENT_FEE):<10}")
    print(" HST rate: {:<10}   ".format(str(HST_RATE)))
    print("----------------------------------------------")

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

    while True:
        Continue = input("Press enter to go back to the main menu.")
        if fV.EmptyVal(Continue) is True:
            main()


def record_employee_payment():

    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL

    PaymentDate = datetime.today()
    PaymentDate = fV.FDateS(PaymentDate)

    print("_________________________________________")
    print("||  HAB Taxi Service Payment Recorder  ||  ")
    print("-----------------------------------------")

    while True:
        DriverNum = input("Enter driver number of payee: ")
        if fV.EmptyVal(DriverNum) is True:
            print("Please re-enter the driver number")
        elif fV.ValSetNum(DriverNum) is False:
            print("Driver Number is numeric digits only.")
        else:
            break

    while True:
        PayAmt = input("Enter the payment amount: ")
        if fV.EmptyVal(PayAmt) is True:
            print("Please enter the amount to be paid down")
        elif fV.ValSetNum(PayAmt) is False:
            print("Please enter numeric digits only.")
        else:
            PayAmt = fV.FDollar2(int(PayAmt))
            break

    while True:
        PayReason = input("Enter the reason for the payment: ")
        if fV.EmptyVal(PayReason) is True:
            print("Please enter the reason for payment")
        else:
            break
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

    p = open("PaymentRec.dat", "a")

    p.write("{}, ".format(str(NEXT_PAYMENT_ID)))
    p.write("{}, ".format(DriverNum))
    p.write("{}, ".format(PaymentDate))
    p.write("{}, ".format(PayAmt))
    p.write("{}, ".format(PayReason))
    p.write("{}\n".format(PayMethod))

    p.close()

    print("Payment information has been saved.")
    NEXT_PAYMENT_ID += 1

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

    p.close()


def new_driver():

    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID, \
        NEXT_RENTAL_ID, ProDay, MONTH_PAY_VAL

    DriverNum = NEXT_DRIVER_NUM

    BalDue = 0
    print()
    print("_________________________________________")
    print("||          HAB Taxi Service           ||")
    print("-----------------------------------------")
    print("          ENTER A NEW EMPLOYEE           ")

    while True:
        DriverFName = input("First name: ").title()
        if DriverFName == "" or DriverFName == " ":
            print("Please enter drivers first name.")
        else:
            break

    while True:
        DriverLName = input("Last name: ").title()
        if DriverLName == "" or DriverLName == " ":
            print("Please enter drivers last name.")
        else:
            break

    while True:
        StAdd = input("Street Address: ").title()
        if StAdd == "" or StAdd == " ":
            print("Please enter the Driver's address.")
        else:
            break

    while True:
        PhoneNum = input("Phone Number: ")
        if len(PhoneNum) != 10:
            print("Please input a 10 digit phone number")
        elif not PhoneNum.isdigit():
            print("Phone number must be digits only.")
        else:
            break

    while True:
        LicenseNum = input("License Number: ")
        if LicenseNum == "" or LicenseNum == " ":
            print("Please enter the Driver's License number.")
        else:
            break

    while True:
        ExpiryDate = input("Expiry Date(YYYY-MM-DD): ")

        try:   #
            ExpiryDate = fV.FDateInput(ExpiryDate)
            ExpDate = fV.FDateS(ExpiryDate)
            break
        except ValueError:
            print("Invalid date format, please re-enter")


    while True:
        InsurCompany = input("Insurance Company: ")
        if InsurCompany == "" or InsurCompany == " ":
            print("Please enter the insurance company.")
        else:
            break

    while True:
        PolicyNum = input("Policy Number: ")
        if not PolicyNum.isdigit():
            print("Policy numbers in this case are digit only. Please re-enter.")
        else:
            break

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

    if OwnCar == "Yes":
        print("This Employee will use their own car.")
    elif OwnCar == "No":
        print("This employee will need a rental.")


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

    e.close()

    print()
    print("Employee information has been saved.")
    NEXT_DRIVER_NUM += 1

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

            if OwnCar == "N":
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
    print("8. Your report -- (add description here)")
    print("9. Quit Program.")



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
            print("Unavailable")
        elif Ans == "7":
            print("Unavailable")
        # Option 8
        elif Ans == "8":
            view_defaults_file()

        elif Ans == "9":
            quit()

        else:
            print("Options are (1-9). Please re-enter. ")


if __name__ == "__main__":    # Program will start on the main menu function
    main()
