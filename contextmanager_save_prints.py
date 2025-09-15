import sys
import os
from contextlib import contextmanager

current_directory = os.getcwd()

@contextmanager
def redirect_stdout_to_file(file_path):
    # Save the current stdout so we can restore it later
    original_stdout = sys.stdout  
    
    # Open the file in write mode (will overwrite existing content)
    with open(file_path, 'w') as f:
        # Redirect all prints to the file
        sys.stdout = f  
        yield  # <-- this is where the "with" block body runs
        # After the block ends, restore stdout to the console
        sys.stdout = original_stdout


# Usage Example 1:
file_name = 'output_custom_contextmanager.txt'
file_path = os.path.join(current_directory, file_name)

with redirect_stdout_to_file(file_path):
    print(f"This will be written to filepath {file_path}")
    print("Hello world!")

print("But this will be printed to the console.")

# Usage Example 2: Using built-in context manager

from contextlib import redirect_stdout

file_name = 'output_builtin_contextmanager.txt'
file_path = os.path.join(current_directory, file_name)

with open(file_path, "w") as f:
    with redirect_stdout(f):
        print(f"This will be written to filepath {file_path}")
        print("Hello world!")

print("Back to console again!")