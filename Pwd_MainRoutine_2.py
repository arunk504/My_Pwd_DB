from sys import exit
import Pwd_DB_CRUD_test as pdb
master_password = "Abracadabra"

def create_pwd(option):
    msg_list = ["Enter Account name","Enter user id", "Enter password", "Enter type", "Enter comments if any"]
    create_list = []
    for x in msg_list:
        print(x)
        create_list.append(input().strip())
        pdb.Update_DB(option, create_list)
    return

def update_pwd(option):
    print("Enter Account name")
    sname=input().strip()
    print("Enter new password")
    pname = input().strip()
    pdb.Update_DB(option,pname)
    
def sd_pwd(option):
    print("Enter Account name")
    sname = input().strip()
    record=(pdb.Update_DB(option, sname))
    if record:
        print(record[1], record[2])
    else:
        print("No such Account")
    
    return

def quit_pwd(option):
    print("Goodbye")
    exit()

def invalid_opt():
    print("Invalid option")
    print("Please enter the correct option: c, t, s , d or q")
    
option_dict = {
    "c": (" : Create new password", create_pwd),
    "s": (" : Show password",  sd_pwd),
    "u": (": Update existing password", update_pwd),
    "d": (": Delete a password", sd_pwd),
    "q": (": Quit this program", quit_pwd)
}

def print_menu():
    print("************************************************************")
    for key in option_dict.keys():
        print (key+ option_dict[key][0])
    print('\n', "************************************************************")


# The main program: Authenticates, prints menu, gets user input and does the rest....
print('Enter master password:')
pwd_input = input()

if pwd_input == master_password:
    print("Access granted", '\n')
else:
    print("Sorry, try again")

while True:
    print_menu()      
    option=input().strip().lower()
    option_dict.get(option, [None,invalid_opt])[1](option)
    
   
    



