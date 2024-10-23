import boto3
import logging


class Bucket:
    def __init__(self, bucket_name: str, s3_resource: boto3.resource = None) -> None:
        self.bucket_name = bucket_name
        self.bucket_resource = s3_resource.Bucket(self.bucket_name)

    def put_object(self, key: str, data: dict) -> dict:
        logging.info(f"Putting object {key} to {self.bucket_name}")
        response = self.bucket_resource.put_object(Key=key, Body=data)
        logging.debug(f"Response: {response}")
        return response

    def get_object(self, key: str) -> dict:
        logging.info(f"Getting object {key} from {self.bucket_name}")
        response = self.bucket_resource.Object(key).get()
        logging.debug(f"Response: {response}")
        return response

    def delete_object(self, key: str) -> dict:
        logging.info(f"Deleting object {key} from {self.bucket_name}")
        response = self.bucket_resource.Object(key).delete()
        logging.debug(f"Response: {response}")
        return response

    def generate_signed_upload_url(self, key: str, content_type: str) -> str:
        logging.info(f"Generating signed UPLOAD URL for {key} in {self.bucket_name}")
        url = self.bucket_resource.meta.client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": key,
                "Expires": 300,
                "ContentType": content_type,
            },
            HttpMethod="PUT",
        )
        logging.debug(f"Generated URL: {url}")
        return url

    def generate_signed_download_url(self, key: str) -> str:
        logging.info(f"Generating signed DOWNLOAD URL for {key} in {self.bucket_name}")
        url = self.bucket_resource.meta.client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": key,
            },
        )
        logging.debug(f"Generated URL: {url}")
        return url
