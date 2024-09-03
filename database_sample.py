
import csv

# Define the condition for extracting the row
aadharno = input("Enter the AADHAR NUMBER:")

# Define the path to the CSV file
file_path = r"C:\Users\ChandraSekar\Desktop\Yesist.csv"

try:
    # Open the CSV file for reading
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        
        # Flag to check if we found the row
        found = False
        
        # Search for the row that meets the condition
        for row in csv_reader:
            if row.get('Aadhar no.') == aadharno:
                # Print or process the desired row
                print("Record found:")
                print(row)
                found = True
                break
        
        if not found:
            print("No record found with the provided AADHAR number.")
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
import csv
#456787659876
# Define the condition for extracting the row
aadharno = input("Enter the AADHAR NUMBER:")

# Define the path to the CSV file
file_path = r"C:\Users\ChandraSekar\Desktop\Yesist.csv"

try:
    # Open the CSV file for reading
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        
        # Flag to check if we found the row
        found = False
        
        # Search for the row that meets the condition
        for row in csv_reader:
            if row.get('Aadhar no.') == aadharno:
                # Print or process the desired row
                print("Record found:")
                print(row)
                found = True
                break
        
        if not found:
            print("No record found with the provided AADHAR number.")
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
