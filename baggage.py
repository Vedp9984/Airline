def deleteBaggage(cur, con):
    try:
        # Fetch and display existing baggage
        cur.execute("SELECT BaggageId, BelongsTo FROM Baggage")
        baggage = cur.fetchall()
        print("Select the baggage to delete from the following:")
        for bag in baggage:
            print(f"Baggage ID: {bag['BaggageId']}, Belongs To: {bag['BelongsTo']}")
        
        baggage_id = input("Enter Baggage ID to delete: ")
        belongs_to = input("Enter Passenger ID to delete: ")

        # Check if the baggage ID and passenger ID exist
        cur.execute("SELECT BaggageId FROM Baggage WHERE BaggageId = %s AND BelongsTo = %s", (baggage_id, belongs_to))
        if cur.fetchone() is None:
            print("No baggage found with the given ID and passenger ID.")
            return

        query = "DELETE FROM Baggage WHERE BaggageId = %s AND BelongsTo = %s"
        cur.execute(query, (baggage_id, belongs_to))
        con.commit()
        print("Baggage deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)