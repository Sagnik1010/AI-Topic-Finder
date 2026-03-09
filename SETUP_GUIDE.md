# Sigma Web Development Course - AI Assistant Setup Guide

## Overview
This is an AI-powered course assistant that helps students find relevant video topics and get explanations using a RAG (Retrieval-Augmented Generation) approach.

## Prerequisites

### 1. **Install Required Software**
- Python 3.8+
- Flask
- pandas
- scikit-learn
- joblib
- requests
- Ollama (for local LLM)

### 2. **Install Python Packages**
```bash
pip install flask pandas scikit-learn joblib requests
```

### 3. **Install and Run Ollama**
Download Ollama from: https://ollama.ai

After installation, start Ollama with the required models:
```bash
ollama run bge-m3    # For embeddings
ollama run llama3.2  # For text generation
```

## Project Structure
```
project/
├── app.py                     # Flask backend server
├── process_incoming.py        # Query processing and embedding script
├── templates/
│   └── index.html            # Beautiful web interface
├── embeddings.joblib         # Pre-processed video embeddings
├── jsons/                    # Video chunk JSONs
│   └── [video files].json
├── response.txt              # Last response output
├── relevant_chunks.json      # Related video segments
└── SETUP_GUIDE.md           # This file
```

## Step-by-Step Setup

### Step 1: Verify Ollama is Running
Make sure Ollama is running in the background:
```bash
# In a separate terminal
ollama serve
```

You should see messages indicating the service is listening on `http://localhost:11434`

### Step 2: Verify Embeddings File Exists
Check that `embeddings.joblib` is in the project directory:
```bash
ls -la embeddings.joblib
```

### Step 3: Start the Flask Server
```bash
python app.py
```

You should see output like:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Step 4: Open in Browser
Navigate to:
```
http://localhost:5000
```

## Using the Application

### Web Interface

1. **Ask a Question**: Type your question in the search box
   - Examples:
     - "Where is CSS explained?"
     - "What are HTML forms?"
     - "How do I use classes and IDs?"

2. **See Results**: The interface displays:
   - **Answer**: AI-generated explanation of the topic
   - **Related Video Segments**: Cards showing:
     - Video title
     - Video number
     - Timestamp range (start - end)
     - Actual transcript text

3. **Example Buttons**: Click on suggested questions to auto-fill and search

### Response Format

Each answer includes:
1. **Explanation**: What the topic is and why it matters
2. **Video References**: Which videos cover this topic
3. **Timestamps**: Exact times to watch in each video
4. **Learning Summary**: What students will learn in each section

### Video Segments Display

Each segment card shows:
- **Video Title**: Name of the course video
- **Video #**: Which video number in the course
- **Timestamp**: When in the video the content appears (MM:SS format)
- **Transcript**: Relevant text from that moment

## Troubleshooting

### Issue: "Cannot connect to Ollama"
**Solution**:
- Make sure Ollama is running: `ollama serve`
- Verify it's accessible at `http://localhost:11434`
- Check your firewall settings

### Issue: "embeddings.joblib not found"
**Solution**:
- Make sure the file exists in the project directory
- Run the preprocessing script if needed:
  ```bash
  python preprocess_json.py
  python mp3_to_json.py
  ```

### Issue: "No answer found" or empty results
**Solution**:
- Check that your question is related to web development
- Try a different question format
- Verify Ollama models are running:
  ```bash
  ollama list
  ```

### Issue: Server won't start on port 5000
**Solution**:
- Port 5000 might be in use. Modify `app.py`:
  ```python
  app.run(debug=True, host="0.0.0.0", port=8000)  # Use port 8000
  ```

### Issue: Slow responses
**Solution**:
- First response is slowest (models load into memory)
- Subsequent queries are faster
- This is normal behavior for local LLMs

## API Endpoints

### POST /ask
Sends a question and receives an answer with related video segments

**Request**:
```json
{
  "question": "Where is CSS explained?"
}
```

**Response**:
```json
{
  "answer": "CSS is explained in video 14...",
  "chunks": [
    {
      "title": "Introduction to CSS",
      "number": 14,
      "start": 120,
      "end": 240,
      "text": "CSS is used to style HTML elements..."
    }
  ]
}
```

## Performance Tips

1. **First Query**: Takes 30-60 seconds (models load into memory)
2. **Subsequent Queries**: Takes 5-15 seconds
3. **Internet**: Not required - everything runs locally
4. **RAM**: Ensure at least 8GB available for Ollama models
5. **CPU**: Queries are faster with multi-core processors

## File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Flask web server that serves the UI and API |
| `process_incoming.py` | Processes user questions using embeddings and Ollama |
| `templates/index.html` | Beautiful React-like web interface |
| `embeddings.joblib` | Pre-computed embeddings for all video segments |
| `response.txt` | Cache of the last response |
| `relevant_chunks.json` | Cache of relevant video segments |

## Customization

### Change Port
Edit `app.py`:
```python
app.run(debug=True, host="0.0.0.0", port=YOUR_PORT)
```

### Change Model
Edit `process_incoming.py`:
```python
"model" : "mistral"  # Change to any Ollama model
```

### Change Number of Results
Edit `process_incoming.py`:
```python
top_results = 10  # Show more/fewer relevant segments
```

## Next Steps

1. Share the application URL with students
2. Collect feedback on question quality
3. Fine-tune the prompt for better explanations
4. Add more course videos to the embeddings

---

**Happy Teaching! 🎓**
