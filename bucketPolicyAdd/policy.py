{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::xxxxx:role/core/awsdne00-cloud-admin"
            },
            "Action": [
                "s3:PutObject*",
                "s3:GetObject*",
                "s3:DeleteObject*"
            ],
            "Resource": "arn:aws:s3:::replace-bucket-name/*"
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::xxxxxxxx:role/core/awsdne00-cloud-admin"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::replace-bucket-name"
        },
        {
            "Sid": "",
            "Effect": "Deny",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::replace-bucket-name/*",
                "arn:aws:s3:::replace-bucket-name"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
