import csv
import os
import shutil
from collections import Counter

directory_list = ['train', 'test', 'valid']
for folder in directory_list:
    # Input CSV file path
    csv_file_path = folder + '/_annotations_cleaned.csv'

    # Open the CSV file and create a CSV reader
    with open(csv_file_path, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Extract filenames from the CSV file
        filenames = [row['filename'] for row in reader]

    # Check for duplicate filenames
    duplicate_filenames = [item for item, count in Counter(filenames).items() if count > 1]

    if duplicate_filenames:
        print("Duplicate filenames found in the CSV file:")
        for filename in duplicate_filenames:
            print(f"- {filename}")

        # Specify the base directory where the files are located
        base_directory = folder
        duplicate_directory = os.path.join(base_directory, 'duplicate')

        # Ensure the duplicate directory exists
        os.makedirs(duplicate_directory, exist_ok=True)

        # Move files with duplicate filenames to the 'duplicate' directory
        for filename in duplicate_filenames:
            source_file = os.path.join(base_directory, filename)
            destination_file = os.path.join(duplicate_directory, filename)

            shutil.move(source_file, destination_file)
            print(f"Moved {filename} to 'duplicate' directory.")

        # Create a new CSV file without duplicate filename rows
        output_csv_path = folder + "/_annotations_cleaned_unique_" + folder + ".csv"
        with open(output_csv_path, 'w', newline='') as outfile:
            fieldnames = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write rows excluding duplicate filenames
            with open(csv_file_path, 'r', newline='') as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    if row['filename'] not in duplicate_filenames:
                        writer.writerow(row)

        print(f"CSV file without duplicate filenames written to {output_csv_path}.")
    else:
        print("No duplicate filenames found in the CSV file.")
