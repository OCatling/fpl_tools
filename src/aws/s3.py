import boto3
import logging


class Bucket:
    def __init__(self, bucket_name: str, s3_client: boto3.client = None) -> None:
        self.bucket_name = bucket_name
        self.s3_client = s3_client
        if self.s3_client is None:
            self.s3_client = boto3.client("s3")

    def put_object(self, key: str, data: any) -> dict:
        logging.info(f"Putting object {key} to {self.bucket_name}")
        response = self.s3_client.put_object(Bucket=self.bucket_name, Key=key, Body=data)
        logging.debug(f"Response: {response}")
        return response

    def get_object(self, key: str) -> dict:
        logging.info(f"Getting object {key} from {self.bucket_name}")
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        logging.debug(f"Response: {response}")
        response_body = response["Body"].read().decode("utf-8")
        logging.debug(f"Response Body: {response_body}")
        return response_body

    def delete_object(self, key: str) -> dict:
        logging.info(f"Deleting object {key} from {self.bucket_name}")
        response = self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
        logging.debug(f"Response: {response}")
        return response
