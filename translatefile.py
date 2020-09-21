import boto3
import urllib.request, json

client = boto3.client('translate')

job_name = "transcribe_3971f3f57d2046a9bf30b1750dafe606_mi_job"
job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
json_uri = job['TranscriptionJob']['Transcript']['TranscriptFileUri']

with urllib.request.urlopen(json_uri) as url:
    data = json.loads(url.read().decode())
    print(data)