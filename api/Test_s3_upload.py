import boto3
import os
import io

# Create an S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
)

# Example image bytes
img_byte_arr = io.BytesIO()  # Replace this with actual image byte array
img_byte_arr.write(b'your_image_data_here')  # Replace this with actual image data
img_byte_arr.seek(0)

# Upload image to S3
try:
    response = s3.put_object(
        Bucket="qrcode-storage-devops-capstone-kazbruh",
        Key="qr_codes/test.png",  # Make sure to use a string with quotes
        Body=img_byte_arr,
        ContentType='image/png'
    )
    print(f"Upload successful: {response}")
except Exception as e:
    print(f"An error occurred: {e}")
