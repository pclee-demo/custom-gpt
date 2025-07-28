# Backend – Google Drive Document Extraction Service

This folder contains the Flask backend that supports the Custom GPT demo by providing endpoints for `.docx` document retrieval and text extraction from Google Drive.

---

## ⚙️ **Features**
- `GET /drive/<file_id>` – downloads a `.docx` from Google Drive by file ID and extracts text using Mammoth.
- `GET /list-docs` – lists available `.docx` documents in the shared Drive folder.
- `GET /drive/by-name/<filename>` – fetches and extracts a document by filename.

---

## **Running Locally**

### 1. Clone the Repository
```bash
git clone https://github.com/pclee-demo/gpt-airtable.git
cd gpt-airtable/backend
```

### 2. Install Dependencies
Preferred (using requirements.txt):
```bash
pip install -r requirements.txt
```

Alternative:
```bash
pip install flask google-auth google-api-python-client mammoth requests
```

### 3. Add Google Service Account Credentials
Create a service account in Google Cloud Console and enable the Drive API.
Grant it access to the shared folder.
Download the key as `credentials.json` and place it in this `backend/` directory.

### 4. Run the Server
```bash
python3 main.py
```
The server will start on http://localhost:3000.

---

## **Security Notes**
Do not commit credentials.json or any secrets.
This backend is for demonstration purposes only.
Reviewers do not need to run this backend to test the GPT workflow.
