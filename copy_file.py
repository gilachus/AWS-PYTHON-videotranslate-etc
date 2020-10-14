import boto3
s3 = boto3.resource('s3')

copy_source = {
    'Bucket': 'bucketname',
    'Key': 'nombre viejo.png'
}
s3.meta.client.copy(copy_source, 'bucketname', 'nombre nuevo.png')
