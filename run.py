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
    