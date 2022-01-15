"""
Authentification Program
Jake Zalesny
This program is meant to Authenticate User IDs and Passwords
"""
# This import allows me to read the Json file
import json

# This sets the file variable and loads the file into the variable users_and_passwords
def get_file(): 
    try :
        f = open("Lab02.json")
        users_and_passwords = json.load(f)
    except :
        print("Unable to open file: \"Lab02.json\"")
    
    return users_and_passwords
# This function sorts the file and returns the sorted strings
def sort_file(users_and_passwords):
    usernames = []
    passwords = []

# These two loops read the data from the file variable into two separate strings
    for lines in users_and_passwords["username"] :
        usernames.append(lines)
    
    for lines in users_and_passwords["password"] :
        passwords.append(lines) 
    
    return usernames, passwords

# This function prompts the user for their credentials.
def get_username_and_password():
    username = input("Username: ")
    password = input("Password: ")
    
    return username, password

# This authenticates the user's credentials and returns a true or false based on the results
def authenticate_username_and_password(username, password, usernames, passwords) :
    counter = 0
    for lines in usernames : 
        counter += 1
        if username == lines :
            break
    correct_password = passwords[counter - 1]
    
    if password == correct_password :
        return True
    else :
        return False

# This is where the functions actually run
users_and_passwords = get_file()
usernames, passwords = sort_file(users_and_passwords)
username, password = get_username_and_password()
authentification = authenticate_username_and_password(username, password, usernames, passwords)

# This runs the display at the end of the program
if authentification == True :
    print("You are authenticated.")
else :
    print("You are not authorized to use the system.")