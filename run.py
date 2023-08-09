import os
import sqlite3

# Constants for the database file and table
DATABASE = "./real_estate.db"
TABLE = "property_listings"


class PropertyManager:
    def __init__(self):
        self.connector = self.create_table()

    def validate_integer_input(self, prompt):
        """
        Function to validate and get a positive integer input from the user
        """
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError("Please enter a positive integer.")
                return value
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def print_property_details(self, property_data):
        """
        Function to print property details
        """
        print("ID:", property_data[0])
        print("Title:", property_data[1])
        print("Description:", property_data[2])
        print("Price:", property_data[3])
        print("Bedrooms:", property_data[4])
        print("Bathrooms:", property_data[5])
        print("Location:", property_data[6])

    def create_house(self):
        """
        Function to create a new property entry in the database
        """
        new_house = {
            "title": "",
            "description": "",
            "price": 0,
            "bedrooms": 0,
            "bathrooms": 0,
            "location": "",
        }

        # Collect property details from the user
        for key in new_house:
            if key == "price" or key == "bedrooms" or key == "bathrooms":
                new_house[key] = self.validate_integer_input(f"Insert the {key}: ")
            else:
                new_house[key] = input(f"Insert the {key}: ")

        print(new_house)

        # Insert the new property into the database
        cursor = self.connector.cursor()
        sql_insert = (
            f"INSERT INTO {TABLE} (title, description, price, bedrooms, "
            f"bathrooms, location) VALUES (?, ?, ?, ?, ?, ?)"
        )
        values = (
            new_house["title"],
            new_house["description"],
            new_house["price"],
            new_house["bedrooms"],
            new_house["bathrooms"],
            new_house["location"],
        )
        cursor.execute(sql_insert, values)
        self.connector.commit()

        last_inserted_id = cursor.lastrowid
        """Get the last inserted row ID (primary key) and print it"""
        print("Last inserted rowid:", last_inserted_id)

        cursor.close()

    # Other methods from your original code go here...

    def main(self):
        """
        Main function to run the real estate manager program
        """
        while True:
            print("\n--- Real Estate Manager ---")
            print("1. Add a new property")
            print("2. Update a property")
            print("3. Delete a property")
            print("4. View all properties")
            print("5. Exit")

            choice = input("Enter your choice:")

            if choice == "1":
                self.create_house()
            elif choice == "2":
                self.update_property()
            elif choice == "3":
                self.delete_property()
            elif choice == "4":
                self.query_properties()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

        self.connector.close()

    # Additional methods and other parts of your original code go here...

    def create_table(self):
        """
        Function to create the database table if it does not exist
        """
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS property_listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                price INTEGER NOT NULL,
                bedrooms INTEGER NOT NULL,
                bathrooms INTEGER NOT NULL,
                location TEXT NOT NULL
            )
        """
        )

        connection.commit()
        return connection


if __name__ == "__main__":
    property_manager = PropertyManager()
    property_manager.main()
