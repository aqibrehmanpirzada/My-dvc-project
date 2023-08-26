import os
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil
from logger import logging

def process_data(data_path, test_ratio=0.2):
    # Read the data from the provided path
    data = pd.read_csv(data_path)

    # Split the data into train and test sets
    train_data, test_data = train_test_split(data, test_size=test_ratio, random_state=42)

    # Create a new directory to store the processed data inside the 'artifacts' directory
    processed_data_dir = os.path.join(os.path.dirname(os.path.dirname(data_path)), "processed_data")
    os.makedirs(processed_data_dir, exist_ok=True)

    # Define file paths for train and test datasets
    train_data_path = os.path.join(processed_data_dir, "train.csv")
    test_data_path = os.path.join(processed_data_dir, "test.csv")

    # Save train and test datasets to the new directory
    train_data.to_csv(train_data_path, index=False)
    test_data.to_csv(test_data_path, index=False)

    return train_data_path, test_data_path
    print(logging.info("Data is Processed Alright"))
    
if __name__ == "__main__":
    # Provide the path to the data.csv file
    data_path = "/media/aqib/Software/MLOPS Project/Project 1/My-dvc-project/artifacts/Notebooks/new_data.csv"

    # Call the function to process the data and get paths for train and test datasets
    train_data_path, test_data_path = process_data(data_path)

    print("Train dataset stored at:", train_data_path)
    print("Test dataset stored at:", test_data_path)
