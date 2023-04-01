import zipfile
import requests
from io import BytesIO
import os
import sys

import boto3

sys.path.insert(0, './config')
sys.path.insert(0, './helpers')
from config.aws import LANDING_BUCKET, ENEM_FOLDER, DOWNLOAD_URL
from helpers.parser import parse_file_names

def downloader(url):
    try:
        os.makedirs(ENEM_FOLDER, exist_ok=True)
        file_bytes = BytesIO(
            requests.get(DOWNLOAD_URL, verify=False).content
        )
        myzip = zipfile.ZipFile(file_bytes)
        myzip.extractall(ENEM_FOLDER)
        return True
    except:
        return False

def s3_upload(bucket_name, source_file_path, destination_file):

    s3_client = boto3.client('s3')
    s3_client.upload_file(source_file_path, bucket_name, destination_file)
    print(f"file: {destination_file} uploaded to bucket: {bucket_name} successfully")


if __name__ == "__main__":
    print("Starting Job")
    print(f"DOWNLOADING FILES....")
    downloader(DOWNLOAD_URL)
    print("Sending to S3")
    print("UPLOADING-----> to s3")
    src_path = "./enem2020/DADOS/MICRODADOS_ENEM_2020.csv"
    s3_upload(LANDING_BUCKET, src_path, f"enem2020/enem_2020.csv")

    print("Done!")