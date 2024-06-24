
from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date
import shutil
import os
import json
import ast
from datetime import datetime

contact_info_restore={}

class InvalidOptionException(Exception):
    "Raised when the user provides invalid input when prompted to chose from the list!!"
    pass

def validate_input(prompt_val):
    while True:
     try:
          user_ip = input(prompt_val).strip()
          if not user_ip:
               raise ValueError("The field cant be empty,Please provide a value!")
          else:
               return user_ip
     except Exception as e:
          print(e)

def add_contact(contact_info):
    # take in all the details of the contact
    # add the entry into contact dict
    print("Please enter details to add you as our contact!!")
    user_name = validate_input("Please enter your name!")

    if user_name in contact_info:
        print("Sorry, contact with that name already exists!!")

    try:
        user_email = validate_input("Please enter your personal email!")
       
        user_phonenum = validate_input("Please enter your phone number!")
          
        user_alternate_phone = validate_input("Please enter your alternate phone number!")
              
        user_address = validate_input("Please enter your address!")
                       
        user_cool_facts = validate_input("Please enter one cool fact!")

    except Exception as e:
         print("Sorry , please enter all the required details!!")

    contact_info[user_email] = {
         "name" : user_name,
         "phone_number" : user_phonenum,
         "alternate_number" : user_alternate_phone,
         "email": user_email,
         "additional_info": {
              "address": user_address,
              "notes": user_cool_facts
         }
    }

    print("Sucess! Details are submitted to form a contact")
    for key,value in contact_info.items():
        print(f"{Fore.CYAN}ID : {Fore.YELLOW}{key}{Style.RESET_ALL}")
        for Field,Value in value.items():
          print(f"- {Fore.GREEN} {Field} : {Fore.LIGHTMAGENTA_EX} {Value}{Style.RESET_ALL}")

def export_contact(contact_info):
    file_name = input("Enter the filename from which you want to start the export process!!")
    if not file_name:
        print("File name is mandatory!!")
        return
    try:
     with open(file_name, "w") as file:   
       for key,value in contact_info.items():
          file.write("\n")
          file.write( "ID :" + key +"\n\n")
          for Field,field_value in value.items():
            file.write( f"{Field} : {field_value}\n")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except PermissionError:
        print(f"Error: Insufficient permissions to read the file {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Export process finally!!")  
    pass

