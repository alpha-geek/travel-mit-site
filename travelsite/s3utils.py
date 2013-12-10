from storages.backends.s3boto import S3BotoStorage

StaticS3BotoStorage = lambda: S3BotoStorage(bucket='travelsite',location='static')
MediaS3BotoStorage = lambda: S3BotoStorage(bucket='travelsite',location='media')