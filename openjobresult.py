import boto3


transcribe = boto3.client('transcribe')

job_name = "transcribe_93d4903efb464d2b8bfcb44f2b279203_mi_job"
job = transcribe.get_transcription_job(TranscriptionJobName=job_name)

job_status = job['TranscriptionJob']['TranscriptionJobStatus']
if  job_status in ['COMPLETED', 'FAILED']:
	print(job_status)
	print(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
else:
	print("pruebe en otro momento")
