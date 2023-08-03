import yaml,os,shutil,logging,json


def read_params(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config

def clean_prev_dirs_if_exists(dir_path: str):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    
def create_dirs(dirs: list):
    for dir in dirs:
        os.makedirs(dir,exist_ok=True)

def save_local_df(df,df_path,header=False):
    if header:
        new_cols = [col.replace('',"_") for col in df.columns]
        df.to_csv(df_path,index=False,header=new_cols)
    else:
        df.to_csv(df_path,index=False)
