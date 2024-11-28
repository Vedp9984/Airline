import subprocess as sp
import getpass
from db_connection import connect_to_db
from employee import hireAnEmployee, fireAnEmployee, promoteEmployee, getEmployeeDetails, getEmployeesByAirport, getAverageSalaryByAirport
from airport import addAirport, deleteAirport, getAirlinesByAirport, getFlightsByAirlineAtAirport
from passenger import getTotalBaggageWeightByPassenger, searchPassengerByName
from airline import deleteAirline
from baggage import deleteBaggage

def dispatch(ch, cur, con):
    if ch == 1:
        hireAnEmployee(cur, con)
    elif ch == 2:
        fireAnEmployee(cur, con)
    elif ch == 3:
        promoteEmployee(cur, con)
    elif ch == 4:
        addAirport(cur, con)
    elif ch == 5:
        deleteAirport(cur, con)
    elif ch == 6:
        getEmployeesByAirport(cur)
    elif ch == 7:
        getAirlinesByAirport(cur)
    elif ch == 8:
        getAverageSalaryByAirport(cur)
    elif ch == 9:
        getFlightsByAirlineAtAirport(cur)
    elif ch == 10:
        getTotalBaggageWeightByPassenger(cur)
    elif ch == 11:
        searchPassengerByName(cur)
    elif ch == 12:
        deleteAirline(cur, con)
    elif ch == 13:
        deleteBaggage(cur, con)
    else:
        print("Error: Invalid Option")

if __name__ == "__main__":
    while True:
        tmp = sp.call('clear', shell=True)
        
        username = input("Username: ")
        password = getpass.getpass("Enter MySQL password: ")

        con, cur = connect_to_db(username, password)
        if con and cur:
            tmp = sp.call('clear', shell=True)
            print("Connected")
            tmp = input("Enter any key to CONTINUE>")

            while True:
                tmp = sp.call('clear', shell=True)
                print("1. Hire an Employee")
                print("2. Fire an Employee")
                print("3. Promote Employee")
                print("4. Add Airport")
                print("5. Delete Airport")
                print("6. Get details of all employees working at a specific airport")
                print("7. Get airlines operating at a specific airport")
                print("8. Get average salary of all employees at a specific airport")
                print("9. Get number of flights operated by each airline at a specific airport")
                print("10. Get total baggage weight for each passenger on a specific flight")
                print("11. Search Passenger by Name")
                print("12. Delete Airline")
                print("13. Delete Baggage")
                print("14. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 14:
                    exit()
                else:
                    dispatch(ch, cur, con)
                    tmp = input("Enter any key to CONTINUE>")
        else:
            tmp = sp.call('clear', shell=True)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            tmp = input("Enter any key to CONTINUE>")