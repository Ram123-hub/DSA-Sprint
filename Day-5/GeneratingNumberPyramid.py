def generate_number_pyramid(rows):
    # Loop through each row
    for i in range(1, rows + 1):
        # Create an empty string for the current row
        row_string = ""
        # Loop through numbers from 1 to i
        for j in range(1, i + 1):
            # Append the current number to the row string
            row_string += str(j)
        # Print the constructed row
        print(row_string)

# Example usage
rows = 4
generate_number_pyramid(rows)
