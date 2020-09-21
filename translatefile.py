import boto3


s3 = boto3.client('s3')
translate = boto3.client('translate')

# with open('transcripcion.txt', 'r') as f:
# 	s3.upload_file('gilvideotranslate1', 'transcripcion.txt', f)

text=""
with open('transcripcion.txt', 'r') as f:
	text=f.read()


response = translate.translate_text(Text=text, SourceLanguageCode="en", TargetLanguageCode="es")

result=response['TranslatedText']

with open('traduccion.txt', 'w') as f:
	f.write(result)
