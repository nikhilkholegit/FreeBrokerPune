# Pune Rent Connect Web App

FastAPI prototype for a Pune house-rental marketplace where owners can post properties and renters can view contact details.

## Features

- Browse Pune rental listings
- Search by area or home type
- Filter by locality
- View property detail page
- Post a new rental listing
- Call or WhatsApp the owner directly

## Run locally

1. Open a terminal in `webapp`
2. Create a virtual environment
3. Install dependencies
4. Start the dev server

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000`

## Hosting options

Easy hosting choices for this app:

- Render
- Railway
- Fly.io
- Any VPS with Docker or Python

## Deployment command

```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Important note

This prototype keeps listings in memory only. If the server restarts, posted data resets.

For production, the next upgrade should be:

- PostgreSQL database
- image uploads
- user login
- owner verification
- admin moderation
