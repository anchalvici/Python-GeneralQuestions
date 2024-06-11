def print_half_pyramid(n):
    if n > 0:
        # Call the function recursively with a smaller value of n
        print_half_pyramid(n - 1)
         
        # Print '*' characters for the current row
        print('* ' * n)
 
# Get the number of rows from the user
rows = int(input("Enter the number of rows for the half pyramid: "))
 
# Call the function to print the half pyramid pattern
print_half_pyramid(rows)