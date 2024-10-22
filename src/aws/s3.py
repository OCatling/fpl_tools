import boto3


class Bucket:
    def __init__(self, bucket_name: str, s3_resource: boto3.resource = None) -> None:
        self.bucket_name = bucket_name
        self.bucket_resource = s3_resource.Bucket(self.bucket_name)

    def put_object(self, key: str, data: dict) -> dict:
        return self.bucket_resource.put_object(Key=key, Body=data)
