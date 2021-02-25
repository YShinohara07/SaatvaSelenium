'''
Using S3 buckets

Prerequisites: S3 storage bucket creditionals

Install the lastest verision (v2) AWS Command Line Interface (CLI) on your machine
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

Add AWS profile via aws command line (terminal/command prompt):
Execute "aws configure", you will see "AWS Access Key ID [None]:". Copy and paste the key creditionals from the document provided
Do the same for "AWS Secret Access Key [None]:"
For "Default region name [None]:" enter "us-east-2" (no quotes)
Leave "Default output format [None]:" as a blank entry


Interacting with S3 buckets on Python
Install boto3 library by going to your terminal/command prompt with: pip install boto3

Example script using S3:
'''
import pandas as pd
import boto3
from io import StringIO


def read_sample():
    df = pd.read_csv('~/desktop/selenium/Saatva_2021-02-23.csv', sep=',')
    return df


def write_to_s3(df):
    client = boto3.client('s3') # connects to S3 server using our AWS CLI defealt creditionals
    out_buffer = StringIO() # Buffering platform
    df.to_csv(out_buffer, sep=',', index=False) # to_csv is set to a directory location OR buffering platform as memory
    client.put_object(Bucket='ut-capstone-scraper', Key='test/test_file.csv', Body=out_buffer.getvalue()) # action that 


write_to_s3(read_sample()) 