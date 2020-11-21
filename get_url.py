import boto3
import csv
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket_name = 'skillmatch'
my_bucket = s3_resource.Bucket(bucket_name)

with open("pdf_links_S3.csv",'wb') as resultFile:
    for file in my_bucket.objects.all():
        params = {'Bucket': bucket_name, 'Key': file.key}
        url = s3_client.generate_presigned_url('get_object', params)
        print file.key, url.split('?')[0]
        wr = csv.writer(resultFile)
        wr.writerow([file.key, url.split('?')[0]])