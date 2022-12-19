# HAB TAXI SERVICE
# AUTHOR JONATHAN IVANY, TYLER STUCKLESS, ALEXANDER GILLESPIE
# DATE: 2022-12-12

from datetime import datetime
import FormatValues as fV

ProDay = datetime.today()
ProDay = fV.FDateS(ProDay)

f = open("Defaults.dat", "r")

NEXT_TRANS_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTH_STAND_FEE = float(f.readline())
DAY_RENT_FEE = float(f.readline())
WEEK_RENT_FEE = float(f.readline())
HST_RATE = float(f.readline())
NEXT_PAYMENT_ID = int(f.readline())

f.close()


def record_employee_payment():

    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID
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

    p.close()


def new_driver():


    global NEXT_TRANS_NUM, NEXT_DRIVER_NUM, MONTH_STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE, NEXT_PAYMENT_ID
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
    e.write("{}, ".format(ExpiryDate))
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

    Ans = input("Enter choice (1-9): ")

    while True:
        # Option 1, 2 OR 3
        if Ans == "1":
            new_driver()
        elif Ans == "2":
            print("Unavailable")
        elif Ans == "3":
            print("Unavailable")
        # Option 4
        elif Ans == "4":
            print("Unavailable")
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
            print("Unavailable")

        elif Ans == "9":
            quit()

        else:
            print("Options are (1-9). Please re-enter. ")


if __name__ == "__main__":    # Program will start on the main menu function
    main()
