def addAirport(cur, con):
    try:
        row = {}
        print("Enter new airport's details: ")
        row["Ap_name"] = input("Airport Name: ")
        row["City"] = input("City: ")
        row["Country"] = input("Country: ")

        query = "INSERT INTO Airport (Ap_name, City, Country) VALUES ('%s', '%s', '%s')" % (
            row["Ap_name"], row["City"], row["Country"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deleteAirport(cur, con):
    try:
        # Fetch and display existing airports
        cur.execute("SELECT Ap_name FROM Airport")
        airports = cur.fetchall()
        if airports:
            print("Select Airport to delete from the following list:")
            for airport in airports:
                print(f"Airport: {airport['Ap_name']}")
        else:
            print("No airports found in the database.")
            return

        ap_name = input("Enter Airport Name to delete: ").strip()
        query = "DELETE FROM Airport WHERE Ap_name = %s"
        cur.execute(query, (ap_name,))
        if cur.rowcount == 0:
            print("No airport found with the given name.")
        else:
            con.commit()
            print("Airport deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)


def airportStatistics(cur):
    try:
        query = "SELECT Country, COUNT(*) AS Airport_Count FROM Airport GROUP BY Country"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            print(f"Country: {row['Country']}, Number of Airports: {row['Airport_Count']}")

    except Exception as e:
        print("Failed to retrieve data from database")
        print(">>>>>>>>>>>>>", e)

def getAirlinesByAirport(cur):
    try:
        # Fetch and display the list of airports
        cur.execute("SELECT Ap_name FROM Airport")
        airports = cur.fetchall()
        if airports:
            print("Select Airport from the following list:")
            for airport in airports:
                print(f"Airport: {airport['Ap_name']}")
        else:
            print("No airports found in the database.")
            return

        airport_name = input("Enter Airport Name to get airline details: ").strip()
        query = """
        SELECT Airline.Airline_ID, Airline.Airline_name 
        FROM Airline 
        JOIN Operates ON Airline.Airline_ID = Operates.AirlineID 
        WHERE Operates.AirportID = %s
        """
        cur.execute(query, (airport_name,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Airline ID: {row['Airline_ID']}, Airline Name: {row['Airline_name']}")
        else:
            print("No airlines found for the given airport.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))

def getFlightsByAirlineAtAirport(cur):
    try:
        # Fetch and display the list of airports
        cur.execute("SELECT Ap_name FROM Airport")
        airports = cur.fetchall()
        if airports:
            print("Select Airport from the following list:")
            for airport in airports:
                print(f"Airport: {airport['Ap_name']}")
        else:
            print("No airports found in the database.")
            return

        airport_name = input("Enter Airport Name to get flight details: ").strip()
        query = """
        SELECT Airline.Airline_name, COUNT(Flight.Flight_code) AS Flight_Count
        FROM Flight
        JOIN Flight_Employee ON Flight.Pilot = Flight_Employee.Emp_id
        JOIN Airline ON Flight_Employee.Works_For = Airline.Airline_ID
        JOIN Operates ON Airline.Airline_ID = Operates.AirlineID
        WHERE Operates.AirportID = %s
        GROUP BY Airline.Airline_name;
        """
        cur.execute(query, (airport_name,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Airline: {row['Airline_name']}, Number of Flights: {row['Flight_Count']}")
        else:
            print("No flights found for the given airport.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))