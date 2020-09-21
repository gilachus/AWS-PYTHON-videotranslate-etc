import boto3
import requests
import json

# servicio transcribe
transcribe = boto3.client('transcribe')
# servicio translate
translate = boto3.client('translate')

# el job con que estoy trabajando
job_name = "transcribe_3971f3f57d2046a9bf30b1750dafe606_mi_job"
job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
json_uri = str(job["TranscriptionJob"]["Transcript"]["TranscriptFileUri"])

# pedir json
def getTranscript( transcriptURI ):
	# para que el request resulte debe poner el bucket en modo publico y el luego el archivo en modo publico 
	# o tocaria hacer un request con credenciales 
    result = requests.get( transcriptURI )

    return result.text

# json
transcript = getTranscript( json_uri ) 
# json to python 
ts = json.loads( transcript )

# texto a traducir
txt = ts["results"]["transcripts"][0]["transcript"]
print(txt[0:30],"...\n")

# idiomas
sourceLangCode="en"
targetLangCode="es"

# método de traducción -> {}
translation = translate.translate_text(Text=txt,SourceLanguageCode=sourceLangCode, TargetLanguageCode=targetLangCode)
# el texto traducido
translation_txt = translation['TranslatedText']

print(translation_txt)

with open('traduccionuri.txt', 'w') as f:
	f.write(translation_txt)