from datetime import datetime, timedelta
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
NEXT_RENTAL_ID = int(f.readline())

f.close()
def rental_tracker():

    RentCost = 0

    TransactDesc = "Rental"

    print()
    print("_________________________________________")
    print("||   HAB Taxi Service Rental Tracker   ||  ")
    print("-----------------------------------------")
    print("     Please Enter Rental Information")
    print()
    DriverNum = input("Driver number of renter: ")

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

    f = open("Rental.dat", "a")

    f.write("{}, ".format(str(NEXT_RENTAL_ID)))
    f.write("{}, ".format(str(DriverNum)))
    f.write("{}, ".format(str(RentStart)))
    f.write("{}, ".format(str(CarNum)))
    f.write("{}, ".format(str(RentType)))
    f.write("{}, ".format(str(RentDays)))
    f.write("{}, ".format(str(RentCost)))
    f.write("{}, ".format(str(HST)))
    f.write("{}\n".format(str(TotalCost)))

    f.close()

    print(f"              Rental ID: {NEXT_RENTAL_ID} for {CarNum} to driver {DriverNum}")
    print("                  Has been successfully saved")

    NEXT_RENTAL_ID += 1


    f = open("Revenue.dat", "a")

    f.write("{}, ".format(str(NEXT_TRANS_NUM)))
    f.write("{}, ".format(str(ProDay)))
    f.write("{}, ".format(str(TransactDesc)))
    f.write("{}, ".format(str(DriverNum)))
    f.write("{}, ".format(str(RentCost)))
    f.write("{}, ".format(str(HST)))
    f.write("{}\n".format(str(TotalCost)))

    f.close()

    print()
    print(f"Transaction {NEXT_TRANS_NUM} Success")

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

    e.close()

    while True:
        Continue = input("Press Enter to Continue")
        if fV.EmptyVal(Continue) is True:
            main()