import json
import boto3
import datetime

s3 = boto3.client('s3')  # Create an S3 client

def lambda_handler(event, context):
    bucket = 'shishir-aws'  # Specify the S3 bucket name
    ct = datetime.datetime.now()  # Get the current timestamp

    dict = {}  # Create an empty dictionary to store data
    dict['transaction_id'] = '12345'  # Add transaction ID
    dict['payment_mode'] = 'card/netbanking/upi'  # Add payment mode
    dict['amount'] = 200  # Add transaction amount
    dict['customer_id'] = 101  # Add customer ID
    dict['timestamp'] = str(ct)  # Add timestamp as a string

    file_name = str(ct) + '.json'  # Generate the file name with timestamp and '.json' extension

    uploadByteStream = bytes(json.dumps(dict).encode('UTF-8'))  # Convert the dictionary to JSON byte stream

    # Upload the JSON byte stream to the specified S3 bucket with the generated file name
    s3.put_object(Bucket=bucket, Key=file_name, Body=uploadByteStream)

    print('put complete!')  # Print a completion message
