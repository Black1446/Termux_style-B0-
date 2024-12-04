import os
import time
from getpass import getpass  # Import getpass for secure password input

# Global variables for stored username and password
stored_username = ""
stored_password = ""

def read_login_data():
    global stored_username, stored_password
    try:
        with open("login.txt", "r") as file:
            stored_username = file.readline().strip()
            stored_password = file.readline().strip()
    except FileNotFoundError:
        print("No login data found. Please set up a new username and password.")
        setup_login()  # Directly call setup_login if file is not found

def write_login_data(username, password):
    with open("login.txt", "w") as file:
        file.write(username + "\n" + password)

def login():
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")  # Use getpass for secure input
    return username == stored_username and password == stored_password

def show_options():
    print("------------------------------------------")
    print("            Welcome to Black1446          ")
    print("------------------------------------------")
    for i in range(1, 101):
        print(f"{i}. Option {i}")
    print("------------------------------------------")

def system_info():
    os.system("uname -a")

def run_python():
    os.system("python3 script.py")

def show_dir():
    os.system("ls")

def network_status():
    os.system("ifconfig")

def disk_usage():
    os.system("df -h")

def running_processes():
    os.system("top")

def show_date_time():
    os.system("date")

def ping_google():
    os.system("ping -c 4 google.com")

def update_system():
    os.system("sudo apt update && sudo apt upgrade -y")  # Added -y for automatic confirmation

def setup_login():
    username = input("Set Username: ")
    password = getpass("Set Password: ")  # Secure password input
    write_login_data(username, password)
    print("Login data saved successfully.")

def main():
    read_login_data()  # Read the login data at the start

    while True:
        if login():
            while True:
                show_options()
                choice = int(input("Select an option: "))

                if choice == 1:
                    system_info()
                elif choice == 2:
                    run_python()
                elif choice == 3:
                    show_dir()
                elif choice == 4:
                    network_status()
                elif choice == 5:
                    disk_usage()
                elif choice == 6:
                    running_processes()
                elif choice == 7:
                    show_date_time()
                elif choice == 8:
                    ping_google()
                elif choice == 9:
                    update_system()
                elif choice == 100:
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice! Please select again.")
        else:
            print("Invalid username or password. Try again.")
            time.sleep(2)  # Delay before retry

if __name__ == "__main__":
    main()
