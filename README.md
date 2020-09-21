# videotranslate

## configuraciones
- crea tu cuenta en AWS
- crea un usuario AIM 
- dale permisos en los servicios AdministratorAccess, AmazonTranscribeFullAccess, TranslateFullAccess
- descarga las credenciales del usuario 
- instala aws cli en tu pc
- configuralo en el cmd con el comando: aws configure
- agrega las credenciales que descargaste anteriormente la region y el formato 

ejemplo: https://aws.amazon.com/es/getting-started/hands-on/backup-to-s3-cli/

## código
crea tu entorno virtual e instala boto3 requests

- main.py - *con esto puedes extraer texto a un video que ya tengas en s3*
- openjobresult.py - *con esto puedes descargar el json que se guarda con la operacion de main.py*
- subirarchivo.py - *ejemplo de como subir archivos con python a s3*
- translatefile.py - *traduciendo un archivo que tengas en local*
- translateuri.py - *traduciendo un archivo con la uri del json que se guarda con la operacion de main.py*

## nota: importante saber en que job estas trabajando, cada vez que ejecutas main.py creas un job nuevo

