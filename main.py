import time
import boto3
import uuid

# este es el servicio de transcribe
transcribe = boto3.client('transcribe')
# los jobs deben tener nombre unicos y el nombre todo pegado o con guiones
job_name = "transcribe_" + uuid.uuid4().hex + "_" +"mi_job" 
#para saber en que job estoy
print(job_name)

# "The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling."
# no usar caracteres especiales para los nombres de archivos, haber creado el bucket en us-east-1 (para que funcione por defecto según yo)
mediafile_uri = "s3://gilvideotranslate1/Life-in-Middle-Ages-and-Mass-MUS-630.mp4" # esto lo copie desde la consola s3 donde esta el archivo
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': mediafile_uri},
    MediaFormat='mp4',
    LanguageCode='en-US'
)

# consulta el estado del job cada 5 segundos
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
# el json con la transcripcion se puede bajar desde la consola Amazon Transcribe (hay que ver como sería con código)