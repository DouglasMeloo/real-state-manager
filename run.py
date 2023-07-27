import os
import sqlite3

DATABASE = "./real_estate.db"
TABLE = "property_listings"

def validate_integer_input(prompt):
    while True:
        try: 
            value = int(input(prompt)):
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
            