# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sabrina Fechtner ,11/15/2023, Define Classes
# ------------------------------------------------------------------------------------------ #
import json

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

# Define the Data Variables and constants
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
csv_data: str = ''
json_data: str = ''
file = None
menu_choice: str

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
        try:
            open(FILE_NAME, "r")
            student_data = json.load(file_name)
            print("Data successfully loaded from the file.")
        except FileNotFoundError as e:
            print(f"File not found, creating it...")
            open(FILE_NAME, "w")
            json.dump(student_data, file_name)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON file: {e}. Resetting it...")
            open(FILE_NAME, "w")
            json.dump(student_data, file_name)
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")
        finally:
            if file and not file.closed:
                file.close()
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
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
@staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do?: ")


    # Input user data
    if menu_choice == "1":

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            # CSV answer
            # for student in students:
            #     csv_data = f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n'
            #     file.write(csv_data)

            # # JSON answer
            json.dump(students, file)

            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
