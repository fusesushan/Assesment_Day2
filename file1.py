"""Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older"""

import csv

def filter_adults(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as csv_infile, open(output_file, 'w', newline='') as csv_outfile:
            reader = csv.DictReader(csv_infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csv_outfile, fieldnames=fieldnames)

            # Write header to the output file
            writer.writeheader()

            for row in reader:
                age = int(row['Age'])
                if age >= 18:
                    writer.writerow(row)

            print("Filtered data is now saved to 'adults.csv'")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Specify input and output filenames
input_filename = 'data.csv'
output_filename = 'adults.csv'

# Call the function to filter and save the data
filter_adults(input_filename, output_filename)
