# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sabrina Fechtner, 11/15/2023, Define Classes
# ------------------------------------------------------------------------------------------ #
import json
import io
from typing import TextIO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
Select from the following menu:  
1. Register a Student for a Course.
2. Show current data.  
3. Save data to a file.
4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []
menu_choice: str


#File Processing Functions
class FileProcessor:
        """
        A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created Class
        Sabrina Fechtner 11.15.2023 Incorporated Class into A06
        """
# When the program starts, read the file data into table
# Extract the data from the file
# Read from the Json file
@staticmethod
def read_data_from_file(file_name: str, student_data: list):
        """ This function reads previous JSON file with student and course data

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated Function

        :return: Student Data
        """
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
            print("Data successfully loaded from the file.")
        except FileNotFoundError as e:
            print(f"File not found, creating it...")
            open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
        except json.JSONDecodeError as e:
            print(f"Invalid JSON file: {e}. Resetting it...")
            open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")
        finally:
            if file.closed == False:
                file.close()
        return student_data
@staticmethod
def write_data_to_file(file_name: str, student_data: list):
    """ This function writes student and course data to JSON file

ChangeLog: (Who, When, What)
RRoot,1.3.2030,Created function
Sabrina Fechtner, 11.16.2023, Incorporated Function

:return: None
"""
    try:
        file = open(file_name, "w")
        json.dump(student_data, file)
        file.close()
    except TypeError as e:
        IO.output_error_messages("Please check that the data is a valid JSON format", e)
    except Exception as e:
        IO.output_error_messages("There was a non-specific error!", e)
    finally:
        if file.closed == False:
            file.close()

# Present and Process the data
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """
    pass

@staticmethod
def output_error_messages(message:str, error: Exception = None):
    """ This function displays error messages to the user

ChangeLog: (Who, When, What)
RRoot,1.3.2030,Created function
Sabrina Fechtner, 11.16.2023, Incorporated into A06

:return: None
"""
    print(message, end="\n\n")
    if {error} is not None:
        print(f"An unexpected error occurred: {error}")

@staticmethod
def output_menu(menu: str):
    """ This function displays the menu of choices to the user

    ChangeLog: (Who, When, What)
    RRoot,1.3.2030,Created function
    Sabrina Fechtner, 11.16.2023, Incorporated into A06

    :return: None
    """
    print()
    print(menu)

@staticmethod
def input_menu_choice():
    """ This function incorporates user choice from menu

    ChangeLog: (Who, When, What)
    RRoot,1.3.2030,Created function
    Sabrina Fechtner, 11.16.2023, Incorporated into A06

    :return: User Choice
        """
    choice = "0"
    try:
        choice = input("What would you like to do?: ")
        if choice not in ("1","2","3","4"):
            raise Exception("Only Enter 1, 2, 3, or 4")
    except Exception as e:
        IO.output_error_messages(e.__str__())
        return choice

@staticmethod
def input_student_data(student_data: list):
    while True:
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name cannot be alphanumeric. Please re-enter the first name.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name cannot be alphanumeric. Please re-enter the last name.")
            break
        except ValueError as e:
            print(e)

        course_name = input("Please enter the name of the course: ")
        student_data = {"student_first_name": student_first_name, "student_last_name": student_last_name,
        "course": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

@staticmethod
def output_student_courses(student_data: list):
    """ This function gets the first name, last name, and GPA from the user

    ChangeLog: (Who, When, What)
    RRoot,1.3.2030,Created function
    Sabrina Fechtner, 11.16.2023, Incorporated into A06

    :return: None
    """
    for students in student_data:
        print("The current data is: \n")
        print(students)


#Main program:
    students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

    while (True):
        IO.output_menu(menu=MENU)
        menu_choice = IO.input_menu_choice()
    # Input user data
        if menu_choice == "1":
            IO.input_student_data(student_data=students)
            IO.output_student_courses(student_data)
            continue
    # Present the current data
        elif menu_choice == "2":
            IO.output_student_courses(student_data)
            continue
    # Save the data to a file
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
            continue
    # Stop the loop
        elif menu_choice == "4":
            break  # out of the loop
        
    print("Program Ended")
