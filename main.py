#!/usr/bin/python3

from utils import db

def select_all_customers(conn):
    """
    Displays a list of all customers in the database.

    :param conn: Connection to the database
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Customers
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_toothbrushes(conn):
    """
    Displays a list of all toothbrushes in the database.

    :param conn: Connection to the database
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Toothbrushes
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_materials(conn):
    """
    Displays a list of all materials in the database.

    :param conn: Connection to the database
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Materials
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_suppliers(conn):
    """
    Displays a list of all suppliers in the database.

    :param conn: Connection to the database
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Suppliers
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_toothbrushes_under_price(conn, price):
    """
    Displays a list of toothbrushes that are priced under or equal to the specified amount.

    :param conn: Connection to the database
    :param price: Maximum price for toothbrushes
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT toothbrush_model, toothbrush_price 
                FROM Toothbrushes 
                WHERE toothbrush_price <= ?
                """, (price,))

    rows = cur.fetchall()

    if len(rows) == 0:
        print("No toothbrushes found under or equal to €{:.2f}.".format(price))
    else:
        print("Toothbrushes under or equal to €{:.2f}:".format(price))
        for row in rows:
            print("{:<20} €{:.2f}".format(row[0], row[1]))

def select_non_plastic_toothbrushes(conn):
    """
    Returns a list of toothbrush models and colours that are not made of plastic.

    :param conn: Connection to the database
    :return: List of tuples representing toothbrush models and colours
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT toothbrush_model, toothbrush_colour
                FROM Toothbrushes
                EXCEPT
                SELECT toothbrush_model, toothbrush_colour
                FROM Toothbrushes
                JOIN ToothbrushesMaterials ON Toothbrushes.toothbrush_number = ToothbrushesMaterials.toothbrush_number
                JOIN Materials ON ToothbrushesMaterials.material_number = Materials.material_number
                WHERE material_name = 'Plastic'
                """)
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No non-plastic toothbrushes found.")
    else:
        print("Non-plastic toothbrushes:")
        for row in rows:
            print("{:<20} {}".format(row[0], row[1]))

def add_customer(conn, name, email):
    """
    Inserts a new customer into the database.

    :param conn: Connection to the database
    :param name: Name of the customer
    :param email: Email address of the customer
    """
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO Customers (customer_name, customer_email) 
                VALUES (?, ?)
                """, (name, email))
    conn.commit()
    print("Customer added successfully.")

def delete_customer(conn, customer_number):
    """
    Deletes a customer from the database.

    :param conn: Connection to the database
    :param customer_number: ID of the customer to be deleted
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT customer_number FROM Customers WHERE customer_number = ?
                """, (customer_number,))
    row = cur.fetchone()
    if row is None:
        print("Customer not found.")
        return
    cur.execute("""
                DELETE FROM Customers WHERE customer_number = ?
                """, (customer_number,))
    conn.commit()
    print("Customer deleted successfully.")

def update_customer(conn, customer_number, new_name, new_email):
    """
    Updates a customer record in the database.

    :param conn: Connection to the database
    :param customer_number: ID of the customer to be updated
    :param new_name: New name to be set for the customer
    :param new_email: New email address to be set for the customer
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT customer_number FROM Customers WHERE customer_number = ?
                """, (customer_number,))
    row = cur.fetchone()
    if row is None:
        print("Customer not found.")
        return
    cur.execute("""
                UPDATE Customers SET customer_name = ?, customer_email = ?
                WHERE customer_number = ?
                """, (new_name, new_email, customer_number))
    conn.commit()
    print("Customer updated successfully.")

def select_all_toothbrushes_materials_suppliers(conn):
    """
    Displays all toothbrushes, their materials, and their suppliers from the ToothbrushesMaterialsSuppliers view.

    :param conn: Connection to the database
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * FROM ToothbrushesMaterialsSuppliers
                """)
    rows = cur.fetchall()
    if not rows:
        print("No toothbrushes found.")
        return
    for row in rows:
        print(f"Toothbrush Number: {row[0]}\nToothbrush Model: {row[1]}\nToothbrush Colour: {row[2]}\nToothbrush Price: {row[3]}\nMaterial Name(s): {row[4]}\nSupplier Name(s): {row[5]}\nSupplier Address(es): {row[6]}\n")

def sum_order_total_price(conn):
    """
    Calculates the sum of all total order prices in the database.

    :param conn: Connection to the database
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT SUM(order_total_price)
                FROM Orders
                """)

    row = cur.fetchone()

    if row[0] is None:
        print("No orders found.")
    else:
        print("Sum of Orders: €{:.2f}".format(row[0]))

def main():
    # Name of the database file to create
    db_file = "data/EcoBrush.db"

    # Create a connection to the database
    conn = db.create_connection(db_file)

    # Initialize the database with some values
    print("Welcome to EcoBrush DB ♻️ 🥄\n")
    print("Creating the database and initializing it with some values.")
    db.update_database(conn, "data/Create.sql")
    db.update_database(conn, "data/Insert.sql")
    # Display menu and prompt user for input
    while True:
        print("\nSelect an option:")
        print("1.  Show all customers")
        print("2.  Show all toothbrushes")
        print("3.  Show all materials")
        print("4.  Show all suppliers")
        print("5.  Show toothbrushes under a certain price")
        print("6.  Show non-plastic toothbrushes")
        print("7.  Add a new customer")
        print("8.  Update a customer record")
        print("9.  Delete a customer")
        print("10. Show ToothbrushesMaterialsSuppliers view")
        print("11. Show the sum of all orders")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            select_all_customers(conn)
        elif choice == "2":
            select_all_toothbrushes(conn)
        elif choice == "3":
            select_all_materials(conn)
        elif choice == "4":
            select_all_suppliers(conn)
        elif choice == "5":
            price = float(input("Enter maximum price: "))
            select_toothbrushes_under_price(conn, price)
        elif choice == "6":
            select_non_plastic_toothbrushes(conn)
        elif choice == "7":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            add_customer(conn, name, email)
        elif choice == "8":
            customer_number = input("Enter customer number: ")
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            update_customer(conn, customer_number, name, email)
        elif choice == "9":
            customer_number = input("Enter customer number: ")
            delete_customer(conn, customer_number)
        elif choice == "10":
            select_all_toothbrushes_materials_suppliers(conn)
        elif choice == "11":
            sum_order_total_price(conn)
        elif choice == "12":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
