from src.utils.common_utils import read_params,clean_prev_dirs_if_exists,create_dirs,save_local_df
import logging
import argparse
import pandas as pd

def get_data(config_path):
    config = read_params(config_path=config_path)
    data_path = config['data_source']['s3_source']
    arfifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_data_dir = config['artifacts']['raw_local_data_dir']
    raw_local_data = config['artifacts']['raw_local_data']
    clean_prev_dirs_if_exists(arfifacts_dir)
    create_dirs(dirs=[arfifacts_dir,raw_local_data_dir])
    df = pd.read_csv(data_path,sep=';')
    save_local_df(df,raw_local_data,header=True)
    return config


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='params.yaml')
    parsed_args = parser.parse_args()
    try:
        data = get_data(config_path=parsed_args.config)  # Fix: pass the actual value of parsed_args.config
        # Rest of your code for further processing or logging goes here

    except Exception as e:
        raise e
