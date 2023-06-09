## TASK 1
- Imported the boto3 library for interacting with AWS services.
- An IAM client is created using boto3.client('iam').
- The create_role method is called to create a new IAM role named 'awss3fullaccessanuj'. The role's assume role policy document allows the EC2 service to assume this role.
- The attach_role_policy method is used to attach the 'AmazonS3FullAccess' policy to the newly created role.
- A new S3 client is created using boto3.client('s3').
- The create_bucket method is called to create a new S3 bucket named 'my-bucket-anuj-821105' with an ACL set to 'private'.
- An EC2 client is created using boto3.client('ec2').
- The run_instances method is called to launch a new EC2 instance. It specifies the image ID, instance type, key pair name, and the minimum and maximum count of instances to launch.
- The response from the API calls is stored in the response or response_s3 variables, but they are not used further in the code.


## TASK 2
- Imported the necessary libraries: boto3 for interacting with AWS services, datetime and time for timestamp generation, and json for JSON operations.
- An S3 resource is created using boto3.resource('s3').
- The bucket name is set as 'awsanuj', and the key name for the JSON file is defined as 'transaction{}.json', where '{}' is a placeholder for the timestamp.
- A CloudWatch Logs client is created using boto3.client('logs').
- The log group name is set as 'lambda_logs', and the log stream name is set as 'lambda_stream'.
- The lambda_handler function is the entry point for the Lambda function.
- Inside the function, a JSON object is generated in the given format with transaction details.
- The JSON data is serialized using json.dumps into json_data.
- The file name is generated by formatting the key_name with the current timestamp, replacing spaces with underscores.
- The JSON file is uploaded to the S3 bucket using s3.Bucket(bucket_name).Object(file_name).put(Body=json_data).
- A log message is created to indicate the S3 object creation event.
- The log group and log stream are created if they don't already exist.
- The log message is published to CloudWatch Logs using cloudwatch_logs.put_log_events.
- The code checks the number of times the Lambda function has been invoked based on the ARN of the function.
- If it's the first, second, or third execution, a message is printed indicating the execution number. Otherwise, the code stops further execution.
- Exception handling is added to print any exception that occurs during execution.



## TASK 3
- Imported the necessary libraries: boto3 for interacting with AWS services, datetime for timestamp generation, and json for JSON operations.
- An S3 resource is created using boto3.resource('s3').
- The bucket name is set as 'awsanuj', and the key name for the JSON file is defined as 'anuj{}.json', where '{}' is a placeholder for the timestamp.
- The lambda_handler function is the entry point for the Lambda function.
- Inside the function, the input data is parsed from event['body'] and assigned to the body variable.
- The current timestamp is generated using datetime.datetime.now() and converted to a string (timestamp).
- The timestamp is added to the body dictionary with the key "timestamp".
- The JSON data is serialized using json.dumps into json_data.
- The file name is generated by formatting the key_name with the current timestamp, replacing spaces with underscores.
- The JSON file is uploaded to the S3 bucket using s3.Object(bucket_name, file_name).put(Body=json_data).
- A log message is printed indicating the S3 object creation event.
- The function returns a response dictionary with the file name and a status of "success" if the execution completes without errors.
- If an exception occurs during execution, it is printed, and the function returns a response dictionary with a status of "error".