def import_contact(contact_info): # not adding contacts 
    file_name = input("Enter the filename from which you want to start the import process!!")
    if not file_name:
        print("File name is mandatory!!")
        return
   
    try:
     with open(file_name, "r") as file:
        current_id = None
        current_info = {}

        for line in file:
            if not isinstance(line,str):
                print(f"Skipping lines which arent strings : {line} ")
                continue
            line = str(line).strip()
            
            if line.startswith("ID:"):
                if current_id is not None:
                    contact_info[current_id] = current_info
                current_id = line.split(":",1)[1].strip()
                current_info = {}
            elif line:
                key, value = line.split(":", 1)
                if key.strip() == "additional_info":
                        value = ast.literal_eval(value.strip())
                current_info[key.strip()] = value.strip()

        if current_id is not None:
            contact_info[current_id] = current_info
        print(contact_info)
     
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except PermissionError:
        print(f"Error: Insufficient permissions to read the file {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    #print("Noww displaying the Contact Information from dictionary:")
    #display_contact(contact_info)

def edit_contact(contact_info):
     try:
        user_ip = input("Please enter your email address(to fetch you unique ID)")
        if user_ip in contact_info:
            user_val = input("Please enter the field you would like to update? (name/phone_number/address/notes/alternate_number)")
            print(user_val)
        else:
             print("Invalid user id")

        accepted_fields =["name","phone_number","address","notes","alternate_number"] 

        if user_val.strip() not in accepted_fields:
             raise ValueError("Email address or Field value cant be empty!!")
        else:
             user_field_val = input("Please enter the field value you would like to update?")

        if not user_val or not user_ip or not user_field_val:
             raise ValueError("Email address or Field value cant be empty!!")
           
        if user_val == "name":
            contact_info[user_ip]["name"] = user_field_val
        elif user_val == "phone_number":
            contact_info[user_ip]["phone_number"] = user_field_val
        elif user_val == "alternate_number":
            contact_info[user_ip]["alternate_number"] = user_field_val
        elif user_val == "address":
            contact_info[user_ip]["additional_info"]["address"] = user_field_val
        elif user_val == "notes":
            contact_info[user_ip]["notes"] = user_field_val
     except ValueError:
          print("Please enter a proper field for editing the contact!!")
     except Exception as e:
          print("Sorry exception e encountered")
     finally:
          print("Contact Edit operation function was invoked!!")
          print("Contact information after update:")
          display_contact(contact_info)
     pass

def display_contact(contact_info):
     print("Sucess! Details are submitted to form a contact\n")
     print("displaying contacts existing ones\n")
     for key,value in contact_info.items():
        print(f"{Fore.CYAN}ID : {Fore.YELLOW}{key}{Style.RESET_ALL}")
        for Field,Value in value.items():
            print(f"- {Fore.GREEN} {Field} : {Fore.LIGHTMAGENTA_EX} {Value}{Style.RESET_ALL}")
     pass

def search_contact(contact_info):
     search_ip = input("Please enter your email for searching your contact info:\n")

     if search_ip.strip() in contact_info:
          print(contact_info[search_ip])
          contact_val = contact_info[search_ip]
          print("Contact details information:")
          print(f"""-------------------------------
                    Contact found for {search_ip}
                    -------------------------------
                "Name" : {contact_val["name"]},
                "Phone Number" : {contact_val["phone_number"]},
                "Alternate Number" : {contact_val["alternate_number"]},
                "Address" : {contact_val["additional_info"]["address"]},
                "Notes" : {contact_val["additional_info"]["notes"]}
                """)
     else:
          print("Sorry unable to fetch the details!!Please enter Id already present in the system!!")
          user_ip = input("Do you want to enter details for adding your contact?")
          if user_ip == "yes":
            add_contact(contact_info)
     pass

def search_by_fields(contact_info):
    user_search = input("Enter your search term, for fetching your contact details!!")
    
    if not user_search:
        print("Please enter the search field!")
    # search by name , phone_number, email address or others 
    # currently works when searched by name / phone no / email / alternate no
    for key,value in contact_info.items():
        if user_search in key:
            print(f"{key} : {value}")
        else:
          for fields, field_val in value.items():    
            if user_search in field_val:
                  print("search_by_field")
                  print(user_search)
                  print(f"{key} - {value}")
                   
            else:
               pass
    pass

def save_contacts_json(contact_info):
    user_input = input("Please enter the json file name, to save contact details!")
    with open(user_input,"w") as file:
        json.dump(contact_info,file,indent=4)
        print(f"Contact Info saved succesfully to {user_input}")
    create_backup(user_input)  

def create_backup(json_file):
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    #timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    #backup_file = os.path.join(backup_dir, f"Contact_backup_{timestamp}.json")
    backup_file = os.path.join(backup_dir, "Contact_backup.json")
                               
    # Copy the source directory to the backup directory
    shutil.copy2(json_file,backup_file)
    print(f"Backup created at {backup_file}")

def restore_backup(contact_info_restore):
    user_ip = input("Enter the json file from which you want to restore backup")
    try:
          with open(user_ip,"r") as file:
               data = json.load(file)

          contact_info_restore = data
          print(contact_info_restore) 

    except FileNotFoundError: 
      print("The specified backup file does not exist!")

    except PermissionError: 
      print("Insufficient permissions to read the file")

    except IOError: 
     print("General I/O error while handling the file")

    except json.JSONDecodeError: 
       print("The JSON data is malformed")

    except TypeError: 
       print("Issues with the data format or type")

    except Exception as e:
        print("Sorry, The following error is encountered!" , e)

def delete_contact(contact_info):
     delete_id = input("Please enter your email for deleting your contact info:\n")

     if delete_id.strip() in contact_info:
          print(contact_info[delete_id])
          contact_val = contact_info[delete_id]

          del contact_info[delete_id]
          print("Contact details after delete:")

          display_contact(contact_info)

     else:
          print("Sorry unable to fetch the details!!Please enter Id already present in the system!!")
          user_ip = input("Do you want to enter details for adding your contact?")
          if user_ip == "yes":
            add_contact(contact_info)
          else:
            search_contact(contact_info)
     pass

#delete_contact(contact_info)

def display_contact_id(contact_info):
    contact_id = input("Please enter you email for displaying your contact details!")

    if contact_id in contact_info:
        print("Sucess! Details are submitted to form a contact\n")
        print("displaying contacts existing ones\n")
        for key,value in contact_info.items():
          print(f"{Fore.CYAN}ID : {Fore.YELLOW}{key}{Style.RESET_ALL}")
          for Field,Value in value.items():
            print(f"- {Fore.GREEN} {Field} : {Fore.LIGHTMAGENTA_EX} {Value}{Style.RESET_ALL}")
    pass

def add_custom_fields(contact_info):
     contact_id = input("Please enter you email for displaying your contact details!")

     try: 
          if contact_id in contact_info:
               birth_day = input("Enter your birthdate to update your contact")
               Anniversary = input("Enter your Anniversary date for updating your contact")
               contact_info[contact_id]["birthdays"] = birth_day
               contact_info[contact_id]["Anniversary_day"] = Anniversary
          else:
               raise ValueError("Sorry your entered Id doesnt match the existing Contact details!!")
     except ValueError:
         print("Please enter a valid Id or create a new one!!")
     finally:
         print("This is a function for adding birthdays and anniversaries!!")
         print("Displaying details after adding custom Fields::")
         for key,value in contact_info.items():
          print(f"{Fore.CYAN}ID : {Fore.YELLOW}{key}{Style.RESET_ALL}")
          for Field,Value in value.items():
            print(f"- {Fore.GREEN} {Field} : {Fore.LIGHTMAGENTA_EX} {Value}{Style.RESET_ALL}")
     pass
     
def sort_contacts(contact_info):
    print("""------------- Sort Options --------------------------
          1. Sort contacts by Name field
          2. Sort contacts by Email field
          3. Sort contacts by Address 
          4. Sort contacts by phonenum
          """)
    try:
          sort_field = input("Please enter the field by which you want to sort(name/email/Address)")
          if sort_field == "1":
              print("Sorting the contact by name field!!")
              name_sort = dict(sorted(contact_info.items(),key = lambda x : x[1]["name"]))
              display_contact(name_sort)

              pass
          elif sort_field == "2":
              print("Sorting the contact by email field!!")
              email_sort = dict(sorted(contact_info.items(),key = lambda x : x[1]["email"]))
              display_contact(email_sort)
              pass
          elif sort_field == "3":
              print("Sorting the contact by Address field!!")
              address_sort = dict(sorted(contact_info.items(),key = lambda x : x[1]["additional_info"]["address"]))
              display_contact(address_sort)
              pass
          else:
              print("Please enter a valid option(1/2/3)")
              pass

    except Exception as e:
        print("Following error occured ", e)  
    finally:
        print("Sort function executed successfully!!")
        ip = input("Do you want to see all existing contacts in the system?").lower()
        if ip == "yes": 
            display_contact(contact_info)
    pass

def main(contact_info):
    print(""" 
        Welcome to the Contact Management System!!

        Menu:
        1. Adding a new contact with all relevant details.
        2. Editing an existing contact's information (name, phone number, email, etc.).
        3. Deleting a contact by searching for their unique identifier.
        4. Searching for a contact by their unique identifier and displaying their details.
        5. Displaying a list of all contacts with their unique identifiers.
        6. Displaying list of all contacts in the system.
        7. Exporting contacts to a text file in a structured format.
        8. Importing contacts from a text file and adding them to the system.
        9. Add custom fields like birthdays and anniversaries.
        10. Create automatic backups of contact data and the ability to restore data from a backup file. 
        11. Exit
    """)

    while True:
        try:
            choice = input("Hello there!! Please input your choice:\n")
            if choice == "1":
                add_contact(contact_info)
    
            elif choice == "2":
                edit_contact(contact_info)

            elif choice == "3":
                user_ip = input("Are you sure you want to delete the contact?\n")
                if user_ip == "yes": 
                    delete_contact(contact_info)
                    print("Your list after deletion:")
                    print(contact_info)
                else:
                    print("You have changed your mind!!The list remains intact!")
                    print(contact_info)

            elif choice == "4":
                user_ip = input("Do you want to search for a contact by Id?\n")
                if user_ip == "yes": 
                    search_contact(contact_info)
                    display_contact(contact_info)
               
                user_ip1 = input("Do you want to search for a contact by specific field?\n") 
                if user_ip1 == "yes":
                    search_by_fields(contact_info) 

            elif choice == "5":
                 print("Displaying contacts based on the Id!!")
                 display_contact_id(contact_info)
                 ans  = input("Do you want to sort the contacts based on a specific field?")
                 if ans == "yes":
                     sort_contacts(contact_info)
                
            elif choice == "6":
                print("Displaying list of all contacts in the system!!")
                display_contact(contact_info)

            elif choice == "7":
                    print("Export contacts to a text file")
                    export_contact(contact_info)
                    break
            
            elif choice == "8":
                    print("Import contacts from a text file")
                    import_contact(contact_info) # need to fix this
                    break
            elif choice == "9":
                    user_inp = input("Do you want to add custom fields for contacts? like birthdays and anniverseries?").lower()
                    if user_inp == "yes": 
                        add_custom_fields(contact_info)
                    pass
            elif choice == "10":
                    print("create automatic backups of contact data and the ability to restore data from a backup file.")
                    save_contacts_json(contact_info)
                    print("restoring backup")
                    restore_backup(contact_info_restore)
                    pass
            elif choice == "11":
                    print("You have chosen to quit!!Exiting.....")
                    break
            else: 
                raise InvalidOptionException
            
        except InvalidOptionException:
            print("Please choose a valid option between 1 to 11")


contact_info={
     "john.doe@gmail.com": {
        "name": "John Doe",
        "phone_number": "+1-789-234-1234",
        "alternate_number" :"+1-234-237-5647",
        "email": "john.doe@gmail.com",
        "additional_info": {
            "address": "756 BlossomHill, Bakersfield, USA",
            "notes": "Para Educator Position."
        }
    },
    "jane.smith@abc.com": {
        "name": "Jane Smith",
        "phone_number": "+1-456-234-4562",
        "alternate_number":"+1-234-777-8653",
        "email": "jane.smith@abc.com",
        "additional_info": {
            "address": "5678 Oak Street, Springfield, USA",
            "notes": "Works at ABC Corp."
        }
    }
}

main(contact_info)
contact_info_restore={}