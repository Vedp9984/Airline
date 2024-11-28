def addAirplane(cur, con):
    try:
        row = {}
        print("Enter new airplane's details: ")
        row["AirplaneID"] = input("Airplane ID: ")
        row["SeatingCapacity"] = int(input("Seating Capacity: "))

        query = "INSERT INTO Airplane (AirplaneID, SeatingCapacity) VALUES ('%s', %d)" % (
            row["AirplaneID"], row["SeatingCapacity"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deleteAirplane(cur, con):
    try:
        airplane_id = input("Enter Airplane ID to delete: ")
        query = "DELETE FROM Airplane WHERE AirplaneID = '%s'" % airplane_id
        cur.execute(query)
        con.commit()
        print("Airplane deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
