# Q10. Handle multiple exceptions in a single try block.
def process(value_str, divisor, filename):
    """
    - Convert value_str to int
    - Divide 100 by the integer
    - Read the given filename
    Demonstrates multiple exception handling.
    """
    try:
        value = int(value_str)       # may raise ValueError
        result = 100 / value         # may raise ZeroDivisionError
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()         # may raise FileNotFoundError
    except ValueError as e:
        print("Invalid integer provided:", e)
    except ZeroDivisionError:
        print("Cannot divide by zero. Provide a non-zero integer.")
    except FileNotFoundError as e:
        print("File not found:", e)
    except (TypeError, OverflowError) as e:
        # group exceptions that we want to handle the same way
        print("Type/Overflow error:", e)
    except Exception as e:
        # catch-all fallback (use sparingly)
        print("An unexpected error occurred:", e)
    else:
        # Runs if no exception was raised
        print("Processing successful.")
        print("Converted value:", value)
        print("Division result:", result)
        print("File length (chars):", len(data))
    finally:
        # Runs always (cleanup)
        print("Finished attempt to process inputs.\n")

# Example runs
process("10", 0, "existing.txt")     # int OK, division OK, but file might be missing
process("0", 0, "existing.txt")      # int OK (0), but ZeroDivisionError
process("abc", 0, "existing.txt")    # ValueError at int conversion
process("50", 0, "missing.txt")      # int OK, division OK, file missing -> FileNotFoundError