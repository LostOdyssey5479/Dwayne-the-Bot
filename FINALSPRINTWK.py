# COMMENT LIKE A PRO
# AUTHOR JON IVANY
# DATE: 2022-12-12

from datetime import datetime, timedelta
import matplotlib
import math


def new_driver():


    f = open("Defaults.dat", "r")

    NEXT_TRANS_NUM = int(f.readline())
    NEXT_DRIVER_NUM = int(f.readline())
    MONTH_STAND_FEE = float(f.readline())
    DAY_RENT_FEE = float(f.readline())
    WEEK_RENT_FEE = float(f.readline())
    HST_RATE = float(f.readline())

    f.close()

    print()
    print("-ENTER A NEW DRIVER-")
    print()

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
        ExpiryDate = input("Expiry Date: ")
        if ExpiryDate == "" or ExpiryDate == " ":
            print("Please enter the license expiry date.")
        else:
            break

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

    print("HAB Taxi Services")
    print("Employee Information")
    print("First name: {:<10}".format(DriverFName))
    print("Last name: {:<10}".format(DriverLName))
    print("Address: {:<10}".format(StAdd))
    print("Phone number: {:<10}".format(PhoneNum))
    print("License number: {:<10}".format(LicenseNum))
    print("Expiry date: {:<10}".format(ExpiryDate))
    print("Insurance company: {:<10}".format(InsurCompany))
    print("Policy number: {:<10}".format(PolicyNum))
    print(f"Own Car?: {OwnCar}")

    f.write("{}, ".format(str(NEXT_DRIVER_NUM)))
    f.write("{}, ".format(DriverFName))
    f.write("{}, ".format(DriverLName))
    f.write("{}, ".format(StAdd))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(LicenseNum))
    f.write("{}, ".format(ExpiryDate))
    f.write("{}, ".format(InsurCompany))
    f.write("{}, ".format(PolicyNum))
    f.write("{}\n".format(OwnCar))

    f.close()

    print()
    print("Employee information has been saved.")
    NEXT_DRIVER_NUM += 1

    f = open("Defaults.dat", "w")

    f.write("{}\n".format(str(NEXT_TRANS_NUM)))
    f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
    f.write("{}\n".format(str(MONTH_STAND_FEE)))
    f.write("{}\n".format(str(DAY_RENT_FEE)))
    f.write("{}\n".format(str(WEEK_RENT_FEE)))
    f.write("{}\n".format(str(HST_RATE)))

    f.close()


def main():

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
            print("Unavailable")
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


if __name__ == "__main__":
    main()
