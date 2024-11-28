def hireAnEmployee(cur, con):
    try:
        row = {}
        print("Enter new employee's details: ")
        row["Emp_id"] = input("Employee ID: ").strip()
        row["F_name"] = input("First Name: ").strip()
        row["M_name"] = input("Middle Name (or leave blank): ").strip()
        row["L_name"] = input("Last Name: ").strip()
        row["Jobtype"] = input("Job Type: ").strip()
        row["Salary"] = float(input("Salary: ").strip())
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ").strip()

        cur.execute("SELECT Airline_ID, Airline_name FROM Airline")
        airlines = cur.fetchall()
        print("Select Works For (Airline ID) from the following airlines:")
        for airline in airlines:
            print(f"ID: {airline['Airline_ID']}, Name: {airline['Airline_name']}")
        row["Works_For"] = input("Works For (Airline ID): ").strip()

        cur.execute("SELECT Emp_id, F_name, L_name FROM Flight_Employee")
        employees = cur.fetchall()
        print("Select Manager ID from the following employees (leave blank if none):")
        for emp in employees:
            print(f"ID: {emp['Emp_id']}, Name: {emp['F_name']} {emp['L_name']}")
        row["ManagerID"] = input("Manager ID: ").strip() or None

        query = """
        INSERT INTO Flight_Employee 
        (Emp_id, F_name, M_name, L_name, Jobtype, Salary, Bdate, Works_For, ManagerID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            row["Emp_id"], row["F_name"], row["M_name"], row["L_name"], row["Jobtype"],
            row["Salary"], row["Bdate"], row["Works_For"], row["ManagerID"]))
        con.commit()
        print("Inserted into database")

    except ValueError:
        print("Invalid input. Please enter data in the correct format.")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print("Error details:", repr(e))


def fireAnEmployee(cur, con):
    try:
        emp_id = input("Enter Employee ID to fire: ").strip()

        query = "DELETE FROM Flight_Employee WHERE Emp_id = %s"
        cur.execute(query, (emp_id,))
        if cur.rowcount == 0:
            print("No employee found with the given ID.")
        else:
            con.commit()
            print("Employee fired from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print("Error details:", repr(e))


def promoteEmployee(cur, con):
    try:
        emp_id = input("Enter Employee ID to promote: ").strip()
        new_salary = float(input("Enter new salary: ").strip())

        query = "UPDATE Flight_Employee SET Salary = %s WHERE Emp_id = %s"
        cur.execute(query, (new_salary, emp_id))
        if cur.rowcount == 0:
            print("No employee found with the given ID.")
        else:
            con.commit()
            print("Employee promoted in the database")

    except ValueError:
        print("Invalid salary. Please enter a numeric value.")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print("Error details:", repr(e))

def getEmployeeDetails(cur):
    try:
        emp_id = input("Enter Employee ID to get details: ").strip()
        query = """
        SELECT F_name, M_name, L_name, Phone_No 
        FROM Flight_Employee 
        JOIN Employee_Phone ON Flight_Employee.Emp_id = Employee_Phone.PID 
        WHERE Flight_Employee.Emp_id = %s
        """
        cur.execute(query, (emp_id,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"First Name: {row['F_name']}, Middle Name: {row['M_name']}, Last Name: {row['L_name']}, Phone Number: {row['Phone_No']}")
        else:
            print("No employee found with the given ID.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))


def employeeStatistics(cur):
    try:
        query = "SELECT Jobtype, AVG(Salary) AS Average_Salary FROM Flight_Employee GROUP BY Jobtype"
        cur.execute(query)
        results = cur.fetchall()

        if results:
            for row in results:
                print(f"Job Type: {row['Jobtype']}, Average Salary: {row['Average_Salary']:.2f}")
        else:
            print("No data found in the database.")

    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))

def getEmployeesByAirport(cur):
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

        airport_name = input("Enter Airport Name to get employee details: ").strip()
        query = """
        SELECT Emp_id, F_name, M_name, L_name, Phone_No 
        FROM Flight_Employee 
        JOIN Employee_Phone ON Flight_Employee.Emp_id = Employee_Phone.PID 
        JOIN Airline ON Flight_Employee.Works_For = Airline.Airline_ID
        JOIN Operates ON Airline.Airline_ID = Operates.AirlineID
        WHERE Operates.AirportID = %s
        """
        cur.execute(query, (airport_name,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Emp ID: {row['Emp_id']}, First Name: {row['F_name']}, Middle Name: {row['M_name']}, Last Name: {row['L_name']}, Phone Number: {row['Phone_No']}")
        else:
            print("No employees found for the given airport.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))

def getAverageSalaryByAirport(cur):
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

        airport_name = input("Enter Airport Name to get average salary details: ").strip()
        query = """
        SELECT AVG(Salary) AS Average_Salary
        FROM Flight_Employee 
        JOIN Airline ON Flight_Employee.Works_For = Airline.Airline_ID
        JOIN Operates ON Airline.Airline_ID = Operates.AirlineID
        WHERE Operates.AirportID = %s
        """
        cur.execute(query, (airport_name,))
        result = cur.fetchone()
        if result and result['Average_Salary'] is not None:
            print(f"Average Salary of employees at {airport_name}: {result['Average_Salary']:.2f}")
        else:
            print("No employees found for the given airport.")
    except Exception as e:
        print("Failed to retrieve data from database")
        print("Error details:", repr(e))