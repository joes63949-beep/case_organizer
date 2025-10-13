import json, os, hashlib
from uuid import uuid4
from datetime import datetime
from cryptography.fernet import Fernet
from reportlab.pdfgen import canvas

KEY_FILE = "secret.key"
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    fernet = Fernet(f.read())

DATA_FILE = "records.enc"

def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "rb") as f:
        decrypted = fernet.decrypt(f.read()).decode()
        return json.loads(decrypted)

def save_records(records):
    encrypted = fernet.encrypt(json.dumps(records, indent=2).encode())
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def add_record(text, source="note", tags=None):
    rec = {
        "id": uuid4().hex,
        "timestamp_added": datetime.utcnow().isoformat(),
        "source": source,
        "text": text,
        "tags": tags or [],
        "hash": hashlib.sha256(text.encode()).hexdigest()
    }
    records = load_records()
    records.append(rec)
    save_records(records)
    print("Record stored locally and encrypted.")

def export_pdf(filename="case_notes.pdf"):
    records = load_records()
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 10)
    y = 800
    for r in records:
        c.drawString(20, y, f"Date: {r['timestamp_added']}")
        y -= 14
        c.drawString(20, y, f"Tags: {', '.join(r['tags'])}")
        y -= 14
        text = r['text'][:500].replace("\n", " ")
        c.drawString(20, y, f"Text: {text}")
        y -= 30
        if y < 100:
            c.showPage()
            y = 800
    c.save()
    print(f"PDF exported: {filename}")

if __name__ == "__main__":
    print("Case Materials Organizer")
    print("1. Add note")
    print("2. Export PDF")
    choice = input("Choose: ")
    if choice == "1":
        text = input("Enter note or message text:\n")
        tags = input("Tags (comma separated): ").split(",")
        add_record(text, tags=[t.strip() for t in tags])
    elif choice == "2":
        export_pdf()

