
## Real Estate Manager

Real Estate Manager is a Python command-line application that allows users to manage property listings. With this user-friendly software, users can add, view, update, and delete property listings stored in an encrypted SQLite database. Simplify your property management tasks with Real Estate Manager.

## Table of Contents
* [Technologies Used](#technologies-used)
    * [Language](#language)
    * [Libraries](#libraries)
    * [Frameworks & Tools](#frameworks--tools)
* [Deployment](#deployment)
  * [Heroku Deployment](#heroku-deployment)
  * [Run locally](#run-locally)
* [Design](#design)
  * [Existing Features](#existing-features)
  * [Potential Enhancements](#potential-enhancements)
* [User Experience](#user-experience-ux)
* [Testing](#testing)
* [Credits](#credits)

## Technologies Used

### Language
* ![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python&logoColor=yellow)

    * The language of choice for this project was Python, specifically version 3.11.4

### Libraries
* ![os](https://img.shields.io/badge/OS-Library-yellow?logo=linux&logoColor=white) 

     * The project also made use of the "os" library, which enabled the clearing of the Python terminal. This feature contributed to a clean and user-friendly interface, enhancing the overall user experience.

* ![SQLite3](https://img.shields.io/badge/SQLite3-Library-yellow?logo=sqlite&logoColor=white) 

     * The project utilized the "SQLite3" library as its database management system, ensuring a secure and efficient storage and management of account credentials.

### Frameworks & Tools
* To facilitate the development process, this project utilized a [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which offered all the necessary files to run the mock terminal in the browser. This template served as a foundation, streamlining the setup and allowing developers to focus on implementing project-specific functionalities.

* ![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-yellow?logo=github&logoColor=white)

     * GitHub served as the repository for this project, providing a platform to store, manage, and collaborate on the project's source code and related files.

* ![Git Version Control](https://img.shields.io/badge/Git-Version%20Control-yellow?logo=git&logoColor=white)

     * The project utilized Git for version control, enabling efficient tracking of changes made during the development process.

* ![Heroku Deployed](https://img.shields.io/badge/Heroku-Deployed-yellow?logo=heroku&logoColor=white)

     * Heroku was employed to deploy a live view of the project, allowing users to access and interact with it online.

## Deployment 


## Design 

### Features
* Add a New Property:
     * Users can add a new property to the database by providing details such as title, description, price, number of bedrooms, number of bathrooms, and location.

* Update a Property:
     * Users can update the details of an existing property by entering the property's ID and then providing the new information for the title, description, price, bedrooms, bathrooms, and location.

* Delete a Property
     * Users can delete a property from the database by entering the property's ID. A confirmation prompt ensures the deletion is intentional.

* View All Properties
     * Users can view all the properties currently stored in the database. The program displays the ID, title, description, price, number of bedrooms, number of bathrooms, and location for each property.

* Data Validation
     * The program includes data validation to ensure that user inputs are correctly formatted and that appropriate data types are used. Users are prompted to reenter values if they provide invalid inputs.

* Database Persistence
     * The program uses an SQLite database to store property listings, ensuring that data is persisted between different program runs.

* How to Use
     * Run the real_estate_manager.py script.

* The main menu will be displayed with the following options:

*sql
--- Real Estate Manager ---
1. Add a new property
2. Update a property
3. Delete a property
4. View all properties
5. Exit
To perform an action, enter the corresponding number and press Enter:

Enter 1 to add a new property.
Enter 2 to update an existing property.
Enter 3 to delete a property.
Enter 4 to view all properties.
Enter 5 to exit the program.
Follow the on-screen prompts to complete the desired action.

* Dependencies
     * The Real Estate Manager program uses the sqlite3 module, which is included in the Python standard library.

### Potential Enhancements
* While the current version of the Real Estate Manager provides essential property management functionalities, there are several potential enhancements and additional features that could be implemented in the future to improve the program further:

* Search Functionality: 
     * Allow users to search for properties based on specific criteria such as location, price range, number of bedrooms, etc.

* Sorting:
     * Implement sorting options to view properties based on price, location, or other criteria.

* User Authentication:
     * Introduce user authentication to restrict access and provide security for the property management system.

* Property Images: 
     * Add support for property images to provide a visual representation of the listings.

* Multiple Locations: 
     * Allow users to add multiple locations for each property (e.g., city, state, country).

* Additional Property Details:
     * Extend the property data model to include additional details such as property type, square footage, amenities, etc.

* Rental Management: 
     * Introduce features for managing rental properties, including lease details and tenant information.

* Export/Import Functionality:
     * Enable users to export property data to a file or import data from other sources.

* GUI Interface: 
     * Develop a graphical user interface (GUI) for a more visually appealing and intuitive user experience.

* Reports and Analytics:
     * Provide statistical reports and analytics on property listings, such as average price, highest/lowest prices, etc.

* Online Database:
     * Implement cloud-based storage for the property database, allowing multiple users to access and manage property listings simultaneously.

* Currency Conversion: 
     * Support currency conversion for international property listings.

* Error Handling:
     * Enhance error handling to provide more informative and user-friendly error messages.

* Please note that these potential enhancements are suggestions and can be tailored to meet specific project requirements and user needs.