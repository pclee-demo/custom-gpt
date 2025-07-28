from flask import Flask, jsonify
from google.oauth2 import service_account
from googleapiclient.discovery import build
import mammoth
import io
import requests

app = Flask(__name__)

# Authenticate with Google Drive API
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Uploaded to Replit project
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
drive_service = build('drive', 'v3', credentials=credentials)

# Shared folder ID from Google Drive
FOLDER_ID = '1SpPD8xsMWt1y0SOczr-PigNGrNBF3GMB'  # Replace this with shared folder's ID


# Get document by file ID
@app.route('/drive/<file_id>', methods=['GET'])
def read_docx(file_id):
    try:
        # Download the file content as binary
        file = drive_service.files().get_media(fileId=file_id).execute()
        with io.BytesIO(file) as docx_file:
            result = mammoth.extract_raw_text(docx_file)
            return jsonify({'text': result.value})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# List all .docx files in the shared folder, except for Onboarding_Requirements.docx
@app.route('/list-docs', methods=['GET'])
def list_docs():
    try:
        results = drive_service.files().list(
            q=f"'{FOLDER_ID}' in parents and mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'",
            fields="files(id, name)"
        ).execute()

        files = results.get('files', [])

        filtered_files = [
            {"name": f["name"], "id": f["id"]}
            for f in files
            if f["name"] != "Onboarding_Requirements.docx"
        ]

        return jsonify({
            "documents": filtered_files
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Read a document by its filename
@app.route('/drive/by-name/<filename>', methods=['GET'])
def get_doc_by_name(filename):
    try:
        results = drive_service.files().list(
            q=f"'{FOLDER_ID}' in parents and name = '{filename}' and mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'",
            fields="files(id, name)"
        ).execute()

        files = results.get('files', [])

        if not files:
            return jsonify({"error": "File not found"}), 404

        file_id = files[0]["id"]
        return read_docx(file_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)