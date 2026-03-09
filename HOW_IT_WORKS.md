# How the AI Course Assistant Works

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          WEB BROWSER                                │
│                      (localhost:5000)                               │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              Beautiful Web Interface (HTML/CSS/JS)           │  │
│  │                                                              │  │
│  │  User types question: "Where is CSS explained?"             │  │
│  │  ├─ Checks for empty input                                 │  │
│  │  └─ Shows loading spinner                                  │  │
│  └──────────────────────────┬──────────────────────────────────┘  │
└─────────────────────────────┼────────────────────────────────────────┘
                              │ HTTP POST /ask
                              │ {"question": "..."}
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      FLASK SERVER (app.py)                          │
│                      (localhost:5000)                               │
│                                                                     │
│  @app.route("/ask", methods=["POST"])                              │
│  ├─ Receives user question                                         │
│  ├─ Validates input                                                │
│  └─ Calls process_incoming.py                                      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           │ subprocess.run()
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│                  QUERY PROCESSOR (process_incoming.py)              │
│                                                                     │
│  Step 1: Create Question Embedding                                 │
│  ├─ Input: "Where is CSS explained?"                              │
│  ├─ Call: Ollama API (bge-m3 model)                               │
│  └─ Output: [0.234, -0.156, 0.892, ...]  (384-dimensional vector)│
│                                                                     │
│  Step 2: Find Similar Video Chunks                                 │
│  ├─ Load: embeddings.joblib (all video chunks + embeddings)       │
│  ├─ Compare: Question embedding vs all chunk embeddings           │
│  │          Using cosine similarity                                │
│  └─ Result: Top 5 most similar chunks                             │
│                                                                     │
│  Step 3: Create Enhanced Prompt                                    │
│  ├─ Include: Top 5 relevant video chunks                          │
│  ├─ Include: Original user question                               │
│  └─ Include: Instructions for AI (format, explanation)            │
│                                                                     │
│  Step 4: Generate Answer                                           │
│  ├─ Call: Ollama API (llama3.2 model)                             │
│  ├─ Prompt: "User asked: ... Here are relevant chunks: ..."       │
│  └─ Output: Detailed explanation with video references            │
│                                                                     │
│  Step 5: Save Results                                              │
│  ├─ Write: response.txt (the AI-generated answer)                 │
│  └─ Write: relevant_chunks.json (the 5 chunk details)             │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│              OLLAMA API (localhost:11434)                           │
│                   Running on Your Computer                          │
│                                                                     │
│  Model 1: bge-m3                                                    │
│  └─ Purpose: Creates embeddings (converts text to vectors)         │
│     Time: ~0.5 seconds per embedding                               │
│                                                                     │
│  Model 2: llama3.2                                                  │
│  └─ Purpose: Generates human-like responses                        │
│     Time: ~5-30 seconds per response                               │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ JSON responses
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│              FLASK SERVER (app.py) - Response                       │
│                                                                     │
│  ├─ Read: response.txt                                             │
│  ├─ Read: relevant_chunks.json                                     │
│  └─ Return: JSON response to browser                               │
│     {                                                               │
│       "answer": "CSS is explained in video 14...",                 │
│       "chunks": [                                                   │
│         {                                                           │
│           "title": "Introduction to CSS",                          │
│           "number": 14,                                            │
│           "start": 120,                                            │
│           "end": 240,                                              │
│           "text": "CSS is used to style..."                       │
│         },                                                          │
│         ...                                                         │
│       ]                                                             │
│     }                                                               │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ HTTP Response (JSON)
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│                          WEB BROWSER                                │
│                                                                     │
│  Step 1: Hide loading spinner                                      │
│  Step 2: Display answer in purple box                              │
│  Step 3: Create cards for each video segment                       │
│  ├─ Title: "Introduction to CSS"                                  │
│  ├─ Video: "Video #14"                                            │
│  ├─ Time: "2:00 - 4:00"                                           │
│  └─ Text: "CSS is used to style..."                              │
│  Step 4: Show results section with smooth animation               │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow Example

### User Question: "Where is CSS explained?"

### 1. Browser → Server
```json
{
  "question": "Where is CSS explained?"
}
```

