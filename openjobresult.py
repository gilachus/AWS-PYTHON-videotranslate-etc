import boto3
import requests
import json

transcribe = boto3.client('transcribe')
s3 = boto3.client('s3')

def guardar_como_txt(json_uri):
	with open('respuesta.json', 'wb') as f:
		s3.download_fileobj('gilvideotranslate1', 'transcribe_3971f3f57d2046a9bf30b1750dafe606_mi_job.json', f)

def leer_json(file="respuesta.json"):		
	with open(file) as json_file:
		data = json.load(json_file)
		print(data['results']['transcripts'][0]['transcript'])


job_name = "transcribe_3971f3f57d2046a9bf30b1750dafe606_mi_job"
job = transcribe.get_transcription_job(TranscriptionJobName=job_name)

job_status = job['TranscriptionJob']['TranscriptionJobStatus']
if  job_status in ['COMPLETED', 'FAILED']:
	print(job_status)
	json_uri = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
	print(json_uri)
	guardar_como_txt(json_uri)
	leer_json()
else:
	print("pruebe en otro momento")


