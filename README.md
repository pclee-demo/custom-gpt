# Custom GPT Demo – Backend Component

This repository contains the backend service used as part of the Custom GPT demo.  

---

## 📌 **Project Context**

This backend works with the Custom GPT to:
- Fetch `.docx` onboarding documents from Google Drive
- Extract text
- Return structured data for GPT parsing and task logging into Airtable

The GPT workflow also supports manual document upload directly in the chat.

---

## **How It Works**
- `main.py` runs a lightweight Flask API.
- It authenticates to Google Drive using a service account.
- Endpoints expose `.docx` extraction capabilities to the Custom GPT.

---

## **Running the Backend**
To run the backend locally, see the detailed instructions in [`backend/README.md`](backend/README.md).

---

## **Security Note**
This repository does not include `credentials.json` or any secrets.  
To replicate the backend, you must create a Google service account and provide your own credentials.

---
