'''
# Tee class to duplicate print output to multiple destinations.

import sys

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, message):
        for f in self.files:
            f.write(message)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

with open("output.txt", "w") as f:
    sys.stdout = Tee(sys.__stdout__, f)
    print("This shows in console AND goes to file")

# restore stdout after you're done
sys.stdout = sys.__stdout__
'''

import sys

class Tee:
    def __init__(self, *files):
        """
        Accepts one or more file-like objects (e.g., sys.__stdout__, open("file", "w")).
        Any message written to this Tee will be written to ALL of them.
        """
        self.files = files

    def write(self, message):
        """
        Called whenever something is printed.
        Writes the same message to every file in self.files.
        """
        for f in self.files:
            f.write(message)   # send message to target
            f.flush()          # make sure it's written immediately (no buffering delay)

    def flush(self):
        """
        Called to flush buffers (important for real-time output).
        Ensures all targets flush too.
        """
        for f in self.files:
            f.flush()

# Usage Example:
import os

current_directory = os.getcwd()
file_name = 'output_tee.txt'
file_path = os.path.join(current_directory, file_name)

# Open a file for logging
with open(file_path, "w") as f:
    # Redirect stdout to BOTH console and file
    sys.stdout = Tee(sys.__stdout__, f)

    # 👇 This goes to both console AND file
    print("Hello both!")

    # 👇 Only console (explicitly using sys.__stdout__)
    print("Hello console only!", file=sys.__stdout__)

    # 👇 Only file (explicitly using f)
    print("Hello file only!", file=f)

# Restore stdout when done
sys.stdout = sys.__stdout__

# Back to normal
print("Normal console output again")

