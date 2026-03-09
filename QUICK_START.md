# Quick Start Guide (5 Minutes)

## All-in-One Setup

### Prerequisites Installed? (One-time only)
```bash
pip install flask pandas scikit-learn joblib requests
```

### Step 1: Start Ollama (Terminal 1)
```bash
ollama serve
```
Wait for it to say "Listening on 127.0.0.1:11434"

### Step 2: Start the Server (Terminal 2)
```bash
python app.py
```
You'll see "Running on http://0.0.0.0:5000"

### Step 3: Open in Browser
```
http://localhost:5000
```

### Step 4: Ask a Question!
Type in the search box:
- "Where is CSS explained?"
- "What are HTML forms?"
- "How do I use classes and IDs?"

---

## What You'll See

### 1. Loading Spinner
"Searching through course videos..."

(First query takes 30-60 seconds, rest are faster)

### 2. Answer Section
A detailed explanation of the topic with:
- Clear explanation
- Which videos cover it
- What you'll learn

### 3. Video Segments
Beautiful cards showing:
- Video title and number
- Exact timestamp (MM:SS - MM:SS)
- Relevant transcript text

---

## Common Questions

**Q: How long does the first query take?**
A: 30-60 seconds (models load). Rest are 5-15 seconds.

**Q: Do I need internet?**
A: No! Everything runs locally on your computer.

**Q: Can I change the port?**
A: Yes! Edit the last line of `app.py` and change 5000 to your port.

**Q: What if I get an error?**
A: See the full `SETUP_GUIDE.md` for troubleshooting.

---

**Now go enjoy the course assistant! 🚀**
