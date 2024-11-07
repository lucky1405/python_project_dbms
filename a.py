import mysql.connector
from datetime import date

# def clear():
#     for _ in range(65):
#         print()\
        
def print_hello():
    print("Hello World")
    

# creating tables
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="Photography_Management")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Photography_Management")
mycursor.execute("USE Photography_Management")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee(
        employee_id INT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        specialization VARCHAR(100) NOT NULL,
        phone_no INT
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer(
        customer_id INT PRIMARY KEY,
        customer_first_name VARCHAR(100) NOT NULL,
        customer_last_name VARCHAR(100) NOT NULL,
        customer_phone_no VARCHAR(15) 
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Services(
        service_id INT PRIMARY KEY,
        service_name VARCHAR(100) NOT NULL,
        description VARCHAR(100) NOT NULL,
        price VARCHAR(15) 
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Booking (
        booking_id INT PRIMARY KEY AUTO_INCREMENT,
        service_id INT,
        customer_id INT,
        FOREIGN KEY (service_id) REFERENCES Services(service_id),
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    );
""")

mycursor.execute("""
   CREATE TABLE IF NOT EXISTS Bill (
        payment_id INT PRIMARY KEY AUTO_INCREMENT,
        booking_id INT,
        customer_id INT,
        amount DECIMAL(10, 2),
        payment_date DATE,
        FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    );
""")

# For Employee
def employee_exist(employee_id):
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    sql = 'select * from Employee where employee_id =' + str(employee_id) + ';'
    cursor.execute(sql)
    record = cursor.fetchone()
    return record     

def show_employees():
    # Connect to the Photography_Management database
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    # SQL query to select all employees
    cursor.execute("SELECT employee_id, first_name, last_name, specialization, phone_no FROM Employee")
    employees = cursor.fetchall()
    
    # Display the results
    print("\nEmployee List")
    print("-" * 50)
    for employee in employees:
        print(f"ID: {employee[0]}, Name: {employee[1]} {employee[2]}, Specialization: {employee[3]}, Phone: {employee[4]}")
    
    # Close the connection
    con.close()

def add_employee():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    print('Add New Employee - Screen')
    print('-' * 120)
    
    # Collect employee details from the user
    employee_id = int(input('\n Enter Employee Id : '))
    first_name = input('\n Enter First Name : ')
    last_name = input('\n Enter Second Name : ')
    specialization = input('\n Enter Specialization : ')
    phone_no = input('\n Enter Phone Number : ')  # Using input() here to handle the phone number as a string

    # SQL query to insert a new employee
    sql = "INSERT INTO Employee (employee_id, first_name, last_name, specialization, phone_no) VALUES (%s, %s, %s, %s, %s)"
    
    # Check if the employee already exists
    if not employee_exist(employee_id):
        cursor.execute(sql, (employee_id, first_name, last_name, specialization, phone_no))
        con.commit()  # Commit the transaction to save the new employee
        print(f'Employee {employee_id} added successfully!')
    else:
        print(f'\nEmployee ID {employee_id} already exists.')

    con.close()
    input('\n Press any key to continue...')

def delete_employee():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    # Collect employee ID to delete
    employee_id = int(input('Enter Employee Id To Be Deleted : '))
    
    # SQL query to delete the employee
    sql = "DELETE FROM Employee WHERE employee_id = %s"
    
    # Check if the employee exists before deleting
    if employee_exist(employee_id):
        cursor.execute(sql, (employee_id,))
        con.commit()  # Commit the deletion
        print(f'Employee {employee_id} deleted successfully!')
    else:
        print(f'\nEmployee ID {employee_id} does not exist.')

    con.close()
    input('\nPress any key to continue...') 

def modify_employee():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    print('Change Employee Information')
    print('*' * 120)
    print('1. First Name')
    print('2. Last Name')
    print('3. Specialization')
    print('4. Phone Number')

    choice = int(input('Enter your choice : '))
    field_name = ''
    
    if choice == 1:
        field_name = 'first_name'
    elif choice == 2:
        field_name = 'last_name'   
    elif choice == 3:
        field_name = 'specialization'
    elif choice == 4:
        field_name = 'phone_no'

    if field_name == '':
        print("Invalid choice, please select a valid option.")
        return

    employee_id = int(input('Enter Employee Id : '))
    value = input('Enter New Value : ')

    # Check if employee exists
    if not employee_exist(employee_id):
        print(f'Employee ID {employee_id} does not exist.')
        con.close()
        return

    # Construct the SQL query with parameterized values
    sql = f"UPDATE Employee SET {field_name} = %s WHERE employee_id = %s"
    
    # Execute the update query
    cursor.execute(sql, (value, employee_id))
    con.commit()  # Commit the changes to the database

    print(f'Employee ID {employee_id} updated successfully!')

    con.close()
    input('\nPress any key to continue...') 

# For Customer    
def customer_exist(customer_id):
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    sql = 'select * from Customer where customer_id =' + str(customer_id) + ';'
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def show_customers():
    # Connect to the Photography_Management database
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    # SQL query to select all customers
    cursor.execute("SELECT customer_id, customer_first_name, customer_last_name, customer_phone_no FROM Customer")
    customers = cursor.fetchall()
    
    # Display the results
    print("\nCustomer List")
    print("-" * 50)
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]} {customer[2]}, Phone: {customer[3]}")
    
    # Close the connection
    con.close()

def add_customer():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    print('Add New Customer - Screen')
    print('-' * 120)
    
    # Input customer details
    customer_id = int(input('\n Enter Customer Id : '))
    customer_first_name = input('\n Enter First Name : ')
    customer_last_name = input('\n Enter Second Name : ')
    customer_phone_no = input('\n Enter Phone Number : ')  # Phone number should be a string to handle special chars

    # Check if customer already exists
    res = customer_exist(customer_id)
    if res is None:
        # Use parameterized query to prevent SQL injection
        sql = "INSERT INTO Customer (customer_id, customer_first_name, customer_last_name, customer_phone_no) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (customer_id, customer_first_name, customer_last_name, customer_phone_no))
        con.commit()  # Commit the changes to the database
        print(f'Customer ID {customer_id} added successfully!')
    else:
        print(f'\nCustomer ID {customer_id} already exists.')

    con.close()
    input('\n Press any key to continue...')

def delete_customer():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    customer_id = int(input("Enter Customer Id To Be Deleted : "))
    
    # Ensure the customer exists before attempting to delete
    res = customer_exist(customer_id)
    if res is not None:
        # Use parameterized query to prevent SQL injection
        sql = "DELETE FROM Customer WHERE customer_id = %s"
        cursor.execute(sql, (customer_id,))
        con.commit()  # Commit the changes to the database
        print(f"Customer ID {customer_id} deleted successfully!")
    else:
        print(f"\nCustomer ID {customer_id} does not exist.")

    con.close()

    input('\nEnter any key to continue...')

def modify_customer():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    print('Change Customer Information')
    print('*' * 120)
    print('1. First Name')
    print('2. Last Name')
    print('3. Phone Number')

    choice = int(input('Enter your choice : '))
    
    # Map choice to the corresponding field in the database
    field_name = ''
    if choice == 1:
        field_name = 'customer_first_name'
    elif choice == 2:
        field_name = 'customer_last_name'   
    elif choice == 3:
        field_name = 'customer_phone_no'  # Corrected column name
    
    # Get the customer_id and the new value for the field
    customer_id = int(input('Enter Customer Id : '))
    value = input('Enter New Value : ')

    # Use parameterized queries to prevent SQL injection
    sql = f"UPDATE Customer SET {field_name} = %s WHERE customer_id = %s"
    
    # Check if the customer exists
    res = customer_exist(customer_id)
    if res is not None:
        cursor.execute(sql, (value, customer_id))  # Execute the query with parameters
        con.commit()  # Commit the changes
        print(f"Customer ID {customer_id} updated successfully!")
    else:
        print(f"\nCustomer ID {customer_id} does not exist.")
    
    con.close()
    input('\nEnter any key to continue...')      

# For Services
def service_exist(service_id):
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    sql = 'select * from Services where employee_id =' + str(service_id) + ';'
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def show_services():
    # Connect to the Photography_Management database
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    # SQL query to select all services
    cursor.execute("SELECT service_id, service_name, description, price FROM Services")
    services = cursor.fetchall()
    
    # Display the results
    print("\nService List")
    print("-" * 50)
    for service in services:
        print(f"ID: {service[0]}, Name: {service[1]}, Description: {service[2]}, Price: {service[3]}")
    
    # Close the connection
    con.close()

def add_service():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    print('Add New Service - Screen')
    print('-' * 120)
    
    service_id = int(input('\n Enter Service Id : '))
    service_name = input('\n Enter Service Name : ')
    description = input('\n Enter Description : ')
    price = input('\n Enter Price : ')  # Use input to allow for currency symbols or formatting
    
    # SQL query with parameterized input to prevent SQL injection
    sql = "INSERT INTO Services (service_id, service_name, description, price) VALUES (%s, %s, %s, %s)"
    
    # Check if the service already exists
    res = service_exist(service_id)
    if res is None:
        cursor.execute(sql, (service_id, service_name, description, price))  # Execute query with parameters
        con.commit()  # Commit the transaction
        print(f"Service with ID {service_id} added successfully!")
    else:
        print(f"\nService ID {service_id} already exists")
    
    con.close()
    input('\nPress any key to continue...')

def delete_service():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    service_id = int(input("Enter Service Id To Be Deleted : "))
    
    # Check if the service exists using the service_exist function
    res = service_exist(service_id)
    
    if res is not None:
        # Use a parameterized query to safely delete the service
        sql = "DELETE FROM Services WHERE service_id = %s"
        cursor.execute(sql, (service_id,))  # Pass service_id as a tuple
        con.commit()  # Commit the changes to the database
        print(f"\nService with ID {service_id} has been deleted.")
    else:
        print(f"\nService ID {service_id} does not exist.")
    
    con.close()
    input('\nEnter any key to continue...') 

def modify_service():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    print('Change Service Information')
    print('*' * 120)
    print('1. Service Name')
    print('2. Description')
    print('3. Price')

    choice = int(input('Enter your choice : '))
    field_name = ''
    
    if choice == 1:
        field_name = 'service_name'
    elif choice == 2:
        field_name = 'description'
    elif choice == 3:
        field_name = 'price'

    service_id = int(input('Enter Service Id : '))
    value = input('Enter New Value : ')

    # If price is chosen, ensure it is handled as a string (to account for currency symbols or formatting)
    if field_name == 'price':
        value = str(value)  # Ensure price is stored as string if required
    
    # Check if service exists
    res = service_exist(service_id)
    if res is not None:
        # Using parameterized query to prevent SQL injection
        sql = f"UPDATE Services SET {field_name} = %s WHERE service_id = %s"
        cursor.execute(sql, (value, service_id))  # Execute with parameters
        con.commit()  # Commit the changes to the database
        print(f"\nService with ID {service_id} updated successfully!")
    else:
        print(f"\nService ID {service_id} does not exist.")
    
    con.close()
    input('\nEnter any key to continue...') 


# For Bookong
def book_service():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()

    print('Book a New Service')
    print('-' * 120)

    # Get input from the user
    service_id = int(input('\nEnter Service Id: '))
    customer_id = int(input('\nEnter Customer Id: '))

    # Check if the service exists
    cursor.execute("SELECT * FROM Services WHERE service_id = %s", (service_id,))
    service = cursor.fetchone()
    
    # Check if the customer exists
    cursor.execute("SELECT * FROM Customer WHERE customer_id = %s", (customer_id,))
    customer = cursor.fetchone()

    if service and customer:
        # If both the service and customer exist, create the booking
        cursor.execute("INSERT INTO Booking (service_id, customer_id) VALUES (%s, %s)", (service_id, customer_id))
        con.commit()  # Commit the transaction to the database

        print(f"\nService with ID {service_id} has been booked for Customer with ID {customer_id}.")
    else:
        # Handle the case where service or customer does not exist
        if not service:
            print(f"\nService with ID {service_id} does not exist.")
        if not customer:
            print(f"\nCustomer with ID {customer_id} does not exist.")

    con.close()
    input('\nPress any key to continue...')  


# For Payment
def generate_bill():
    # Connect to the database
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()

    print('Generate Bill - Screen')
    print('-' * 120)
    
    # Get the booking_id and amount from the user
    booking_id = int(input('\nEnter Booking ID: '))
    amount = float(input('\nEnter Amount: '))

    # Check if the booking exists and get customer_id
    cursor.execute("SELECT customer_id FROM Booking WHERE booking_id = %s", (booking_id,))
    booking = cursor.fetchone()

    if booking:
        customer_id = booking[0]
        # Get today's date
        payment_date = date.today()

        # SQL to insert bill details into the Bill table
        sql = "INSERT INTO Bill (booking_id, customer_id, amount, payment_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (booking_id, customer_id, amount, payment_date))
        con.commit()  # Commit transaction

        print(f"\nBill generated successfully for Booking ID {booking_id} with amount {amount}.")
    else:
        print(f"\nBooking ID {booking_id} does not exist. Cannot generate bill.")

    # Close the connection
    con.close()
    input('\nPress any key to continue...')


def show_bills():
    # Connect to the Photography_Management database
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Photography_Management')
    cursor = con.cursor()
    
    # SQL query to select all bills
    cursor.execute("SELECT payment_id, booking_id, customer_id, amount, payment_date FROM Bill")
    bills = cursor.fetchall()
    
    # Display the results
    print("\nBill List")
    print("-" * 50)
    for bill in bills:
        print(f"Payment ID: {bill[0]}, Booking ID: {bill[1]}, Customer ID: {bill[2]}, Amount: {bill[3]}, Date: {bill[4]}")
    
    # Close the connection
    con.close()


def main_menu():
    while True:
        # clear()
        print('*' * 120)
        print('*' * 120)
        print('PHOTOGRAPHY MANAGEMENT SYSTEM')
        print('*' * 120)
        print('*' * 120)
        print("\n1. Admin")
        print("\n2. Employee")
        print("\n3. Customer")
        choice = int(input('Enter your choice...'))

        if(choice == 1):
            print("\n1. Employee")
            print("\n2. Customer")
            print("\n3. Services")
            print("\n4. Bill")
            choice1 = int(input("Enter your choice : "))

            if(choice1 == 1) :
                print("\n1. Show Employees")
                print("\n2. Add Employee")
                print("\n3. Delete Employees")
                print("\n4. Update Employees")
                choice11 = int(input("Enter your choice : "))

                if(choice11 == 1) :
                    show_employees()
                elif(choice11 == 2) :
                    add_employee()
                elif(choice11 == 3) :
                    delete_employee()
                elif(choice11 == 4) :
                    modify_employee()
                else :
                    break 

            elif(choice1 == 2) :
                print("\n1. Show Customers")
                print("\n2. Add Customer")
                print("\n3. Delete Customer")
                print("\n4. Update Customer")
                print("\n5. Generate Bill Of Customer")
                choice11 = int(input("Enter your choice : "))

                if(choice11 == 1) :
                    show_customers()
                elif(choice11 == 2) :
                    add_customer()
                elif(choice11 == 3) :
                    delete_customer()
                elif(choice11 == 4) :
                    modify_customer()
                elif(choice11 == 4) :
                    generate_bill()    
                else :
                    break  

            elif(choice1 == 3) :
                print("\n1. Show Services")
                print("\n2. Add Service")
                print("\n3. Delete Service")
                print("\n4. Update Service")
                choice11 = int(input("Enter your choice : "))

                if(choice11 == 1) :
                    show_services()
                elif(choice11 == 2) :
                    add_service()
                elif(choice11 == 3) :
                    delete_service()
                elif(choice11 == 4) :
                    modify_service()
                else :
                    break  

            elif(choice1 == 4) :
                print("\n1. Show Bills")
                choice11 = int(input("Enter your choice : "))

                if(choice11 == 1) :
                    show_bills()
                else :
                    break    

            else :
                break          

        elif(choice == 2):
            print("\n1. Show Other Employees")   
            print("\n2. Show Services")   
            print("\n3. Show Customer")
            choice2 = int(input("Enter your choice : "))

            if(choice2 == 1):
                show_employees()
            elif(choice2 == 2):
                show_services()
            elif(choice2 == 3):
                show_customers()
            else :
                exit()
        elif(choice == 3) :   
            print("\n1. Show Services")
            print("\n2. Show Bill")
            choice3 = int(input("Enter your choice : "))

            if(choice3 == 1) :
                show_services()
            elif(choice3 == 2) :
                show_bills()
            else :
                exit()

        else :
            exit()    


if __name__ == "__main__":
    main_menu()            