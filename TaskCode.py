import boto3
import csv
import urllib
ls=[]


# Connect S3 , EC2 to client.

s3_client = boto3.client('s3')
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    # instantiate empty array
    for instance in instances:
        # for each instance, append to array and print instance id
        ls.append(instance.id)
    print(ls)
    
    
    
    # Get the bucket and object key from the Event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    localFilename = '/tmp/test.csv'   #you can give any name.

    # Download the file from S3 to the local filesystem
    s3_client.download_file(bucket, key, localFilename)


    # Writing in CSV file

    with open('/tmp/test.csv', 'w', newline='') as f:
      w = csv.writer(f)
      sample=["InstanceId"]
      
      w.writerow(sample)
      for i in ls:
          w.writerow([i])
          
    # Upload modified file
    s3_client.upload_file(localFilename, bucket, key)
