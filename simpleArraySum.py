# Function to calculate the sum of elements in an array
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Get user input for the array size
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty array
arr = []

# Get user input for the elements of the array
for i in range(n):
    try:
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    except ValueError:
        print("Please enter a valid number for element {i + 1}.")

# Calculate the sum of the array using the defined function
result = calculate_sum(arr)

# Print the sum
print(f"The sum of the array is: {result}")
