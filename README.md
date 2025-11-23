# Case Organizer

A secure case materials organizer with encryption and PDF export capabilities.

## Features

- 🔐 Encrypted storage of case records
- 📝 Add notes with tags and timestamps
- 📄 Export records to PDF format
- 🔒 AES encryption using Fernet

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

## AI Coding Assistant

Want AI-powered help for coding, debugging, and analyzing this project?

**👉 See [AI_SETUP_GUIDE.md](AI_SETUP_GUIDE.md) for complete instructions on setting up GitHub Copilot and other AI tools in VS Code!**

This repository includes VS Code configuration for:
- GitHub Copilot (code suggestions and chat)
- Python language support
- Recommended extensions

Simply open this folder in VS Code and install the recommended extensions when prompted.

## Project Structure

- `app.py` - Main application with encryption and PDF export
- `requirements.txt` - Python dependencies
- `secret.key` - Encryption key (auto-generated)
- `records.enc` - Encrypted data storage
- `.vscode/` - VS Code configuration with AI tool recommendations

## Usage

The application provides two main functions:

1. **Add Note**: Store encrypted notes with tags
2. **Export PDF**: Generate PDF of all stored records

All data is encrypted at rest using Fernet symmetric encryption.
