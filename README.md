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



