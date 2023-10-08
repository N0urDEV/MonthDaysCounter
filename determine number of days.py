def determine_number_of_days():
    mois = int(input("Please enter the month (1 for January, 2 for February, etc.): "))

    if mois in [1, 3, 5, 7, 8, 10, 12]:
        nbreJours = 31
    elif mois in [4, 6, 9, 11]:
        nbreJours = 30
    elif mois == 2:
        nbreJours = 28
    else:
        print("Invalid month.")
        return

    print("Month", mois, "has", nbreJours, "days.")
determine_number_of_days()
