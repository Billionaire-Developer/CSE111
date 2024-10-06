import random

def append_random_numbers(number_list, quantity=1):
    for _ in range(quantity):
        num = round(random.uniform(0, 100), 1)
        number_list.append(num)
def main():
    numbers = [16.2, 75.1, 52.3]
    print("Initial lists:", numbers)
    
    append_random_numbers(numbers)
    print("List after adding 1 number:", numbers)
    
    append_random_numbers(numbers, 3)
    print("List after adding 3 more numbers:", numbers)
    
if __name__ == "__main__":
    main()
    