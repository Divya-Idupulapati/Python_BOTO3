import boto3
from boto3 import session


region = "us-east-1"
bucket_name = "aws-bigdata-blog"
object_prefix = "artifacts/flink-refarch/data/nyc-tlc-trips.snz/"

session_ = session.Session()
s3_resource = session_.resource("s3", region_name=region)
bucket = s3_resource.Bucket(bucket_name)
print("Files in S3 bucket:")
for obj in bucket.objects.filter(Prefix=object_prefix):
    print(obj.key)




for obj in bucket.objects.filter(Prefix=object_prefix):
    target = obj.key.split("/")[-1]  # keep only the filename
    if target:  # skip folder placeholders
        print(f"Downloading {obj.key} to {target}")
        bucket.download_file(obj.key, "./" +target)
        print(f"Downloaded {obj.key} to {target}")
        print(target)
        print(f"Size: {obj.size/(1024*1024)} MB")