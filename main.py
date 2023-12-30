import os

def check_number(n):
    while n < 1 or n > 6:
        n = int(input("Error, this number is invalid! Enter a number from 1 to 6\n"
                      "1. Add\n"
                      "2. Delete\n"
                      "3. Change\n"
                      "4. Search\n"
                      "5. Display\n"
                      "6. Exit\n"
                      "Enter the number of the command: "))
    return n

def add_row():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone_number = input("Enter phone number: ")
    comment = input("Enter comment: ")
    
    with open("phonebook.txt", "a") as file:
        file.write(f"{name},{surname},{phone_number},{comment}\n")
    print("Record added successfully!")

def delete_row():
    search_term = input("Enter name or surname to delete: ")
    lines = []

    with open("phonebook.txt", "r") as file:
        lines = file.readlines()

    with open("phonebook.txt", "w") as file:
        for line in lines:
            if search_term not in line:
                file.write(line)
    
    print("Record deleted successfully!")

def change_row():
    search_term = input("Enter name or surname to change: ")
    new_phone_number = input("Enter the new phone number: ")
    lines = []

    with open("phonebook.txt", "r") as file:
        lines = file.readlines()

    with open("phonebook.txt", "w") as file:
        for line in lines:
            if search_term in line:
                parts = line.strip().split(',')
                parts[3] = new_phone_number
                file.write(','.join(parts) + '\n')
            else:
                file.write(line)

    print("Record changed successfully!")

def search_row():
    search_term = input("Enter name or surname to search: ")
    with open("phonebook.txt", "r") as file:
        for line in file:
            if search_term in line:
                print(line.strip())

def print_file():
    with open("phonebook.txt", "r") as file:
        for line in file:
            print(line.strip())

def start_menu():
    command = None
    while command != 6:
        command = int(input("Greetings!!\n"
                            "1. Add\n"
                            "2. Delete\n"
                            "3. Change\n"
                            "4. Search\n"
                            "5. Display\n"
                            "6. Exit\n"
                            "Enter the number of the command: "))
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            search_row()
        elif command == 5:
            print_file()
    print("Goodbye, I will be glad to see you again!\n")

if __name__ == "__main__":
    start_menu()