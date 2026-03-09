# Sigma Web Development - AI Course Assistant

A powerful, AI-driven course assistant that helps students find relevant video content and get detailed explanations for their questions about the Sigma web development course.

## 🎯 Features

- **Smart Question Understanding**: Uses AI embeddings to understand what students are really asking
- **Precise Video Finding**: Identifies the exact videos and timestamps relevant to each question
- **Detailed Explanations**: AI provides context and explanations, not just raw data
- **Beautiful Interface**: Modern, responsive web design that works on all devices
- **Offline & Private**: Everything runs locally on your computer - no cloud services needed
- **Fast**: Gets answers in 5-30 seconds (first query takes longer as models load)

## 📖 Documentation

Start with the document that matches your needs:

### Quick Start (2-5 minutes)
- **[START_HERE.md](START_HERE.md)** - Begin here! Complete overview and quick setup
- **[QUICK_START.md](QUICK_START.md)** - Ultra-fast setup if you're in a hurry

### Learn How to Use (10-20 minutes)
- **[RUN_INSTRUCTIONS.md](RUN_INSTRUCTIONS.md)** - Step-by-step guide with examples
- **[INTERFACE_PREVIEW.md](INTERFACE_PREVIEW.md)** - Visual mockups and design overview

### Understand the System (15-30 minutes)
- **[HOW_IT_WORKS.md](HOW_IT_WORKS.md)** - Complete system architecture and data flow
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup with troubleshooting

### Summary & Status
- **[FINAL_SUMMARY.md](FINAL_SUMMARY.md)** - What's been built and how to use it

## 🚀 Quick Start (TL;DR)

### Prerequisites
```bash
pip install flask pandas scikit-learn joblib requests
```
Download Ollama from: https://ollama.ai

### Run It
```bash
# Terminal 1
ollama serve

# Terminal 2
python app.py

# Browser
http://localhost:5000
```

## 💻 System Requirements

- Python 3.8+
- 8GB RAM minimum (16GB recommended)
- 10GB free disk space
- Modern web browser
- Ollama (AI engine)

## 📁 Project Structure

```
project/
├── app.py                    # Flask web server
├── process_incoming.py       # Query processing engine
├── templates/
│   └── index.html           # Web interface
├── embeddings.joblib        # Video data & embeddings
├── jsons/                   # Source video transcripts
│
├── START_HERE.md            # Read this first
├── QUICK_START.md           # Fast setup guide
├── RUN_INSTRUCTIONS.md      # Step-by-step guide
├── HOW_IT_WORKS.md          # System architecture
├── SETUP_GUIDE.md           # Detailed setup & troubleshooting
├── INTERFACE_PREVIEW.md     # Visual mockups
├── FINAL_SUMMARY.md         # Project summary
└── README.md                # This file
```

## 🎓 How It Works (Simple Version)

1. Student asks: *"Where is CSS explained?"*
2. AI converts question to vector (understands meaning)
3. Compares with all video segments
4. Finds 5 most similar videos
5. AI reads those segments + question
6. Generates helpful explanation
7. Shows answer + video cards with timestamps

**Result**: Student knows exactly which video to watch and when!

## 🌟 Example Usage

### Student Asks:
> "Where is CSS explained?"

### AI Responds:
```
CSS (Cascading Style Sheets) is a styling language used to
control how HTML elements look.

In this course, CSS is primarily taught in:

Video 14 - Introduction to CSS (2:00 - 4:00)
Covers: CSS basics, syntax, how to link CSS files

Video 17 - CSS Selectors MasterClass (1:15 - 8:30)
Covers: How to target specific HTML elements

Video 18 - CSS Box Model (0:00 - 12:45)
Covers: Margins, padding, borders, spacing
```

## ⏱️ Performance

| Action | Time |
|--------|------|
| First question | 30-60 seconds |
| Subsequent questions | 5-15 seconds |
| Page load | 1-2 seconds |
| Average response | ~10 seconds |

