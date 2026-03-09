# START HERE - Complete Setup Guide

## 🎯 What You're Building

An AI-powered teaching assistant that:
- Answers student questions about your course
- Shows which video covers each topic
- Provides exact timestamps to watch
- Gives detailed explanations
- Runs 100% offline on your computer

## ⚡ Quick 5-Minute Start

### Prerequisites (Install Once)
```bash
pip install flask pandas scikit-learn joblib requests
```

Download Ollama from: https://ollama.ai

### Run It (3 Steps)

**Terminal 1** - Start AI Engine:
```bash
ollama serve
```

**Terminal 2** - Start Web Server:
```bash
python app.py
```

**Browser** - Open:
```
http://localhost:5000
```

**Done!** 🎉 Ask a question and see results.

---

## 📚 Documentation Files

Choose one based on what you need:

### For Quick Start
→ **QUICK_START.md** (2 min read)
- Super short setup
- Common questions
- Troubleshooting basics

### For Complete Setup
→ **RUN_INSTRUCTIONS.md** (10 min read)
- Step-by-step instructions
- Understanding the output
- Interface guide
- All features explained

### For Understanding the System
→ **HOW_IT_WORKS.md** (15 min read)
- Complete architecture diagram
- Data flow explanation
- Why each component exists
- Performance details

### For Detailed Configuration
→ **SETUP_GUIDE.md** (20 min read)
- Detailed prerequisites
- Installation instructions
- All endpoints documented
- Performance optimization
- Customization options

### For Visual Preview
→ **INTERFACE_PREVIEW.md** (5 min read)
- ASCII mockups of UI
- What you'll see at each step
- Color scheme and animations
- Mobile design

---

## 🚀 What to Do Right Now

### Step 1: Verify Prerequisites
Do you have these installed?
- [ ] Python 3.8+
- [ ] Ollama downloaded
- [ ] 8GB+ RAM available

### Step 2: Install Dependencies
```bash
pip install flask pandas scikit-learn joblib requests
```

### Step 3: Start Ollama (Terminal 1)
```bash
ollama serve
```

Wait for: `Listening on 127.0.0.1:11434`

### Step 4: Start Server (Terminal 2)
```bash
python app.py
```

Wait for: `Running on http://0.0.0.0:5000`

### Step 5: Open Browser
Go to: `http://localhost:5000`

### Step 6: Test It
Ask a question:
- "Where is CSS explained?"
- "What are HTML forms?"
- "How do I use JavaScript?"

---

## 📊 What You Should See

### 1. Interface Loads
Beautiful purple interface with:
- Search box at top
- Example questions as buttons
- Instructions

### 2. After Asking
- Purple answer box with explanation
- Video segment cards below
- Each card shows: Video #, Timestamp, Transcript

### 3. Performance Timeline
- First query: 30-60 seconds (normal)
- Rest: 5-15 seconds

---

## ✅ Checklist: Is It Working?

- [ ] Can you open http://localhost:5000?
- [ ] Does the page load with purple interface?
- [ ] Can you type in the search box?
- [ ] Click "Ask Question" shows spinner?
- [ ] After 30 seconds, see answer appear?
- [ ] Video cards show below answer?

All yes? **Congratulations! You're all set!** 🎉

---

## 🆘 Common Issues

### "Cannot connect to server"
→ Make sure Terminal 2 is running: `python app.py`

### "Cannot connect to Ollama"
→ Make sure Terminal 1 is running: `ollama serve`

### Very slow (>60 seconds after first)
→ Restart Ollama, close other apps, check RAM

### Port 5000 already in use?
→ Edit app.py last line, change 5000 to 8000

---

## 🎓 How It Works (Simple Version)

1. Student asks: "Where is CSS explained?"
2. Question → Vector (AI understands meaning)
3. Compare with all video chunks
4. Find 5 most similar videos
5. AI reads those chunks + question
6. AI writes natural explanation
7. Show answer + video cards with timestamps

**Result**: Student knows exactly which video to watch!

---

## 📁 Key Files

```
app.py                    ← Run this (Terminal 2)
process_incoming.py       ← Processes questions
templates/index.html      ← The web interface
embeddings.joblib        ← All video data
```

---

## 🔧 Common Customizations

### Change Port (if 5000 taken)
Edit `app.py` last line:
```python
app.run(debug=True, host="0.0.0.0", port=8000)
```

### Change AI Model (for speed)
Edit `process_incoming.py`:
```python
"model" : "mistral"  # Faster, less detailed
```

### Get More Video Segments
Edit `process_incoming.py`:
```python
top_results = 10  # Show 10 instead of 5
```

---

## 💡 Pro Tips

1. **First query slowest**: Normal! Models load into RAM
2. **No internet needed**: Everything is local
3. **Data is private**: Your course content never leaves your computer
4. **Multiple users**: Can share URL on your network
5. **Keep both terminals open**: They run continuously

---

## 📞 Need Help?

1. Check **QUICK_START.md** for common questions
2. See **RUN_INSTRUCTIONS.md** for detailed guide
3. Read **HOW_IT_WORKS.md** to understand the system
4. Check **SETUP_GUIDE.md** for troubleshooting

---

## 🎉 Next Steps

After setup works:

1. **Share with students**: Give them http://localhost:5000
2. **Collect feedback**: Which questions do they ask?
3. **Refine prompts**: Improve answer quality
4. **Add more videos**: Include additional course material
5. **Optimize speed**: Adjust models for faster responses

---

## 📊 Project Status

Your project is now:
- ✅ **Beautiful UI**: Modern purple interface
- ✅ **Smart Answers**: AI provides explanations
- ✅ **Video Finding**: Shows exact timestamps
- ✅ **Fast**: Local processing, no API calls
- ✅ **Private**: All data stays on your computer
- ✅ **Documented**: Complete guides included

**You're ready to enhance your teaching!** 🚀

---

## 🎯 Quick Reference

```
What to Run           Command              Terminal
─────────────────────────────────────────────────────
AI Engine            ollama serve         Terminal 1
Web Server           python app.py        Terminal 2
Open in Browser      localhost:5000       Browser

How Long It Takes
─────────────────────────────────────────────────────
First question       30-60 seconds
Later questions      5-15 seconds
Page load            1-2 seconds
```

---

**Ready? Let's go!**

```
Terminal 1: ollama serve
Terminal 2: python app.py
Browser:   http://localhost:5000
```

Start asking questions! 🎓✨
