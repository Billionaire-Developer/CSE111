import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    products = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row (headings)
        for row in reader:
            key = row[key_column_index]
            products[key] = row
    return products

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        print("Billionaire-Developer")
        print("Requested Items")
        subtotal = 0
        total_items = 0
        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first row (headings)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                product = products_dict.get(product_number)
                if product:
                    price = float(product[2])
                    total_items += quantity
                    subtotal += price * quantity
                    print(f"{product[1]}: {quantity} @ {price:.2f}")
                else:
                    print(f"Product not found: {product_number}")
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        sales_tax = subtotal * 0.06
        print(f"Sales Tax: {sales_tax:.2f}")
        total_due = subtotal + sales_tax
        print(f"Total: {total_due:.2f}")
        print("Thank you for shopping at the Billionaire-Developer.")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A %I:%M %p}")
    except FileNotFoundError:
        print("Error: missing file")
    except PermissionError:
        print("Error: permission denied")
    except KeyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    