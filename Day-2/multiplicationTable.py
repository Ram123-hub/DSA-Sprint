def multiplication_table_range(start, end, limit=10):
    for i in range(start, end + 1):
        print(f"Multiplication table for {i}:")
        for j in range(1, limit + 1):
            print(f"{i} x {j} = {i * j}")
        print()  # Print a new line for better readability

# Example usage
multiplication_table_range(1, 5)
