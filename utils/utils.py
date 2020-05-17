from google.cloud import storage
import yaml
import os
import pandas as pd

def yamlConfig():
    """
    read yaml file from storage
    """
    client = storage.Client()
    bucket = client.get_bucket('dotz_configs')
    blob = bucket.get_blob('dotz_config.yaml')
    f = blob.download_as_string()
    return yaml.safe_load(f)

def list_bucket_csv_files(bucket_):
    """
    list all files where extension == csv
    """
    client = storage.Client()
    listed_files = []
    listed_bucket = client.list_blobs(bucket_)
    for files in listed_bucket:
        if len(files.name.split(".")[-1]) == 3:
            listed_files.append(files.name)
    return listed_files

def download_files(bucket_):
    """
    download files from raw bucket to remote path
    """
    fp = yamlConfig()
    downloads_path = fp["remote_paths"]["downloads"]
    files = list_bucket_csv_files(bucket_)
    client = storage.Client()
    bucket = client.bucket(bucket_)
    for i in files:
        blob = bucket.blob(i)
        try:
            os.mkdir(downloads_path)
        except FileExistsError:
            folder = i.split("/")[0]
            try:
                os.mkdir(downloads_path+folder)
                blob.download_to_filename(downloads_path+i)
                print(f"file {i} downloaded")
            except FileExistsError:
                blob.download_to_filename(downloads_path+i)
                print(f"file {i} downloaded")

def upload_file(bucket_name, remote_prefix):
    """
    upload file from specific bucket
    """
    fp = yamlConfig()
    download_path = fp["remote_paths"]["downloads"]
    list_file_to_update = os.listdir(download_path+remote_prefix+"/")
    source_file_name = download_path + remote_prefix + "/" + list_file_to_update[0]
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    destination_blob_name = remote_prefix + "/" + list_file_to_update[0]
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        bucket_name+"/"+destination_blob_name))

def restore_downloads():
    """
    restore download folder local path
    """
    fp = yamlConfig()
    download_path = fp["remote_paths"]["downloads"]
    price = 'price/'
    comp = 'comp/'
    bills = 'bills/'

    files_price = os.listdir(download_path+price)
    for i in files_price:
        os.remove(download_path+price+i)
    
    files_comp = os.listdir(download_path+comp)
    for j in files_comp:
        os.remove(download_path+comp+j)
    
    files_bills = os.listdir(download_path+bills)
    for l in files_bills:
        os.remove(download_path+bills+l)

def file_to_df(prefix):
    """
    read remote file based on prefix and return df
    """
    fp = yamlConfig()
    download_path = fp["remote_paths"]["downloads"]
    
    files = os.listdir(download_path+prefix)
    return pd.read_csv(download_path+prefix+files[0])
    