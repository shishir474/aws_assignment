import json
import boto3
import datetime

def lambda_handler(event, context):
    # Parse the JSON data from the request body
    data = json.loads(event['body'])
    
    bucket = 'shishir-aws'  # Specify the S3 bucket name
    s3 = boto3.client('s3')  # Create an S3 client
    
    # Generate the file name with a prefix, current timestamp, and '.json' extension
    file_name = 'testdata' + str(datetime.datetime.now()) + '.json'
    
    # Convert the data dictionary to a JSON byte stream
    uploadByteStream = bytes(json.dumps(data).encode('UTF-8'))
    
    # Upload the JSON byte stream to the specified S3 bucket with the generated file name
    s3.put_object(Bucket=bucket, Key=file_name, Body=uploadByteStream)
    
    # Prepare the response object
    response = {}
    response['filename'] = file_name  # Add the uploaded file name to the response
    response['status_code'] = 200  # Add a status code (200 for success) to the response
    
    return response  # Return the response object
