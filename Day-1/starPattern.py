def pyramid_star_pattern(n):
    for i in range(n):
        # Print spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()

# Example usage:
rows = int(input("Enter the number of rows: "))
pyramid_star_pattern(rows)
