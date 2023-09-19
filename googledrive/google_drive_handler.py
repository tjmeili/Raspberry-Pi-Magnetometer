import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/docs']
PATH_TOKEN = 'drive_data/token.json'
PATH_CRED = 'drive_data/credentials.json'

service = None


def initialize():
    creds = None
    global service
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(PATH_TOKEN):
        creds = Credentials.from_authorized_user_file(PATH_TOKEN, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                PATH_CRED, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(PATH_TOKEN, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

# Upload text file
def upload_file(fileName):
    if service is not None:
        file_metadata = {'name': fileName}
        media = MediaFileUpload(fileName, mimetype='text/plain')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        #file.get('id')
        print(fileName + ' upload successful. Probably.')
    else:
        print('Drive service not initialized.')
