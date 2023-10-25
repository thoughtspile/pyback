"""S3 connectors."""
from io import BytesIO
from os import path
from uuid import uuid4

import boto3
from botocore.exceptions import ClientError
from botocore.utils import fix_s3_host

from .settings import Settings


def upload_file(file: BytesIO, filename: str) -> bool:
    """Upload a file to an S3 bucket.

    :param file: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name.
    :return: True if file was uploaded, else False
    """
    settings = Settings()

    _, file_extension = path.splitext(filename)
    key = f"{str(uuid4())}{file_extension}"
    s3 = boto3.resource(
        service_name="s3", endpoint_url="http://s3-server:8000", use_ssl=False
    )
    s3.meta.client.meta.events.unregister("before-sign.s3", fix_s3_host)

    try:
        s3.create_bucket(Bucket=settings.AWS_S3_BUCKET_NAME)
        object = s3.Object(settings.AWS_S3_BUCKET_NAME, key)
        object.put(Body=file, ACL="public-read")
    except ClientError:
        return None
    return key
