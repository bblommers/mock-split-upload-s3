import re
import boto3


def test_handle_content_parallel():
    from package.server_split import __version__, SplitUploadS3
    bucket = 'my-bucket'
    conn = boto3.resource('s3', region_name='us-east-1', endpoint_url="http://localhost:5000")
    conn.create_bucket(Bucket=bucket)
    prefix = 'd1/d2/d3/d4'
    regex = re.compile(r'(\d{4}-\d{2})-\d{2} \d{2}:\d{2}:\d{2}')

    iterator = [
        dict(dt="2020-02-10 10:04:10", level=10, name="cyril"),
        dict(dt="2020-06-02 16:04:10", level=21, name="cynthia"),
        dict(dt="2019-07-03 12:24:08", level=12, name="steve"),
        dict(dt="2018-01-06 11:14:17", level=17, name="oliver"),
    ]

    res = SplitUploadS3(bucket, prefix, regex, iterator).handle_content()
    print(res)
    
    res = boto3.client("s3", endpoint_url="http://localhost:5000").list_objects_v2(Bucket=bucket)
    print(res)