### 2. Embedding Creation
```
Question Text: "Where is CSS explained?"
↓
(sent to Ollama bge-m3 model)
↓
Embedding Vector: [0.234, -0.156, 0.892, ..., 0.445]  (384 dimensions)
```

### 3. Similarity Search
```
Compare question embedding with all video chunk embeddings using cosine similarity

Video Chunk 1 (Intro to CSS):       Similarity: 0.87 ← Top match!
Video Chunk 2 (CSS Selectors):      Similarity: 0.84 ← 2nd match
Video Chunk 3 (CSS Box Model):      Similarity: 0.81 ← 3rd match
Video Chunk 4 (HTML Forms):         Similarity: 0.45 ← Not relevant
Video Chunk 5 (JavaScript):         Similarity: 0.12 ← Not relevant
...
```

### 4. Prompt Generation
```
"I am teaching web development in my Sigma web development course.
Here are video subtitle chunks:

[
  {
    "title": "Introduction to CSS",
    "number": 14,
    "start": 120,
    "end": 240,
    "text": "CSS is used to style HTML elements..."
  },
  {
    "title": "CSS Selectors",
    "number": 17,
    "start": 45,
    "end": 180,
    "text": "CSS selectors are used to target elements..."
  },
  ...
]

User asked: 'Where is CSS explained?'

Please provide:
1. A clear explanation of CSS
2. Which videos cover this topic
3. Timestamp ranges
4. What they'll learn"
```

### 5. AI Generation
```
Input:  The prompt above + top 5 relevant chunks
↓
(sent to Ollama llama3.2 model)
↓
Output: "CSS (Cascading Style Sheets) is a fundamental web technology
used to style and layout HTML elements. In this course, CSS is primarily
taught in Video 14 (Introduction to CSS) starting at 2:00, where we cover
the basics of CSS syntax and how to apply styles...

For more advanced topics:
- Video 17 (CSS Selectors) teaches how to target specific elements
- Video 18 (CSS Box Model) explains margins, padding, and borders
..."
```

### 6. Response Display
```
Browser receives JSON:
{
  "answer": "CSS (Cascading Style Sheets) is...",
  "chunks": [
    {
      "title": "Introduction to CSS",
      "number": 14,
      "start": 120,
      "end": 240,
      "text": "CSS is used to style HTML elements..."
    },
    ...
  ]
}

Renders:
┌──────────────────────────────────────┐
│ Answer (in purple box)               │
│ CSS is a fundamental technology...   │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ Related Video Segments               │
├──────────────────────────────────────┤
│ Introduction to CSS     [Video #14]  │
│ 2:00 - 4:00                          │
│ "CSS is used to style..."            │
└──────────────────────────────────────┘
  (more cards...)
```

## Key Files

### embeddings.joblib
- Contains all video chunks with their embeddings
- Created during preprocessing
- Structure:
  ```
  DataFrame with columns:
  - title: Video title
  - number: Video number
  - start: Timestamp start
  - end: Timestamp end
  - text: Transcript text
  - embedding: Vector representation [384 dimensions]
  ```

### process_incoming.py Functions

```python
create_embedding(text_list)
├─ Input: List of text strings
├─ Calls: Ollama API (bge-m3)
└─ Output: List of embedding vectors

inference(prompt)
├─ Input: Prompt text
├─ Calls: Ollama API (llama3.2)
└─ Output: Generated response text
```

## Why This Works

1. **Semantic Search**: Embeddings capture meaning, not just keywords
   - "Where is CSS?" matches chunks about "CSS fundamentals"
   - Not just string matching

2. **Context Aware**: AI sees the actual video content
   - Provides accurate video numbers and timestamps
   - Can explain what students will learn

3. **Conversational**: Using llama3.2 for natural responses
   - Sounds like a helpful teaching assistant
   - Not just returning raw video chunks

4. **Fast**: Most processing happens locally
   - No internet required
   - Complete privacy for your course data

## Performance Characteristics

| Phase | Time | Notes |
|-------|------|-------|
| Embedding question | 0.5s | (Fast) |
| Find similar chunks | 0.1s | (Very fast) |
| Generate response | 5-30s | (Depends on answer length) |
| **Total** | **5-31s** | **First query slower** |

After first query:
- First query: 30-60s (models load into RAM)
- Subsequent queries: 5-15s (models already loaded)

---

Ready to get started? See `QUICK_START.md`!
