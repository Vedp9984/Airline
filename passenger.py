def addPassenger(cur, con):
    try:
        row = {}
        print("Enter new passenger's details: ")
        row["PID"] = input("Passenger ID: ")
        row["BoardingFlight"] = input("Boarding Flight (Flight Code): ")

        query = "INSERT INTO Passenger (PID, BoardingFlight) VALUES ('%s', '%s')" % (
            row["PID"], row["BoardingFlight"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deletePassenger(cur, con):
    try:
        pid = input("Enter Passenger ID to delete: ")
        query = "DELETE FROM Passenger WHERE PID = '%s'" % pid
        cur.execute(query)
        con.commit()
        print("Passenger deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def addFirstClassPassenger(cur, con):
    try:
        pid = input("Enter Passenger ID to promote to First Class: ")
        query = "INSERT INTO First_Class_Passenger (PID) VALUES ('%s')" % pid
        cur.execute(query)
        con.commit()
        print("Passenger promoted to First Class")

    except Exception as e:
        con.rollback()
        print("Failed to promote passenger to First Class")
        print(">>>>>>>>>>>>>", e)

def addBusinessClassPassenger(cur, con):
    try:
        pid = input("Enter Passenger ID to promote to Business Class: ")
        query = "INSERT INTO Business_Class_Passenger (PID) VALUES ('%s')" % pid
        cur.execute(query)
        con.commit()
        print("Passenger promoted to Business Class")

    except Exception as e:
        con.rollback()
        print("Failed to promote passenger to Business Class")
        print(">>>>>>>>>>>>>", e)

def getTotalBaggageWeightByPassenger(cur):
    try:
        flight_code = input("Enter Flight Code to get baggage weight details: ").strip()
        query = """
        SELECT Passenger.F_name, Passenger.M_name, Passenger.L_name, SUM(Baggage.Weight) AS Total_Weight
        FROM Passenger
        JOIN Baggage ON Passenger.PID = Baggage.BelongsTo
        WHERE Passenger.BoardingFlight = %s
        GROUP BY Passenger.PID
        """
        cur.execute(query, (flight_code,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Passenger: {row['F_name']} {row['M_name']} {row['L_name']}, Total Baggage Weight: {row['Total_Weight']} kg")
        else:
            print("No baggage found for the given flight.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))

def searchPassengerByName(cur):
    try:
        name = input("Enter Passenger Name to search: ").strip()
        query = """
        SELECT PID, F_name, M_name, L_name, Bdate, BoardingFlight
        FROM Passenger
        WHERE F_name LIKE %s OR M_name LIKE %s OR L_name LIKE %s
        """
        search_term = f"%{name}%"
        cur.execute(query, (search_term, search_term, search_term))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Passenger ID: {row['PID']}, Name: {row['F_name']} {row['M_name']} {row['L_name']}, Birth Date: {row['Bdate']}, Boarding Flight: {row['BoardingFlight']}")
        else:
            print("No passengers found with the given name.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))