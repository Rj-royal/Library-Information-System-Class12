import sqlite3
import matplotlib.pyplot as plt

# 1. DATABASE SETUP 
def setup_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS book (bookid INT, name TEXT, author TEXT, pdate TEXT, qty INT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS member (name TEXT, memberid INT, address TEXT, contact INT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS issue (bookid INT, issueid INT, date TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS returnbook (issueid INT, returnid INT, date TEXT)')
    conn.commit()
    return conn

# 2. LOGIC FROM YOUR PROJECT 
def late_fine_calculator(days):
    """Your original logic from p4.py"""
    if 0 < days <= 5:
        return 0.50 * days
    elif 6 <= days <= 10:
        return 1.0 * days
    elif days > 30:
        print("Your Membership would be Cancelled..")
        return 10 * days
    elif days > 10:
        return 5 * days
    return 0

# 3. VISUALIZATION 
def show_graph(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, qty FROM book")
    data = cursor.fetchall()
    if data:
        names, qties = zip(*data)
        plt.bar(names, qties, color='red')
        plt.xlabel("Book Name")
        plt.ylabel("Quantity")
        plt.title("Inventory Overview")
        plt.show()

# 4. MAIN INTERFACE
def main():
    conn = setup_db()
    while True:
        print("\n=== LIBRARY INFORMATION SYSTEM ===")
        print("1. Add Book\n2. Calculate Late Fine\n3. Show Inventory Graph\n4. Exit")
        choice = input("Enter Choice: ")
        
        if choice == '1':
            bid = int(input("Book ID: "))
            name = input("Name: ")
            qty = int(input("Quantity: "))
            conn.execute("INSERT INTO book (bookid, name, qty) VALUES (?, ?, ?)", (bid, name, qty))
            conn.commit()
        elif choice == '2':
            days = int(input("Enter Days Late: "))
            amt = late_fine_calculator(days)
            print(f"Fine Amount: Rs {amt}")
        elif choice == '3':
            show_graph(conn)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()