'''
This script counts the number of files with a specific extension in a directory.
'''
import os
import glob

# pdf counter
def count_pdf_files(directory):
    count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                count += 1

    return count

# general counter
def count_files_by_extension(directory, extension):
    count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                count += 1

    return count

# Example usage
directory_path = '/path/to/directory'
extension = '.txt'
txt_count = count_files_by_extension(directory_path, extension)
print(f"Total {extension} files: {txt_count}")