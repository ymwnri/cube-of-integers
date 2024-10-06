# Program: Cube Elements of an Array Using Functions
# Features: Takes the size and elements of an array as input and prints the cube of each element using functions.
# Procedure:
# 1. Define a function to take and validate input for the array size and elements.
# 2. Define a function to calculate and print the cube of each element.
# 3. Handle invalid input and prompt the user until valid input is provided.

def get_array_input():
    """Get and validate user input for the array size and elements.

    Returns:
        list: A list of integers representing the array elements.
    """
    while True:
        try:
            # Input size of the array
            size = int(input("Enter the size of the array: "))
            
            # Input elements of the array
            elements = input("Enter the elements of the array: ").split()
            
            # Validate if the size matches the number of elements
            if size != len(elements):
                print("Size doesn't match the number of elements. Please try again.")
            else:
                # Convert elements to integers and return
                return [int(element) for element in elements]
        except ValueError:
            print("Invalid Input. Please enter valid numbers for size and elements.")

def print_cubed_elements(elements):
    """Calculate and print the cube of each element in the list.

    Args:
        elements (list): List of integers to be cubed.
    """
    for element in elements:
        print(f"The cube of {element} is: {element ** 3}")

# Start of the program
array_elements = get_array_input()
print_cubed_elements(array_elements)
