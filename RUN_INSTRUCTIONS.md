# How to Run the Sigma Web Development AI Course Assistant

## Complete Step-by-Step Instructions

### Prerequisites Check
Before you start, make sure you have:
- Python 3.8 or higher
- Ollama installed (download from https://ollama.ai)
- About 8GB of available RAM
- The `embeddings.joblib` file in your project directory

### Part 1: Install Dependencies (One-time only)

Open your terminal/command prompt and run:
```bash
pip install flask pandas scikit-learn joblib requests
```

### Part 2: Start the Services

**IMPORTANT: Keep these running while using the application!**

#### Terminal 1: Start Ollama Service
```bash
ollama serve
```

You should see:
```
pulling manifest
...
Listening on 127.0.0.1:11434
```

Let it sit there - don't close this terminal. This is your AI engine running.

#### Terminal 2: Start Flask Server
```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

Let it sit there - don't close this terminal. This is your web server.

### Part 3: Open the Web Application

Open your web browser and navigate to:
```
http://localhost:5000
```

You should see a beautiful purple interface with the title:
**"Sigma Web Development Course"**

### Part 4: Ask Questions!

#### Example 1: Basic Question
1. Click in the search box
2. Type: `Where is CSS explained?`
3. Press Enter or click "Ask Question"
4. Watch the loading spinner...
5. See the answer and related videos

#### Example 2: Using Quick Examples
1. Click on one of the example pills:
   - "Where is CSS explained?"
   - "What are HTML forms?"
   - "How to use classes and IDs?"
   - "What are semantic tags?"

#### Example 3: Your Own Questions
Try any of these:
- "What are HTML tags?"
- "How do I create a webpage?"
- "What is the box model in CSS?"
- "How to use JavaScript in HTML?"
- "What are semantic HTML elements?"

---

## Understanding the Output

### What You See on Screen

#### 1. Answer Section (Purple Box)
```
💡 Answer
────────────────────────
CSS (Cascading Style Sheets) is a styling language used to
control how HTML elements look. It handles colors, fonts,
spacing, and layout.

In this course, CSS is introduced in Video 14 at 2:00. This
video covers the basics of CSS including selectors, properties,
and how to link CSS files to HTML.
```

#### 2. Related Video Segments Cards
```
Introduction to CSS
Video #14
⏱️ 2:00 - 4:00
═══════════════════════════════════════
CSS is used to style HTML elements and
control how they appear in the browser.
You'll learn about selectors, properties,
and values...
```

Each card shows:
- **Video title**: What the video is about
- **Video number**: Position in course sequence
- **Timestamp**: Exact time to watch (Minutes:Seconds - Minutes:Seconds)
- **Transcript**: Relevant text from that moment

---

## Timing Guide

### First Query
- **Time**: 30-60 seconds
- **Why**: The AI models load from disk into memory
- **Normal?**: Yes! This is expected

### Subsequent Queries
- **Time**: 5-15 seconds
- **Why**: Models stay loaded in memory
- **Speed increase**: 3-4x faster after first query

### Very Long Answers
- **Time**: 20-30 seconds
- **Why**: Generating longer text takes more time
- **Normal?**: Yes, depends on complexity

---

## Interface Features

### Search Box
- Type your question
- Press Enter or click button
- Auto-complete suggestions appear

### Example Pills
- Quick access to sample questions
- Click to auto-fill search box
- Great for first-time users

### Loading State
- Shows spinner while processing
- Displays "Searching through course videos..."
- Click other areas while waiting

### Answer Display
- Purple gradient background
- Easy to read formatting
- Shows complete explanation

### Video Segment Cards
- Blue left border
- Hover for animations
- Shows full transcript snippet
- Click to focus if needed

---

## What If Something Goes Wrong?

### Error: "Cannot connect to server"
**Problem**: Flask server not running
**Solution**:
```bash
# In Terminal 2, run:
python app.py
```

### Error: "Cannot connect to Ollama"
**Problem**: Ollama service not running
**Solution**:
```bash
# In Terminal 1, run:
ollama serve
```

### Error: "embeddings.joblib not found"
**Problem**: Missing preprocessing file
**Solution**: The file should be in the project directory. Check that you have it:
```bash
ls embeddings.joblib
```

### Error: "No answer found" / Empty results
**Problem**: Question too different from course content
**Solution**: Try asking about web development topics covered in the course

### Issue: Very slow responses (>30 seconds for 2nd query)
**Problem**: System running slow
**Solution**:
- Close other applications
- Restart Ollama
- Check available RAM (need ~8GB)

### Issue: Server crashes after first query
**Problem**: Memory issue
**Solution**:
- Close other applications
- Restart both servers
- Restart Ollama: `ollama serve`

---

## Advanced Tips

### Change Port (If 5000 is in use)
Edit `app.py`, last line:
```python
app.run(debug=True, host="0.0.0.0", port=8000)  # Change 5000 to 8000
```
Then visit: `http://localhost:8000`

### Faster Responses (Use lighter model)
Edit `process_incoming.py`, find this line:
```python
"model" : "llama3.2"
```
Try `mistral` or `neural-chat` for faster responses (but less detailed)

### More Detailed Responses
Edit `process_incoming.py`, in the prompt section, add:
```
4. Provide specific examples
5. Explain why this is important
6. Show common mistakes
```

### More Video Segments
Edit `process_incoming.py`, find:
```python
top_results = 5
```
Change to `10` or `15` for more segments

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Submit question (when in search box) |
| Tab | Move between elements |
| Click Example Pill | Auto-fill question and search |

---

## File Locations

All files should be in the project root directory:
```
.../project/
├── app.py                    ← Start with: python app.py
├── process_incoming.py       ← Handles queries
├── templates/
│   └── index.html           ← The web interface
├── embeddings.joblib        ← Video data
├── jsons/                   ← Source data
│   └── *.json
├── QUICK_START.md          ← Quick reference
├── SETUP_GUIDE.md          ← Detailed setup
├── HOW_IT_WORKS.md         ← System explanation
└── RUN_INSTRUCTIONS.md     ← This file
```

---

## Testing Your Setup

### Quick Test Script
Copy this to test your system:

```bash
# Test 1: Check Python
python --version

# Test 2: Check dependencies
python -c "import flask; import pandas; import sklearn; print('All packages installed!')"

# Test 3: Check Ollama
curl http://localhost:11434/api/tags

# Test 4: Check Flask server
curl http://localhost:5000/

# Test 5: Test API
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is HTML?"}'
```

---

## Performance Optimization

### Hardware Recommendations
- **RAM**: 8GB minimum (16GB recommended)
- **CPU**: Multi-core processor (4+ cores)
- **Storage**: 10GB free space
- **Internet**: Not required (works offline)

### Running Ollama Efficiently
```bash
# Run with GPU acceleration (faster)
ollama run llama3.2 --gpu=1

# Run with limited memory
export OLLAMA_NUM_THREADS=4
ollama serve
```

### Monitor System While Running
```bash
# Linux/Mac
top

# Windows
tasklist
```

---

## Stopping the Application

### When You're Done
1. **Stop Flask**: Ctrl+C in Terminal 2
2. **Stop Ollama**: Ctrl+C in Terminal 1
3. **Close Browser**: Close the browser tab

### Restart Later
Just run:
```bash
# Terminal 1
ollama serve

# Terminal 2
python app.py
```

---

## Summary

You now have a fully functional AI-powered course assistant that:

✓ Understands student questions
✓ Finds relevant video content
✓ Provides detailed explanations
✓ Shows exact timestamps to watch
✓ Works completely offline
✓ Runs on your local computer

**Ready to teach your Sigma course? Let's go!** 🚀

---

For more details:
- System architecture: See `HOW_IT_WORKS.md`
- Troubleshooting: See `SETUP_GUIDE.md`
- Quick reference: See `QUICK_START.md`
