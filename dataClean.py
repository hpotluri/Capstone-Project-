import pandas as pd
import os

def process_csv_files(data_dir, processed_dir, columns_to_remove):
    """
    Processes CSV files by removing specified columns and saving the modified files to a new directory.
    """
    # Ensure the processed directory exists
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # Process each CSV file in the directory
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(data_dir, filename)
            
            # Read the CSV file, specifying which row contains the headers
            df = pd.read_csv(file_path, header=1)  # Adjust 'header=1' if headers are on a different row

            # Remove unnecessary columns, check if they exist to avoid errors
            df = df.drop(columns=[col for col in columns_to_remove if col in df.columns])

            # Save the modified DataFrame to the processed directory
            processed_file_path = os.path.join(processed_dir, filename)
            df.to_csv(processed_file_path, index=False)

    print(f"All files have been processed and saved in '{processed_dir}'.")

# Directories
data_dir = 'data'
processed_dir = 'processed_data'

# Columns to remove
columns_to_remove = ['Methanol', 'Propane']  # Make sure these are exactly as they appear in your CSV header

# Process the files
process_csv_files(data_dir, processed_dir, columns_to_remove)
