print("==================================")
print("     Train Ticket Automatic Gate ")
print("==================================")


# station information

print("\nStations: ")
print("1. station A")
print("2. station B")
print("3. station C")
print("4. station D")
print("5. station E")
print("6. station F")

# Fare settings
fare_per_station = 100
minimum_balance = 100

# passenger information
credential = input("\nEnter credential (teikiken / kippu / IC): ").lower()

entry_station = int(input("\nEnter a station (1-6): "))

entry_allowed = False


print("\n.....Entry gate .....")

# case-1: commuter pass

if credential == "teikiken":
    pass_valid = input("Is commuter pass valid? (yes/no): ").lower()

    pass_start = int(input("Enter pass starting station: "))
    pass_end = int(input("Enter pass ending station: "))

    if pass_valid == "yes" and pass_start <= entry_station <= pass_end:
        print("Commuter pass is valid.")
        print("LET GO: Open the gate>")
        entry_allowed = True

    else:
        print("commuter pass is not valid.")
        print("NO GO: Alarmed!")


# case-2: Paper ticket
elif credential == "kippu":
    ticket_origin = int(input("Enter the origin of ticke: "))
    ticket_paid = int(input("Enter the paid fare: "))

    if ticket_origin == entry_station and ticket_paid > 0:
        print("Ticket accepted!")
        print("Let Go: Open the gate")

        entry_allowed = True

    else:
        print("No Go: Ticket is not valid!")
        print("Alarmed!!!")

# case-3: IC-card
elif credential == "IC":
    balance = int(input("Enter IC card balance: "))

    if balance >= minimum_balance:
        print("Let Go: Open the Gate!")
        entry_allowed = True
    else:
        print("No Go: Insufficient Balance. Alarmed!")
        print("Please charge.")


else:
    print("No Go: Unknown credential.")
    print("Activate the Alarm!")


# ===============================
#         Exit
# ===============================

if entry_allowed:
    print("\n-------Exit Gate--------")

    exit_station = int(input("Enter exit station (1-6): "))

    journey_fare = abs(exit_station - entry_station) * fare_per_station

    print("Calculated journey fare: ¥", journey_fare)

    # case-1: teikiken
    if credential == "teikiken":
        if exit_station >= pass_start and exit_station <= pass_end:
            print("Destination within commuter pass limit")
            print("No additional charge")
            print("Let Go: Open the gate")

        else:
            if exit_station < pass_start:
                extra_stations = pass_start - exit_station

            else:
                extra_stations = exit_station - pass_end

            additional_fare = extra_stations * fare_per_station

            print("Destination is outside of commuter pass limit!")
            print("Additional Fare: ¥", additional_fare)

            balance = int(input("Enter IC card balance for extra fare: "))

            if balance >= additional_fare:
                balance = balance - additional_fare

                print("Additional fare paid!")
                print("Remaining balance: ¥", balance)

                print("Let Go: Open the gate!")

            else:
                print("No Go: Insufficient balance")
                print("Activate Alarm!")


    # Case -2: paper ticket
    elif credential == "kippu":
        if ticket_paid >= journey_fare:
            print("Let Go: Open the Gate!")

        else:
            print("Please call the station police!")
            print("Alarm Activated!")



    # case-3: IC card
    elif credential == "IC":

        if balance >= journey_fare:
            balance = balance - journey_fare

            print("Fare deducted successfully")
            print("Remaining balance: ¥", balance)

            print("Let go: Open the Gate.")


        else:
            print("No Go: Insufficient balance!")
            print("Alarm Activated!")

            print("Please call the station police!")


print("\n----------------------------")
print("          Journey Finished!")
print("------------------------------")



        