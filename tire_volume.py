#Import the math module, so i can use the math.pi
#Import the datetime module so i can use the current date
from datetime import datetime
import math

#welcome 
width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire in inches: "))

#compute the volume of the tire

volume = math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
volume = round(volume, 2)
current_date = datetime.now()

with open('volumes.txt', 'a') as file:
    file.write(f"{current_date: %Y-%m-%d} {width} {aspect_ratio} {diameter} {volume}\n")
print(f"The approximate volume is {volume} litres")

#Additional feature
#Tire size for four or more tire size

tire_prices = {
    (195, 65, 15): 120.00,
    (205, 55, 16): 150.00,
    (215, 60, 17): 180.00,
    (225, 50, 18): 200.00
}

#find price based on user input
if (width, aspect_ratio, diameter) in tire_prices:
    price = tire_prices[(width, aspect_ratio, diameter)]
    print(f"Tire price: ${price:.2f}")
    
else:
    print("Tire price not available")
    
#Ask user if they want to buy tires
buy_tires = input("Do you want to buy tires with this Dimension? (yes/no): ")
if buy_tires.lower() == "yes":
    phone_number = input("Please enter your phone number: ")
    with open('volumes.txt', 'a') as file:
        file.write(f"Phone number: {phone_number}\n")