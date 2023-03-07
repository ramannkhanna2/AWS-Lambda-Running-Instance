# AWS-Lambda-Running-Instance
AWS Lambda Function to List/Print All Running EC2 Instances in CSV file Stored in Amazon S3.

>  ## USED RESOURCES

- ### IAM
  First create one IAM role for AWS Lambda with S3 full access and EC2 read only Access.

- ### Amazon S3
 Create one Amazon S3 Bucket and Upload One Blank CSV file in  your Bucket. 
 
 - ### Aws Lambda
   Create Lambda Function and Write/Upload Your Code and Run it. Lambda will download your CSV file in `/tmp/` folder. It will modify the CSV file and again automatically upload to the S3.
   
 - ### EC2
Launch EC2 Instances  and Check the output in Lambda console or your CSV file in S3.It will List out all Running Instances in your CSV file.



Note : Make sure to update bucket name and key(ur csv file name ) while configuring test event for the func like below snippet :
```
"bucket": {
          "name": "ec2-list-bucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::ec2-list-bucket"
        },
        "object": {
          "key": "test.csv",
          "size": 1024,
          ```

Note : Dont forget to add s3 and ec2 full access to role assigned to lambda func
