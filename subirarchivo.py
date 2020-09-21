import boto3

# servicio de almacenamieno s3
s3 = boto3.resource('s3')

# por si queremos ver el nombre de los buckets
for bucket in s3.buckets.all():
	print(bucket.name)    

# el archivo en este caso es una imagen png
file = open('test.png', 'rb')

# método para subir archivos
s3.Bucket('gilvideotranslate').put_object(Key='test.png', Body=file)