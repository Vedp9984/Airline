def addFlight(cur, con):
    try:
        row = {}
        print("Enter new flight's details: ")
        row["Flight_code"] = input("Flight Code: ")

        # Fetch and display existing airports for Source
        cur.execute("SELECT Ap_name FROM Airport")
        airports = cur.fetchall()
        print("Select Source (Airport) from the following airports:")
        for airport in airports:
            print(f"Airport: {airport['Ap_name']}")
        row["Source"] = input("Source (Airport): ")

        # Fetch and display existing airports for Destination
        print("Select Destination (Airport) from the following airports:")
        for airport in airports:
            print(f"Airport: {airport['Ap_name']}")
        row["Destination"] = input("Destination (Airport): ")

        # Fetch and display existing airplanes for AirplaneID
        cur.execute("SELECT AirplaneID, Aircraft_Model FROM Airplane")
        airplanes = cur.fetchall()
        print("Select Airplane ID from the following airplanes:")
        for airplane in airplanes:
            print(f"Airplane ID: {airplane['AirplaneID']}, Model: {airplane['Aircraft_Model']}")
        row["AirplaneID"] = input("Airplane ID: ")

        # Fetch and display existing employees for Pilot
        cur.execute("SELECT Emp_id, F_name, L_name FROM Flight_Employee")
        employees = cur.fetchall()
        print("Select Pilot (Employee ID) from the following employees:")
        for emp in employees:
            print(f"ID: {emp['Emp_id']}, Name: {emp['F_name']} {emp['L_name']}")
        row["Pilot"] = input("Pilot (Employee ID): ")
        if not row["Pilot"].startswith("PL"):
            raise ValueError("Pilot ID must begin with 'PL'")

        row["Arrival"] = input("Arrival (YYYY-MM-DD HH:MM:SS): ")
        row["Departure"] = input("Departure (YYYY-MM-DD HH:MM:SS): ")

        query = "INSERT INTO Flight (Flight_code, Source, Destination, AirplaneID, Pilot, Arrival, Departure) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            row["Flight_code"], row["Source"], row["Destination"], row["AirplaneID"], row["Pilot"], row["Arrival"], row["Departure"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deleteFlight(cur, con):
    try:
        flight_code = input("Enter Flight Code to delete: ")
        query = "DELETE FROM Flight WHERE Flight_code = '%s'" % flight_code
        cur.execute(query)
        con.commit()
        print("Flight deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

