import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    
    Parameters:
    filename (str): The name of the CSV file to read.
    key_column_index (int): The index of the column to use as the keys in the dictionary.
    
    Return:
    dict: A compound dictionary that contains the contents of the CSV file.
    """
    products = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row (headings)
        for row in reader:
            key = row[key_column_index]
            products[key] = row
    return products

def main():
    products_dict = read_dictionary('products.csv', 0)
    print("All Products")
    print(products_dict)
    
    print("\nRequested Items")
    with open('request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row (headings)
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            product = products_dict.get(product_number)
            if product:
                price = float(product[2])
                print(f"{product[1]}: {quantity} @ {price:.2f}")
            else:
                print(f"Product not found: {product_number}")

if __name__ == "__main__":
    main()