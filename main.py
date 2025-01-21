# Name: Lisette Ruano
# Class: CS 341, Fall 2024
# Overview: Project 2 - Part 3 - Chicago Lobbyist Database App
#
import sqlite3
import objecttier

def findLobbyist(dbConn):
    print()
    
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
    lobbyists = objecttier.get_lobbyists(dbConn, name)

    print()
    print("Number of lobbyists found:", len(lobbyists)) 

    if len(lobbyists) == 0:
        return
    elif len(lobbyists) > 100:
        print()
        print("There are too many lobbyists to display, please narrow your search and try again...")
    else:
        print()
        for l in lobbyists:
           print(l.Lobbyist_ID, ":", l.First_Name, l.Last_Name, "Phone:", l.Phone)


def findLobbyistDetails(dbConn):
    print()

    id = input("Enter Lobbyist ID: ")
    print()

    details = objecttier.get_lobbyist_details(dbConn, id)

    if details is None:
        print("No lobbyist with that ID was found.")
    else:
        print(details.Lobbyist_ID, ":")
        print("  Full Name:", details.Salutation, details.First_Name, details.Middle_Initial, details.Last_Name, details.Suffix)
        print("  Address:", details.Address_1, details.Address_2, ",", details.City, ",",details.State_Initial, details.Zip_Code, details.Country)
        print("  Email:", details.Email)
        print("  Phone:", details.Phone)
        print("  Fax:", details.Fax)
        print("  Years Registered:", end=" ")
        for year in details.Years_Registered:
            print(year, end=", ")
        print()
        print("  Employers:", end=" ")
        for emp in details.Employers:
            print(emp, end=", ")
        print()
        print("  Total Compensation:", f"${details.Total_Compensation:,.2f}")



def topNLobbyists(dbConn):
    print()

    n_value = int(input("Enter the value of N: "))

    if n_value < 1:
        print("Please enter a positive value for N...")
    else:
        year = input("Enter the year: ")

        nLobbyists = objecttier.get_top_N_lobbyists(dbConn, n_value, year)

        if nLobbyists is None:
            return

        counter = 1
        print()
        for l in nLobbyists:
            print(counter, ".", l.First_Name, l.Last_Name)
            print("  Phone:", l.Phone)
            print("  Total Compensation:", f"${l.Total_Compensation:,.2f}")
            print("  Clients:", end=" ")
            for c in l.Clients:
                print(c, end=", ")
            print()

            counter = counter+1
      

    

def registerYear(dbConn):
    print()
    
    year = input("Enter year: ")
    id = input("Enter the lobbyist ID: ")
    
    result = objecttier.add_lobbyist_year(dbConn, id, year)

    if result == 0 or result == -1:
        print()
        print("No lobbyist with that ID was found.")
    else:
        print()
        print("Lobbyist successfully registered.")


def setSalutation(dbConn):
    print()

    id = input("Enter the lobbyist ID: ")
    sal = input("Enter the salutation: ")
    
    result = objecttier.set_salutation(dbConn, id, sal)

    if result == 0 or result == -1:
        print()
        print("No lobbyist with that ID was found.")
    else:
        print()
        print("Salutation successfully set.")






##################################################################  
#
# main
#
print('** Welcome to the Chicago Lobbyist Database Application **')
dbConn = sqlite3.connect('Chicago_Lobbyists.db')
print()

print("General Statistics:")

total_lobbyists = objecttier.num_lobbyists(dbConn)
total_employers = objecttier.num_employers(dbConn)
total_clients = objecttier.num_clients(dbConn)

print("  Number of Lobbyists:", f"{total_lobbyists:,}")
print("  Number of Employers:", f"{total_employers:,}")
print("  Number of Clients:", f"{total_clients:,}")
print()


cmd = input("Please enter a command (1-5, x to exit): ")

while cmd != "x":
    if cmd == "1":
        findLobbyist(dbConn)
    elif cmd == "2":
        findLobbyistDetails(dbConn)
    elif cmd == "3":
        topNLobbyists(dbConn)
    elif cmd == "4":
        registerYear(dbConn)
    elif cmd == "5":
        setSalutation(dbConn)
    else:
        print("**Error, unknown command, try again...")

    print()
    cmd = input("Please enter a command (1-5, x to exit): ")

dbConn.close()

#
# done
#
