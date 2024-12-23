
"""
Serverless Deployment with AWS Lambda
"""
import boto3
import json

def deploy_function():
    """
    Deploys Lambda function using Boto3.
    """
    lambda_client = boto3.client('lambda')
    with open("lambda_function.zip", "rb") as f:
        zip_content = f.read()

    response = lambda_client.create_function(
        FunctionName="HyCANProcessing",
        Runtime="python3.9",
        Role="<your-role-arn>",
        Handler="lambda_function.lambda_handler",
        Code={"ZipFile": zip_content},
        Timeout=300,
        MemorySize=128
    )
    print(response)
