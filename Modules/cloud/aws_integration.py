
import boto3
from typing import Dict, List
import json

class DistributedBioinformatics:
    def __init__(self, region: str = "us-east-1"):
        self.sqs = boto3.client('sqs', region_name=region)
        self.s3 = boto3.client('s3', region_name=region)
        self.queue_url = self.create_job_queue()
        
    def create_job_queue(self) -> str:
        """Create SQS queue for job distribution."""
        response = self.sqs.create_queue(
            QueueName='bioinformatics-jobs',
            Attributes={
                'VisibilityTimeout': '3600',
                'MessageRetentionPeriod': '86400'
            }
        )
        return response['QueueUrl']
    
    def submit_job(self, job_data: Dict) -> str:
        """Submit a bioinformatics job to the queue."""
        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(job_data)
        )
        return response['MessageId']
    
    def process_results(self, bucket: str, key: str) -> Dict:
        """Process results from S3."""
        response = self.s3.get_object(Bucket=bucket, Key=key)
        return json.loads(response['Body'].read().decode('utf-8'))
    
    def distribute_workflow(self, tasks: List[Dict]) -> List[str]:
        """Distribute workflow tasks across workers."""
        job_ids = []
        for task in tasks:
            job_id = self.submit_job(task)
            job_ids.append(job_id)
        return job_ids
    
    def monitor_jobs(self, job_ids: List[str]) -> Dict[str, str]:
        """Monitor status of distributed jobs."""
        status = {}
        for job_id in job_ids:
            response = self.sqs.receive_message(
                QueueUrl=self.queue_url,
                MessageAttributeNames=['Status']
            )
            if 'Messages' in response:
                status[job_id] = response['Messages'][0]['MessageAttributes']['Status']['StringValue']
            else:
                status[job_id] = 'PENDING'
        return status
