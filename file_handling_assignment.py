try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: This is the first line of text.\n")
        file.write("Line 2: The number is 123.\n")
        file.write("Line 3: Python file handling is fun!\n")
    print("File 'my_file.txt' created and text written successfully.")
except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# File reading and displaying
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nFile content:\n", content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appending more content.\n")
        file.write("Line 5: Numbers can be added like this: 456.\n")
        file.write("Line 6: More file operations are possible!\n")
    print("\nAdditional lines appended successfully.")
except PermissionError:
    print("Permission denied: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Error handling with finally block
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nFinal file content:\n", content)
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("\nFile operations complete.")
