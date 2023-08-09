""" Create a function search_log that takes a log file and a search keyword as input.
The function should find and display all lines containing the search keyword.
"""

def search_log(log_file, search_keyword):
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        matching_lines = [line.strip() for line in lines if search_keyword in line]

        if matching_lines:
            print(f"Lines containing '{search_keyword}':")
            for line in matching_lines:
                print(line)
        else:
            print(f"No lines containing '{search_keyword}' found.")
    except FileNotFoundError:
        print(f"File '{log_file}' not found.")

# Example usage
log_file = 'logfile.txt'
search_keyword = 'file'

search_log(log_file, search_keyword)
