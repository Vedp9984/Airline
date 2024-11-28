def addAirline(cur, con):
    try:
        row = {}
        print("Enter new airline's details: ")
        row["Airline_ID"] = input("Airline ID: ")
        row["Airline_name"] = input("Airline Name: ")

        query = "INSERT INTO Airline (Airline_ID, Airline_name) VALUES ('%s', '%s')" % (
            row["Airline_ID"], row["Airline_name"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deleteAirline(cur, con):
    try:
        # Fetch and display existing airlines
        cur.execute("SELECT Airline_ID, Airline_name FROM Airline")
        airlines = cur.fetchall()
        print("Select the airline to delete from the following:")
        for airline in airlines:
            print(f"Airline ID: {airline['Airline_ID']}, Name: {airline['Airline_name']}")
        
        airline_id = input("Enter Airline ID to delete: ")

        # Check if the airline ID exists
        cur.execute("SELECT Airline_ID FROM Airline WHERE Airline_ID = %s", (airline_id,))
        if cur.fetchone() is None:
            print("No airline found with the given ID.")
            return

        query = "DELETE FROM Airline WHERE Airline_ID = %s"
        cur.execute(query, (airline_id,))
        con.commit()
        print("Airline deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
def airlineStatistics(cur):
    try:
        query = "SELECT Airline_name, COUNT(Flight_code) AS Flight_Count FROM Airline LEFT JOIN Flight ON Airline.Airline_ID = Flight.Pilot GROUP BY Airline.Airline_name"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            print(f"Airline: {row['Airline_name']}, Number of Flights: {row['Flight_Count']}")

    except Exception as e:
        print("Failed to retrieve data from database")
        print(">>>>>>>>>>>>>", e)
