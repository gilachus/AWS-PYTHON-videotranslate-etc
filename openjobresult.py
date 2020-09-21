import boto3
import requests
import json

transcribe = boto3.client('transcribe')
s3 = boto3.client('s3')

job_name = "transcribe_3971f3f57d2046a9bf30b1750dafe606_mi_job"
job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
job_status = job['TranscriptionJob']['TranscriptionJobStatus']


def guardar_archivo(json_uri):
	with open('respuesta.json', 'wb') as f:
		s3.download_fileobj('gilvideotranslate1', 'transcribe_3971f3f57d2046a9bf30b1750dafe606_mi_job'+'.json', f)

def leer_json(file="respuesta.json"):		
	with open(file) as json_file:
		data = json.load(json_file)
		text=data['results']['transcripts'][0]['transcript']
		return text

def guardar_transcripcion(text):
	with open('transcripcion.txt', 'w') as f:
		print(text)
		f.write(text) 



if  job_status in ['COMPLETED', 'FAILED']:
	print(job_status,"\n")
	json_uri = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
	print(json_uri,"\n")
	guardar_archivo(json_uri)
	guardar_transcripcion(leer_json())	
else:
	print("pruebe en otro momento")


