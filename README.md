Introduction:
.............
Welcome to the Contact Management System project! In this project, you will apply your Python programming skills to create a functional command-line-based application that simplifies the management of your contacts. The Contact Management System will empower you to add, edit, delete, and search for contacts with ease, all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.


Project Requirements:
......................
Task is to develop a Contact Management System with the following features:

User Interface (UI):
....................
Create a user-friendly command-line interface (CLI) for the Contact Management System.

Display a welcoming message and provide a menu with the following options:
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit 

Contact Data Storage:
.....................
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
Store contact details within the inner dictionary, including:

Name
Phone number
Email address
Additional information (e.g., address, notes).


Menu Actions:
..............
Implement the following actions in response to menu selections:
Adding a new contact with all relevant details.
Editing an existing contact's information (name, phone number, email, etc.).
Deleting a contact by searching for their unique identifier.
Searching for a contact by their unique identifier and displaying their details.
Displaying a list of all contacts with their unique identifiers.
Exporting contacts to a text file in a structured format.
Importing contacts from a text file and adding them to the system.


User Interaction:
.................
Utilize input() to enable users to select menu options and provide contact details.
Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

Error Handling:
...............
Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

GitHub Repository:
..................
Create a GitHub repository for your project.
Commit your code to the repository regularly.
Create a clean and interactive README.md file in your GitHub repository.
Include clear instructions on how to run the application and explanations of its features.
Provide examples and screenshots, if possible, to enhance user understanding.
Include a link to your GitHub repository in your project documentation.

Optional Features
.......................
Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.
Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.

Github repository link :
.......................

https://github.com/SwathyJagannatha/ContactMgmt.git

Prerequisites:
..............
Ensure you have Python installed on your system. You can download it from python.org and follow the installation instructions for your operating system.
You'll also need pip, Python's package installer, which usually comes with Python by default. Check if it's installed by running pip --version in your command line or terminal.

Steps to run the application:
.............................
Clone the repository:

1.Open your command line or terminal and clone the repository using Git:

git clone https://github.com/SwathyJagannatha/ContactMgmt.git

2.Navigate into the project directory:

cd ContactMgmt

3.Install dependencies:

pip install -r requirements.txt

This command installs all the required Python packages specified in the requirements.txt file.

4. Run the application:

python main.py

This command starts the application. Depending on how the application is structured, main.py might be the entry point script. If the structure is different, you might need to adjust this command based on the actual file structure.

