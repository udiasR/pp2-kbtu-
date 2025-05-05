import psycopg2
import json
from tabulate import tabulate

# Database configuration - replace with your credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "postgres",
    "password": "yourpassword",
    "database": ""
}

class PhoneBook:
    def __init__(self):
        self.conn = self.connect_db()
        self.setup_database()

    def connect_db(self):
        """Establish database connection"""
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            print("✅ Database connection established")
            return conn
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            exit(1)

    def setup_database(self):
        """Create tables and stored procedures"""
        with self.conn.cursor() as cur:
            # Create phonebook table
            cur.execute("""
            DROP TABLE IF EXISTS phonebook;
            CREATE TABLE phonebook (
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                surname VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL
            )
            """)
            
            # Create stored procedures
            procedures = [
                # Search by pattern function
                """
                CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
                RETURNS TABLE (id INT, name VARCHAR, surname VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY 
                    SELECT * FROM phonebook 
                    WHERE name ILIKE '%' || pattern || '%' 
                       OR surname ILIKE '%' || pattern || '%'
                       OR phone ILIKE '%' || pattern || '%';
                END;
                $$ LANGUAGE plpgsql;
                """,
                
                # Upsert procedure
                """
                CREATE OR REPLACE PROCEDURE upsert_user(
                    p_name VARCHAR, p_surname VARCHAR, p_phone VARCHAR
                ) AS $$
                BEGIN
                    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name AND surname = p_surname) THEN
                        UPDATE phonebook SET phone = p_phone 
                        WHERE name = p_name AND surname = p_surname;
                    ELSE
                        INSERT INTO phonebook (name, surname, phone) 
                        VALUES (p_name, p_surname, p_phone);
                    END IF;
                END;
                $$ LANGUAGE plpgsql;
                """,
                
                # Bulk insert procedure
                """
                CREATE OR REPLACE PROCEDURE bulk_insert_users(
                    INOUT invalid_data REFCURSOR, users_data JSON
                ) AS $$
                DECLARE
                    user_data JSON;
                BEGIN
                    OPEN invalid_data FOR
                    SELECT 'Invalid phone' AS error, value::TEXT AS data
                    FROM json_array_elements(users_data)
                    WHERE NOT (value->>'phone' ~ '^\\d+$');
                    
                    FOR user_data IN SELECT * FROM json_array_elements(users_data)
                    LOOP
                        IF user_data->>'phone' ~ '^\\d+$' THEN
                            CALL upsert_user(
                                user_data->>'name',
                                user_data->>'surname',
                                user_data->>'phone'
                            );
                        END IF;
                    END LOOP;
                END;
                $$ LANGUAGE plpgsql;
                """,
                
                # Pagination function
                """
                CREATE OR REPLACE FUNCTION get_paginated(lim INT, offs INT)
                RETURNS TABLE (id INT, name VARCHAR, surname VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY
                    SELECT * FROM phonebook
                    ORDER BY user_id
                    LIMIT lim OFFSET offs;
                END;
                $$ LANGUAGE plpgsql;
                """,
                
                # Delete procedure
                """
                CREATE OR REPLACE PROCEDURE delete_user(p_identifier TEXT) AS $$
                BEGIN
                    IF p_identifier ~ '^\\d+$' THEN
                        DELETE FROM phonebook WHERE phone = p_identifier;
                    ELSE
                        DELETE FROM phonebook 
                        WHERE name = p_identifier OR surname = p_identifier;
                    END IF;
                END;
                $$ LANGUAGE plpgsql;
                """
            ]
            
            for proc in procedures:
                try:
                    cur.execute(proc)
                except Exception as e:
                    print(f"⚠️ Error creating procedure: {e}")
            
            self.conn.commit()
    
    def search_records(self, pattern):
        """Search by name, surname or phone pattern"""
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
            results = cur.fetchall()
            if results:
                print(tabulate(results, headers=["ID", "Name", "Surname", "Phone"]))
            else:
                print("🔍 No results found")

    def add_or_update_user(self, name, surname, phone):
        """Insert new or update existing user"""
        with self.conn.cursor() as cur:
            try:
                cur.callproc('upsert_user', (name, surname, phone))
                self.conn.commit()
                print("✅ Operation successful")
            except Exception as e:
                print(f"❌ Error: {e}")

    def bulk_insert_users(self, users):
        """Insert multiple users with validation"""
        with self.conn.cursor() as cur:
            try:
                cur.callproc('bulk_insert_users', (json.dumps(users),))
                invalid = cur.fetchall()
                if invalid:
                    print("⚠️ Invalid records:")
                    print(tabulate(invalid, headers=["Error", "Data"]))
                self.conn.commit()
                print("✅ Valid records inserted")
            except Exception as e:
                print(f"❌ Error: {e}")

    def show_paginated(self, limit, offset):
        """Display records with pagination"""
        with self.conn.cursor() as cur:
            cur.callproc('get_paginated', (limit, offset))
            results = cur.fetchall()
            if results:
                print(tabulate(results, headers=["ID", "Name", "Surname", "Phone"]))
            else:
                print("📄 No records in this range")

    def remove_user(self, identifier):
        """Delete by name, surname or phone"""
        with self.conn.cursor() as cur:
            try:
                cur.callproc('delete_user', (identifier,))
                self.conn.commit()
                print(f"🗑️ Deleted: {identifier}")
            except Exception as e:
                print(f"❌ Error: {e}")

    def run(self):
        """Main application interface"""
        while True:
            print("\n📞 PhoneBook Management System")
            print("1. 🔍 Search records")
            print("2. ✏️ Add/Update user")
            print("3. 📥 Bulk insert users")
            print("4. 📄 Paginated view")
            print("5. 🗑️ Delete user")
            print("6. ❌ Exit")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                pattern = input("Search pattern: ")
                self.search_records(pattern)
            
            elif choice == "2":
                name = input("Name: ")
                surname = input("Surname: ")
                phone = input("Phone: ")
                self.add_or_update_user(name, surname, phone)
            
            elif choice == "3":
                users = []
                print("Enter users (leave name blank to finish):")
                while True:
                    name = input("Name: ")
                    if not name: break
                    surname = input("Surname: ")
                    phone = input("Phone: ")
                    users.append({"name": name, "surname": surname, "phone": phone})
                self.bulk_insert_users(users)
            
            elif choice == "4":
                try:
                    limit = int(input("Limit: "))
                    offset = int(input("Offset: "))
                    self.show_paginated(limit, offset)
                except ValueError:
                    print("❌ Numbers only")
            
            elif choice == "5":
                identifier = input("Name, surname or phone to delete: ")
                self.remove_user(identifier)
            
            elif choice == "6":
                print("👋 Goodbye!")
                self.conn.close()
                break
            
            else:
                print("❌ Invalid option")

if __name__ == "__main__":
    app = PhoneBook()
    app.run()