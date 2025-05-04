from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Lambda

with Diagram("AWS Cost Drivers", show=False, filename="cost-drivers"):
    ec2 = EC2("EC2\n(Compute Hours + Data Transfer)")
    s3 = S3("S3\n(Storage Class + Requests)")
    lambda_func = Lambda("Lambda\n(Invokes + Duration)")