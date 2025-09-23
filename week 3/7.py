# Q7. Write a generator that yields even numbers up to N.


def even_numbers_up_to(n):
    """Yield even numbers from 2 up to n (inclusive)."""
    # start at 2, step by 2 to produce only even numbers
    for i in range(2, n + 1, 2):
        yield i

# Example usage:
n = 10
print(f"Even numbers up to {n}:")
for even in even_numbers_up_to(n):
    print(even, end=" ")
print()
