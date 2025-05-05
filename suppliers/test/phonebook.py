import psycopg2
import csv
from config import host, user, password, database

def create_phonebook_table(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    phone VARCHAR(20) NOT NULL UNIQUE
                )
            """)
            conn.commit()
            print("Phonebook table created successfully")
    except Exception as e:
        print("Error creating table:", e)
        conn.rollback()

def insert_from_console(conn):
    print("\nEnter contact details:")
    first_name = input("First name: ").strip()
    phone = input("Phone number: ").strip()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (first_name, phone)
            )
            conn.commit()
            print("Contact added successfully!")
    except Exception as e:
        print("Error adding contact:", e)
        conn.rollback()

def upload_from_csv(conn, filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            with conn.cursor() as cursor:
                for row in reader:
                    if len(row) >= 2:  # Ensure we have name and phone
                        cursor.execute(
                            "INSERT INTO phonebook (name, phone) VALUES (%s, %s) "
                            "ON CONFLICT (phone) DO NOTHING",
                            (row[0], row[1])
                        )
                conn.commit()
        print(f"Data uploaded from {filename} successfully!")
    except Exception as e:
        print("Error uploading from CSV:", e)
        conn.rollback()

def update_contact(conn):
    phone = input("\nEnter phone number to update: ").strip()
    new_name = input("Enter new first name: ").strip()
    new_phone = input("Enter new phone (leave blank to keep current): ").strip()
    
    try:
        with conn.cursor() as cursor:
            if new_phone:
                cursor.execute(
                    "UPDATE phonebook SET first_name = %s, phone = %s WHERE phone = %s",
                    (new_name, new_phone, phone)
                )
            else:
                cursor.execute(
                    "UPDATE phonebook SET first_name = %s WHERE phone = %s",
                    (new_name, phone)
                )
            conn.commit()
            print("Contact updated successfully!")
    except Exception as e:
        print("Error updating contact:", e)
        conn.rollback()

def search_contacts(conn):
    print("\nSearch options:")
    print("1. By name")
    print("2. By phone")
    choice = input("Enter choice (1-2): ").strip()
    
    try:
        with conn.cursor() as cursor:
            if choice == '1':
                name = input("Enter name to search: ").strip()
                cursor.execute(
                    "SELECT * FROM phonebook WHERE name ILIKE %s",
                    (f'%{name}%',)
                )
            elif choice == '2':
                phone = input("Enter phone to search: ").strip()
                cursor.execute(
                    "SELECT * FROM phonebook WHERE phone LIKE %s",
                    (f'%{phone}%',)
                )
            else:
                print("Invalid choice")
                return
            
            results = cursor.fetchall()
            if results:
                print("\nSearch results:")
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
            else:
                print("No contacts found")
    except Exception as e:
        print("Error searching contacts:", e)

def delete_contact(conn):
    phone = input("\nEnter phone number to delete: ").strip()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM phonebook WHERE phone = %s",
                (phone,)
            )
            conn.commit()
            print("Contact deleted successfully!" if cursor.rowcount > 0 else "Contact not found")
    except Exception as e:
        print("Error deleting contact:", e)
        conn.rollback()

def main():
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        create_phonebook_table(connection)
        
        while True:
            print("\nPhoneBook Menu:")
            print("1. Add contact (console)")
            print("2. Upload contacts (CSV)")
            print("3. Update contact")
            print("4. Search contacts")
            print("5. Delete contact")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                insert_from_console(connection)
            elif choice == '2':
                filename = input("Enter CSV filename: ").strip()
                upload_from_csv(connection, filename)
            elif choice == '3':
                update_contact(connection)
            elif choice == '4':
                search_contacts(connection)
            elif choice == '5':
                delete_contact(connection)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    except Exception as e:
        print("Error:", e)
    finally:
        if connection:
            connection.close()
            print("Database connection closed")

if __name__ == '__main__':
    main()