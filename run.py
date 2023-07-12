import glob
import os
import sys
import pandas as pd
import datetime


class CSVMerger:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def close(self):
        input("Press any key to exits!")
        sys.exit()

    def merge_csv_files(self):

        # Pattern to match CSV files
        file_pattern = '*.csv'

        # Get a list of all CSV files in the directory
        file_list = glob.glob(self.input_folder + '/' + file_pattern)
        if not file_list:
            print('======> Empty csv file in "input" folder <======')
            self.close()

        # Initialize an empty DataFrame to store the merged data
        merged_data = pd.DataFrame()

        # Get the header of the first file
        first_file = file_list[0]
        first_file_header = pd.read_csv(first_file, nrows=0).columns.tolist()

        # Iterate over each CSV file
        for file in file_list:
            # Read the CSV file into a DataFrame
            data = pd.read_csv(file)
            # Check if the file's header matches the first file's header
            if pd.read_csv(file, nrows=0).columns.tolist() != first_file_header:
                print(
                    f"Warning: File '{os.path.basename(file)}' has a different header!")
                self.close()
            # Append the data to the merged_data DataFrame
            merged_data = merged_data.append(data)

        # Generate the output file path
        now = datetime.datetime.now()
        file_name = f'merge-files-{now.day}-{now.hour}-{now.minute}-{now.second}.csv'
        output_file = os.path.join(self.output_folder, file_name)

        # Write the merged data to the output file
        merged_data.to_csv(output_file, index=False)

        print("Merged CSV files successfully!")
        self.close()


if __name__ == '__main__':
    input_folder = "input"
    output_folder = "output"
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    csv_merger = CSVMerger(input_folder, output_folder)
    csv_merger.merge_csv_files()