## 🔧 Configuration

### Change Port (if 5000 is in use)
Edit `app.py`, last line:
```python
app.run(debug=True, host="0.0.0.0", port=8000)
```

### Change AI Model (for speed)
Edit `process_incoming.py`:
```python
"model" : "mistral"  # Faster responses
```

### Get More Video Segments
Edit `process_incoming.py`:
```python
top_results = 10  # Show 10 instead of 5
```

## 🎨 Interface Features

- ✅ Clean, modern design
- ✅ Responsive (mobile, tablet, desktop)
- ✅ Loading animations
- ✅ Error handling
- ✅ Example questions
- ✅ Beautiful answer formatting
- ✅ Video segment cards
- ✅ Smooth animations

## 🔒 Privacy & Security

- ✅ Everything runs locally on your computer
- ✅ No data sent to external servers
- ✅ No internet required
- ✅ Complete course data privacy
- ✅ Works offline
- ✅ No user tracking

## 🆘 Troubleshooting

### Server Won't Start
Check if port 5000 is available. If not, change to port 8000 in `app.py`.

### Ollama Connection Error
Make sure Ollama is running: `ollama serve`

### No Results
Check that your question is related to web development topics in the course.

### Slow Performance
- Restart Ollama
- Close other applications
- Ensure 8GB+ RAM is available

## 📚 Learning Resources

- **Architecture Diagram**: See HOW_IT_WORKS.md
- **Step-by-Step Setup**: See RUN_INSTRUCTIONS.md
- **Visual Interface**: See INTERFACE_PREVIEW.md
- **Troubleshooting**: See SETUP_GUIDE.md

## 🚀 Getting Started

1. Read **[START_HERE.md](START_HERE.md)** (2 minutes)
2. Follow **[QUICK_START.md](QUICK_START.md)** or **[RUN_INSTRUCTIONS.md](RUN_INSTRUCTIONS.md)**
3. Open http://localhost:5000 in your browser
4. Start asking questions!

## 💡 Tips for Best Results

- Ask clear, specific questions
- Use web development terminology
- First response takes longer (normal!)
- Keep both terminal windows open
- Watch videos at exact timestamps shown

## 🎉 What's Included

✅ Production-ready Flask backend
✅ Beautiful, responsive web interface
✅ Pre-processed video embeddings
✅ Comprehensive documentation
✅ Error handling and validation
✅ Mobile-friendly design
✅ Example questions and quick start

## 📞 Support

For specific help:
- **Quick setup**: QUICK_START.md
- **Step-by-step**: RUN_INSTRUCTIONS.md
- **Understanding the system**: HOW_IT_WORKS.md
- **Troubleshooting**: SETUP_GUIDE.md
- **Visual overview**: INTERFACE_PREVIEW.md

## 🏆 Project Status

✅ **Complete** - Fully functional and ready to use
✅ **Documented** - Comprehensive guides included
✅ **Tested** - Works with all modern browsers
✅ **Optimized** - Fast responses and smooth interface
✅ **Ready for Students** - Can be deployed immediately

## 🎓 Perfect For

- Helping students find relevant course content
- Reducing repetitive Q&A in class
- Providing instant answers 24/7
- Improving student learning experience
- Complementing video lectures with AI assistance

## 📊 Technology Stack

- **Backend**: Flask (Python)
- **AI Models**: Ollama (Local LLM)
- **Vector Search**: scikit-learn (embeddings)
- **Data Processing**: pandas, joblib
- **Frontend**: HTML, CSS, JavaScript
- **HTTP**: REST API with JSON

## ✨ Next Steps

1. Complete initial setup using START_HERE.md
2. Test with various questions
3. Share with students
4. Collect feedback
5. Optimize as needed

---

**Ready to enhance your teaching with AI? Let's go!**

For the quickest start, head to [START_HERE.md](START_HERE.md)
