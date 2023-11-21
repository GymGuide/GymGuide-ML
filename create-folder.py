import csv
import os
import shutil

directory_list = ['train', 'test', 'valid']

for folder in directory_list:
    # Input CSV file path
    input_file_path = folder + "/_annotations_cleaned_unique_" + folder + ".csv"

    # Open the CSV file and create a CSV reader
    with open(input_file_path, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Specify the base directory where the files are located
        base_directory = folder

        # Iterate through each row and move the corresponding file to its class folder
        for row in reader:
            filename = row['filename']
            class_name = row['class']

            # Source and destination paths
            source_file = os.path.join(base_directory, filename)
            destination_directory = os.path.join(base_directory, class_name)

            # Ensure the destination directory exists
            os.makedirs(destination_directory, exist_ok=True)

            destination_file = os.path.join(destination_directory, filename)

            # Move the file to its class folder
            shutil.move(source_file, destination_file)

        print(f"Files moved to class folders for {folder}.")
