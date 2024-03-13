#import boto3
#from botocore.exceptions import NoCredentialsError, ClientError
#from flask import current_app as app
#
#def upload_to_s3(local_file_path, s3_file_path, bucket_name=None):
#    try:
#        bucket_name = bucket_name or app.config.get('AWS_S3_BUCKET_NAME', 'default-bucket-name')
#        s3 = boto3.client('s3',
#                          aws_access_key_id=app.config.get('AWS_ACCESS_KEY_ID'),
#                          aws_secret_access_key=app.config.get('AWS_SECRET_ACCESS_KEY'))
#        s3.upload_file(local_file_path, bucket_name, s3_file_path)
#        app.logger.info(f"File uploaded to S3: {s3_file_path}")
#    except FileNotFoundError:
#        app.logger.error("The local file was not found")
#    except NoCredentialsError:
#        app.logger.error("AWS credentials not available")
#    except ClientError as e:
#        app.logger.error(f"Failed to upload file to S3: {e}")
