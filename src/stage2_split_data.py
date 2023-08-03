from src.utils.common_utils import read_params,clean_prev_dirs_if_exists,create_dirs,save_local_df
import logging
import argparse
import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split



def split_data(config_path):
    config = read_params(config_path=config_path)
    artifacts = config['artifacts']
    raw_local_data = artifacts['raw_local_data']
    split_data = artifacts['split_data']
    process_data_dir = split_data['processed_data_dir']
    train_data_path = split_data['train_data']
    test_data_path = split_data['test_data']

    create_dirs([process_data_dir, train_data_path, test_data_path])  # Update this line to create all three directories

    base = config['base']
    split_ratio = base['test_size']
    random_seed = base['random_state']
    df = pd.read_csv(raw_local_data, sep=',')

    # Split the data into train and test sets
    train, test = train_test_split(
        df,
        test_size=split_ratio,
        random_state=random_seed,
    )

    save_local_df(train, train_data_path)  # Save the train data
    save_local_df(test, test_data_path)    # Save the test data



def get_data(config_path):
    config = read_params(config_path=config_path)
    data_path = config['data_source']['s3_source']  # Directly access the 'data_source' key
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_data_dir = config['artifacts']['raw_local_data_dir']
    raw_local_data = config['artifacts']['raw_local_data']
    clean_prev_dirs_if_exists(artifacts_dir)
    create_dirs(dirs=[artifacts_dir, raw_local_data_dir])
    df = pd.read_csv(data_path, sep=';')
    save_local_df(df, raw_local_data, header=True)
    return config



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='params.yaml')
    parsed_args = parser.parse_args()
    try:
        data = get_data(parsed_args.config)  # Pass the actual value of parsed_args.config without specifying the parameter name
        # Rest of your code for further processing or logging goes here

    except Exception as e:
        raise e
