
# Real Estate Manager
![Real State Manager](/assets/images/mainmenu.png)

Real Estate Manager is a Python command-line application that allows users to manage property listings. With this user-friendly software, users can add, view, update, and delete property listings stored in an encrypted SQLite database. Simplify your property management tasks with Real Estate Manager.

# Table of Contents
* [Technologies Used](#technologies-used)
    * [Language](#language)
    * [Libraries](#libraries)
    * [Frameworks & Tools](#frameworks--tools)
* [Deployment](#deployment)
  * [Heroku Deployment](#heroku-deployment)
  * [Run locally](#run-locally)
* [Design](#design)
  * [Features](#features)
  * [Potential Enhancements](#potential-enhancements)
* [User Experience](#user-experience)
* [Testing](#testing)
* [Credits](#credits)

# Technologies Used

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

# Deployment 
The Real Estate Manager project was developed using the powerful and user-friendly Visual Studio IDE. To showcase its functionality, the application has been deployed to Heroku from the GitHub repository. This deployment process involves version releasing, ensuring smooth updates, and seamless delivery of enhancements to end-users.

### Heroku Deployment
1. Set up a Heroku account and log in to the Heroku Dashboard.
2. Create a new app by clicking "New" in the top-right corner and selecting "Create new app" from the dropdown menu.
3. Provide a unique app name and choose the region closest to you (EU or USA).
4. Click on "Create App" to create the app on Heroku.
5. To run the project on Heroku, we need to install the required dependencies.
6. In the terminal, execute the command `pip3 freeze > requirements.txt` to create a list of dependencies in the `requirements.txt` file.
7. To support the dependencies, select "Add Buildpack" in the Heroku dashboard.
8. The order of buildpacks is essential. Add "Python" first and click "Save changes," then add "Node.js" as the second buildpack and click "Save changes" again. 
You can rearrange them by dragging if needed.
9. Navigate to the "Deploy" section and choose "GitHub" as the deployment method.
10. Connect your Heroku app to the GitHub repository by entering the repository name, clicking "Search," and then "Connect" when it appears below.
11. Select the branch you want to build your app from.
12. Optionally, you can enable "Automatic Deploys" to keep your app up to date with changes from the GitHub repository.
13. Wait for the app to build. Once it's ready, you will see the message "App was successfully deployed" along with a 'View' button that leads to your deployed link.

### Run locally
1. Login or Sign Up to GitHub and open the project [repository](https://github.com/DouglasMeloo/real-state-manager).
2. Click on the "Code" button and choose whether you want to clone with HTTPS, SSH, or GitHub CLI. Copy the provided link.
3. Open the terminal in your preferred code editor and navigate to the desired location for the cloned directory.
4. Type "git clone" into the terminal and paste the link you copied in the previous step, then press enter.
5. This will create a local clone of the repository on your machine.

#### Forking the GitHub Repository
1. Login or Sign Up to GitHub and open the project [repository](https://github.com/DouglasMeloo/real-state-manager).
2. Click the "Fork" button located in the top-right corner of the repository page.
3. A copy of the repository will now be in your own GitHub account, allowing you to propose changes or use it as a reference for another project.<p align="right">[(Back to Top)](#top)</p>

# Design 

### Features                                      
* Add a New Property: 
     * Users can add a new property to the database by providing details such as title, description, price, number of bedrooms, number of bathrooms, and location.
     ![Real State Manager](/assets/images/addnewproperty.gif)

* Update a Property:
     * Users can update the details of an existing property by entering the property's ID and then providing the new information for the title, description, price, bedrooms, bathrooms, and location.
     ![Real State Manager](/assets/images/updateproperty.gif)

* Delete a Property
     * Users can delete a property from the database by entering the property's ID. A confirmation prompt ensures the deletion is intentional.
     ![Real State Manager](/assets/images/deleteproperty.gif)

* View All Properties
     * Users can view all the properties currently stored in the database. The program displays the ID, title, description, price, number of bedrooms, number of bathrooms, and location for each property.
     ![Real State Manager](/assets/images/viewallproperty.gif)

* Data Validation
     * The program includes data validation to ensure that user inputs are correctly formatted and that appropriate data types are used. Users are prompted to reenter values if they provide invalid inputs.

* Database Persistence
     * The program uses an SQLite database to store property listings, ensuring that data is persisted between different program runs.

* How to Use
     * Run the real_estate_manager.py script.

* The main menu will be displayed with the following options:
![Real State Manager](/assets/images/menuoptions.png)

* Dependencies
     * The Real Estate Manager program uses the sqlite3 module, which is included in the Python standard library. <p align="right">[(Back to Top)](#top)</p>

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

* Please note that these potential enhancements are suggestions and can be tailored to meet specific project requirements and user needs.<p align="right">[(Back to Top)](#top)</p>

# User Experience

### Target Users 
* The Real Estate Manager is designed for individuals interested in managing and tracking property listings efficiently. Whether you are a real estate agent, property owner, or someone searching for properties, this user-friendly software provides a seamless experience to handle property information.

### User Stories
* As a user, I want to be able to add a new property to the database, allowing me to keep track of various property listings.
* As a user, I want the flexibility to update existing property details, such as title, description, price, bedrooms, bathrooms, and location, to ensure accurate and up-to-date information.
* As a user, I want the option to easily delete a property entry from the database if it becomes irrelevant or is no longer available.
* As a user, I expect the software to present all property listings in a well-organized manner, facilitating easy navigation and quick reference.
* As a user, I want the software to provide clear and informative error messages when I enter invalid data, helping me understand and correct any mistakes.

### How to Use
1. Start the Real Estate Manager: 
     * Launch the software, and it will connect to the real_estate.db database. The main menu will be displayed, providing various options.

2. Add a New Property:
     * Choose option "1" from the main menu to add a new property.
     * You will be prompted to input the property details:
     * Title: Enter a suitable title for the property.
     * Description: Provide a description of the property.
     * Price: Enter the property price as a positive integer.
     * Bedrooms: Enter the number of bedrooms as a positive integer.
     * Bathrooms: Enter the number of bathrooms as a positive integer.
     * Location: Specify the location of the property.

3. Update an Existing Property:
     * Choose option "2" from the main menu to update an existing property.
     * You will be asked to enter the ID of the property you want to update.
     * The software will display the current details of the property.
     * You can modify any property attribute, such as title, description, price, bedrooms, bathrooms, or location.
     * The software will validate that only positive integers are entered for price, bedrooms, and bathrooms.

4. Delete a Property:
     * Choose option "3" from the main menu to delete a property.
     * You will be asked to enter the ID of the property you want to delete.
     * The software will display the details of the property to confirm the deletion.
     * You must confirm the deletion by typing "yes" or cancel by typing "no."

5. View All Properties:
     * Choose option "4" from the main menu to view all property listings.
     * The software will display the ID, title, description, price, bedrooms, bathrooms, and location of each property.
     * If no properties are found, a message will indicate that there are no properties listed.

6. Exit the Real Estate Manager:
     * To exit the software, choose option "5" from the main menu.
     * All data will be securely saved, and the program will close.

7. User Guidance:
     * Throughout the process, the software provides clear instructions and ensures that users enter valid and appropriate data.
     * Positive integers are validated for specific property attributes to prevent data errors.
     * Each action in the Real Estate Manager is designed to be straightforward and user-friendly, making property management and tracking a seamless experience.<p align="right">[(Back to Top)](#top)</p>

# Testing

### Testing Process for Real Estate Manager Application 
The real estate manager application underwent rigorous testing to ensure that all functionalities work seamlessly, providing users with an easy and straightforward experience to manage property listings effectively.

* Test Approach:
During the development process, extensive testing was conducted using the terminal to identify and resolve any potential issues. The test approach included various scenarios with correct and incorrect user inputs to thoroughly evaluate the application's behavior and ensure it handles different situations gracefully.

* Test Cases and Results:
The following test cases were devised to cover the major features of the real estate manager application:

Feature                                       | Expected Outcome                                         | Testing Performed                                                | Result | Pass/Fail |
----------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|--------|-----------|
Add a new property                            | User enters valid property details.                     | Entered property is successfully added to the database, and the last inserted row ID is printed. | Pass   | Pass      |
Update a property                             | User enters an existing property ID and valid updated details. | Specified property is successfully updated with the new details. | Pass   | Pass      |
Delete a property                             | User enters an existing property ID and confirms the deletion. | Specified property is successfully deleted from the database. | Pass   | Pass      |
View all properties                           | The database contains multiple properties.               | All properties are displayed on the console.                   | Pass   | Pass      |
Exit                                          | User chooses to exit the program.                       | The program terminates gracefully.                           | Pass   | Pass      |
Validate Integer Input                       | User enters a positive integer.                         | The function correctly returns the entered value.              | Pass   | Pass      |
Validate Integer Input (Negative Scenario)    | User enters a negative integer or a non-integer value. | The function prompts the user until a valid positive integer is provided. | Pass   | Pass      |
Property Deletion with Wrong ID               | User attempts to delete a property with a wrong ID.    | Program displays "Property with the ID not found" message.    | Pass   | Pass      |
Property Update with Wrong ID                 | User attempts to update a property with a wrong ID.     | Program displays "Property with the ID not found" message.    | Pass   | Pass      |
Invalid Input for Price                       | User enters a non-numeric value for price.              | Program displays "Invalid input. Please enter a positive Integer" message. | Pass   | Pass      |
Invalid Input for Bathrooms                   | User enters a non-numeric value for bathrooms.          | Program displays "Invalid input. Please enter a positive Integer" message. | Pass   | Pass      |
Invalid Input for Bedrooms                    | User enters a non-numeric value for bedrooms.           | Program displays "Invalid input. Please enter a positive Integer" message. | Pass   | Pass      |
Invalid Main Menu Choice                      | User enters a number that doesn't correspond to a menu choice. | Program displays "Invalid Choice. Please try again" message. | Pass   | Pass      |

### Conclusion
Through comprehensive testing, we are confident that the real estate manager application is reliable and robust, meeting the needs and expectations of users. All test cases passed successfully, demonstrating that the application functions as intended and efficiently handles user inputs. By delivering a thoroughly tested real estate manager, we aim to provide users with a seamless experience to manage property listings effortlessly. 

### Bugs Fixed 
* [PEP8](https://pep8ci.herokuapp.com/#) Validator
During the PEP8 tests, the following errors were found in the real estate manager program:

1. E501 Line Too Long: Lines exceeding the maximum length (79 characters) were identified. This was fixed by breaking the long lines into smaller, readable chunks.
2. E302 Expected 2 Blank Lines, Found 1: Insufficient blank lines were observed between code blocks. The code was modified to include the required two blank lines for better readability.

* The issues were resolved in the following git commit:
commit: 743cdcb

# Credits

### References
* The development of this project drew insights and knowledge from the following sources:
  *  [Code Institute](https://codeinstitute.net/de/)
  *  [SQLite 3 Documentation](https://docs.python.org/3/library/sqlite3.html)
  *  [Python.org](https://peps.python.org/pep-0008/#introduction)
  *  [W3 Schools](https://www.w3schools.com/python/default.asp#gsc.tab=0)

### Acknowledgements 
* Thanks to my Mentor Graeme Taylor for their valuable guidance and continuous feedback during the project development.

* I wish to extend my heartfelt appreciation to Danilo Martins and Bruno Farias for the continuous support provided throughout the course. Our regular interactions have fostered a collaborative environment, allowing us to exchange ideas and insights, leading to mutual growth and improvement in our respective projects. <p align="right">[(Back to Top)](#top)</p>