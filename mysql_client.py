import colorama
import socket
from colorama import Fore, init, Back, Style

blue = Fore.LIGHTBLUE_EX
green = Fore.GREEN
red = Fore.RED

class Log:
    def print(str):
        print(f'{Style.BRIGHT}{Fore.RESET}[{Fore.LIGHTBLUE_EX}REZON{Fore.RESET}]:{Fore.RESET} {str}')
    def print2(str):
        print(f'{Style.BRIGHT}{Fore.RESET}[{Fore.RED}REZON{Fore.RESET}]:{red} {str}')
    

print(red + f"""#####################################################
#       MYSQL DATABASE CONNECTOR & EXECUTOR         #
# CREATE, REMOVE & EDIT ANYTHING IN MYSQL DATABASE  #
#    BY FROLIX | https://github.com/FrolixCZE       #
#####################################################""")
print("")

import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

def connect_to_database():
    host = input(f"{Style.BRIGHT}{Fore.RESET}[{Fore.LIGHTBLUE_EX}REZON{Fore.RESET}]:{Fore.RESET} Enter the MySQL server host (e.g., localhost): ")
    port = input(f"{Style.BRIGHT}{Fore.RESET}[{Fore.LIGHTBLUE_EX}REZON{Fore.RESET}]:{Fore.RESET} Enter the MySQL server port (e.g., 3306): ")
    user = input(f"{Style.BRIGHT}{Fore.RESET}[{Fore.LIGHTBLUE_EX}REZON{Fore.RESET}]:{Fore.RESET} Enter your MySQL username: ")
    password = input(f"{Style.BRIGHT}{Fore.RESET}[{Fore.LIGHTBLUE_EX}REZON{Fore.RESET}]:{Fore.RESET} Enter your MySQL password: ")
    database = input(f"{Style.BRIGHT}{Fore.RESET}[{Fore.LIGHTBLUE_EX}REZON{Fore.RESET}]:{Fore.RESET} Enter the name of the database you want to connect to: ")

    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        
        if connection.is_connected():
            Log.print(red + f"Connected to the database successfully!{Fore.RESET}")
            return connection
        else:
            Log.print(red + f"Failed to connect to the database.{Fore.RESET}")
            return None
    
    except Error as e:
        Log.print2(f"Error: {e}{Fore.RESET}")
        connect_to_database()
        return None

def show_tables(cursor):
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        if tables:
            Log.print(f"Tables in the database:{Fore.RESET}")
            for table in tables:
                print(table[0])
        else:
            Log.print2(red + f"No tables found in the database. {Fore.RESET}")
    
    except Error as e:
        Log.print2(f"Error: {e}")
        connect_to_database()

def run_sql_command(cursor, command):
    try:
        cursor.execute(command)
        results = cursor.fetchall()
        
        if results:
            for row in results:
                print(row)
        else:
            Log.print2("No results.")
    
    except Error as e:
        Log.print2(f"Error executing command: {e}{Fore.RESET}")

def interactive_mode(connection):
    cursor = connection.cursor()
    
    Log.print("Interactive SQL mode. Type 'SHOW TABLES' to list tables, or any SQL command.")
    print("Type 'EXIT' to disconnect from the current server and connect to another.")
    
    while True:
        command = input("mysql> ").strip()
        
        if command.upper() == "EXIT":
            Log.print("Disconnected from the server.")
            connection.close
            connect_to_database()
            break
        elif command.upper() == "SHOW TABLES":
            show_tables(cursor)
        else:
            run_sql_command(cursor, command)

def main():
    connection = connect_to_database()
    
    if connection:
        interactive_mode(connection)
        
        connection.close()

if __name__ == "__main__":
    main()
