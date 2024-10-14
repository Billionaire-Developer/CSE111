import csv

def read_dictionary(students):
    """Read the contents of a CSV file into a dictionary and return the dictionary.
    
    Parameters:
    filename (str): The name of the CSV file to read.
    
    Return:
    dict: A dictionary that contains the contents of the CSV file.
    """
    students = {}
    with open(students, 'r') as file:
        next(file)  # Skip the first line (headings)
        for line in file:
            inumber, name = line.strip().split(',')
            students[inumber] = name
    return students

def main():
    students = read_dictionary('students.csv')
    inumber = input("Please enter an I-Number (xxxxxxxxx): ")
    inumber = inumber.replace('-', '')  # Remove dashes
    if inumber in students:
        print(students[inumber])
    else:
        print("No such student")
