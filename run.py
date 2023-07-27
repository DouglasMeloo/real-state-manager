import os
import sqlite3

DATABASE = "./real_estate.db"
TABLE = "property_listings"

def validate_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Please enter a positive integer.")
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def create_house(connector):
    new_house = {
        "title" : "",
        "description" : "",
        "price" : 0,
        "bedrooms" : 0,
        "bathrooms" : 0,
        "location" : "",
    }

    for key in new_house:
        if key == "price" or key == "bedrooms" or key == "bathrooms":
            new_house[key] = validate_integer_input(f"Insert the {key}: ")
        else:
            new_house[key] = input(f"Insert the {key}: ")
            
    print(new_house)
    cursor = connector.cursor()
    sql_insert = f"INSERT INTO {TABLE} (title, description, price, bedrooms, bathrooms, location) VALUES (?, ?, ?, ?, ?, ?)"
    values = (new_house["title"], new_house["description"], new_house["price"], new_house["bedrooms"], new_house["bathrooms"], new_house["location"])
    cursor.execute(sql_insert, values)
    connector.commit()

    last_inserted_id = cursor.lastrowid
    print("Last inserted rowid:", last_inserted_id)

    cursor.close()

def update_property(connector):
    property_id = validate_integer_input("Enter the ID of property to update:")
    cursor = connector.cursor()
    cursor.execute(f"SELECT * FROM {TABLE} WHERE id = ? ", (property_id,))
    property_data = cursor.fetchone()
    cursor.close()

    if not property_data:
        print("Property with the given ID not found.")
        return
    
    print("Existing Property Details:")
    print("ID:", property_data[0])
    print("Title:", property_data[1])
    print("Description:", property_data[2])
    print("Price:", property_data[3])
    print("bedrooms:", property_data[4])
    print("Bathrooms:", property_data[5])
    print("Location:", property_data[6])

    new_house = {}
    for key in ["title", "description", "price", "bedrooms", "bathrooms", "location"]:
        if key == "price" or key == "bedrroms" or key == "bathrooms":
            new_house[key] = validate_integer_input(f"Enter the new {key}:")
        else:
            new_house[key] = input(f"Enter the new {key}:")

    cursor = connector.cursor()
    sql_update = f"""
        UPDATE {TABLE} SET title = ?, description = ?, price = ?, bedrooms = ?, bathrooms = ?, location = ?
        WHERE id = ?
    """

    values  = (
        new_house["title"],
        new_house["description"],
        new_house["price"],
        new_house["bedrooms"],
        new_house["bathrooms"],
        new_house["location"],
        property_id
    )

    cursor.execute(sql_update, values)
    connector.commit()
    cursor.close()
    print("Property updated successfully.")

def delete_property(connector):
    property_id = validate_integer_input("Enter the ID of property to delete:")
    cursor = connector.cursor()
    cursor.execute(f"SELECT * FROM {TABLE} WHERE id = ?", (property_id,))
    property_data = cursor.fetchone()
    cursor.close()

    if not property_data:
        print("Property with the given ID not found.")
        return
    
    print("Property Details to Delete:")
    print("ID:", property_data[0])
    print("Title:", property_data[1])
    print("Description:", property_data[2])
    print("Price:", property_data[3])
    print("Bedrooms:", property_data[4])
    print("Bathrooms:", property_data[5])
    print("Location:", property_data[6])
    
    confirmation = input("Are you sure you want to delete this property? (yes/no): ")
    if confirmation.lower() == "yes":
        cursor = connector.cursor()
        cursor.execute(f"DELETE FROM {TABLE} WHERE id = ?", (property_id,))
        connector.commit()
        cursor.close()
        print("Property deleted successfully.")
    else:
        print("Deletion canceled.")

def query_properties(connector):
    cursor = connector.cursor()
    cursor.execute(f"SELECT * FROM {TABLE}")
    properties = cursor.fetchall()
    cursor.close()

    if not properties:
        print("No properties found.")
    else:
        print("Property Listings:")
        for property_data in properties:
            print("ID:", property_data[0])
            print("Title:", property_data[1])
            print("Description:", property_data[2])
            print("Price:", property_data[3])
            print("Bedrooms:", property_data[4])
            print("Bathrooms:", property_data[5])
            print("Location:", property_data[6])
            print("--------------------")

def create_table(databasepath):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS property_listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL,
            bedrooms INTEGER NOT NULL,
            bathrooms INTEGER NOT NULL,
            location TEXT NOT NULL
        )
    """)
    
    connection.commit()
    return connection

def main():
    connector = create_table(DATABASE)

    while True:
        print("\n--- Real Estate Manager ---")
        print("1.Add a new property")
        print("2.Update a propery")
        print("3.Delete a property")
        print("4.View all properties")
        print("5.Exit")

        choice = input("Enter your choice(1/2/3/4/5):")

        if choice == "1":
            create_house(connector)
        elif choice == "2":
            update_property(connector)
        elif choice == "3":
            delete_property(connector)
        elif choice == "4":
            query_properties(connector)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    
    connector.close()

if __name__ == "__main__":
    main()