import csv

directory_list = ['train', 'test', 'valid']
for folder in directory_list:
    input_file_path = folder + "/_annotations.csv"
    output_file_path = folder + "/_annotations_cleaned.csv"
    # Open the input CSV file and create a CSV reader
    with open(input_file_path, 'r', newline='') as infile:
        reader = csv.reader(infile)

        # Filter out empty rows and rows with less than 8 columns
        rows = [row for row in reader if any(field.strip() for field in row) and len(row) >= 8]

    # Open the output CSV file and create a CSV writer
    with open(output_file_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write the non-empty rows with at least 8 columns to the output file
        writer.writerows(rows)
