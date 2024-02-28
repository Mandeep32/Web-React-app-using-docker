# Function to find the sum of elements in an array
def array_sum(arr):
    return sum(arr)

# Taking input from the user for the array elements
def input_array():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    return arr

# Main function
def main():
    arr = input_array()  # Input array from the user
    total_sum = array_sum(arr)  # Calculate the sum of the array elements
    print("Sum of the elements in the array:", total_sum)

if __name__ == "__main__":
    main()
