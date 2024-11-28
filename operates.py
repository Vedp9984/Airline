def addOperates(cur, con):
    try:
        row = {}
        print("Enter new operates relationship details: ")

        # Fetch and display existing airports
        cur.execute("SELECT Ap_name FROM Airport")
        airports = cur.fetchall()
        print("Select Airport ID from the following airports:")
        for airport in airports:
            print(f"Airport ID: {airport['Ap_name']}")
        row["AirportID"] = input("Airport ID: ")

        # Fetch and display existing airlines
        cur.execute("SELECT Airline_ID, Airline_name FROM Airline")
        airlines = cur.fetchall()
        print("Select Airline ID from the following airlines:")
        for airline in airlines:
            print(f"Airline ID: {airline['Airline_ID']}, Name: {airline['Airline_name']}")
        row["AirlineID"] = input("Airline ID: ")

        query = "INSERT INTO Operates (AirportID, AirlineID) VALUES ('%s', '%s')" % (
            row["AirportID"], row["AirlineID"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deleteOperates(cur, con):
    try:
        # Fetch and display existing operates relationships
        cur.execute("SELECT AirportID, AirlineID FROM Operates")
        operates = cur.fetchall()
        print("Select the operates relationship to delete from the following:")
        for operate in operates:
            print(f"Airport ID: {operate['AirportID']}, Airline ID: {operate['AirlineID']}")
        
        airport_id = input("Enter Airport ID: ")
        airline_id = input("Enter Airline ID: ")

        query = "DELETE FROM Operates WHERE AirportID = '%s' AND AirlineID = '%s'" % (airport_id, airline_id)
        cur.execute(query)
        con.commit()
        print("Operates relationship deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)