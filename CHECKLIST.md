# Setup Checklist - Sigma AI Course Assistant

Use this checklist to verify everything is properly set up and working.

## ✅ Prerequisites (One-time)

- [ ] Python 3.8 or higher installed
- [ ] Ollama downloaded from https://ollama.ai
- [ ] Ollama installed on your computer
- [ ] 8GB+ RAM available
- [ ] Flask installed: `pip install flask`
- [ ] pandas installed: `pip install pandas`
- [ ] scikit-learn installed: `pip install scikit-learn`
- [ ] joblib installed: `pip install joblib`
- [ ] requests installed: `pip install requests`

## ✅ Files Present

- [ ] `app.py` exists in project root
- [ ] `process_incoming.py` exists in project root
- [ ] `templates/index.html` exists
- [ ] `embeddings.joblib` exists in project root
- [ ] `jsons/` folder exists with video files
- [ ] All documentation files present:
  - [ ] START_HERE.md
  - [ ] QUICK_START.md
  - [ ] RUN_INSTRUCTIONS.md
  - [ ] HOW_IT_WORKS.md
  - [ ] SETUP_GUIDE.md
  - [ ] INTERFACE_PREVIEW.md
  - [ ] FINAL_SUMMARY.md
  - [ ] CHECKLIST.md (this file)
  - [ ] README.md

## ✅ Ollama Setup

- [ ] Ollama installed
- [ ] Terminal 1 opened
- [ ] Run: `ollama serve`
- [ ] Wait for message: "Listening on 127.0.0.1:11434"
- [ ] Keep this terminal open (don't close it)
- [ ] Verify with: `curl http://localhost:11434/api/tags`

## ✅ Flask Server Setup

- [ ] Open Terminal 2 (different window from Ollama)
- [ ] Navigate to project directory
- [ ] Run: `python app.py`
- [ ] Wait for message: "Running on http://0.0.0.0:5000"
- [ ] Keep this terminal open (don't close it)
- [ ] Flask should show "Debug mode: on"

## ✅ Browser & Interface

- [ ] Open browser (Chrome, Firefox, Safari, etc.)
- [ ] Navigate to: `http://localhost:5000`
- [ ] Page loads without errors
- [ ] See purple gradient header
- [ ] See "Sigma Web Development Course" title
- [ ] See search box is visible
- [ ] See "Ask Question" button
- [ ] See example question pills:
  - [ ] "Where is CSS explained?"
  - [ ] "What are HTML forms?"
  - [ ] "How to use classes and IDs?"
  - [ ] "What are semantic tags?"

## ✅ Test First Query

- [ ] Click on an example pill (or type a question)
- [ ] Search box gets filled with text
- [ ] Click "Ask Question" button
- [ ] Loading spinner appears
- [ ] See text: "Searching through course videos..."
- [ ] Wait 30-60 seconds (this is normal for first query)
- [ ] Spinner disappears
- [ ] Answer appears in purple box
- [ ] Answer contains text explanation
- [ ] Video segment cards appear below answer
- [ ] Each card shows:
  - [ ] Video title
  - [ ] Video number (e.g., "Video #14")
  - [ ] Timestamp (e.g., "2:00 - 4:00")
  - [ ] Relevant transcript text

## ✅ Test Second Query

- [ ] Ask another question (type new one)
- [ ] Click "Ask Question"
- [ ] Loading spinner appears
- [ ] Wait 5-15 seconds (much faster than first!)
- [ ] Answer appears quickly
- [ ] Video cards display

## ✅ Test Different Questions

- [ ] "Where is HTML explained?"
- [ ] "How do I use CSS selectors?"
- [ ] "What are semantic HTML tags?"
- [ ] "How to create forms in HTML?"
- [ ] Custom question related to web development

## ✅ Mobile Testing

- [ ] Open on tablet or mobile device
- [ ] Interface is responsive
- [ ] Search box is usable
- [ ] Buttons are clickable
- [ ] Answer displays properly
- [ ] Cards stack vertically
- [ ] Text is readable

## ✅ Error Handling

- [ ] Try searching empty (empty field): Shows error
- [ ] Type nonsense question: Shows answer or no results
- [ ] Check console (F12) for JavaScript errors: None
- [ ] Check browser console: No 404 errors

## ✅ Performance Verification

- [ ] First query: 30-60 seconds ✓ (normal)
- [ ] Second query: 5-15 seconds ✓ (much faster)
- [ ] Page load: <2 seconds ✓
- [ ] Button clicks: Instant response ✓
- [ ] Animations smooth: Yes ✓

## ✅ Terminal Output Check

### Terminal 1 (Ollama)
- [ ] Shows model loaded: "llama3.2"
- [ ] Shows model loaded: "bge-m3"
- [ ] No error messages
- [ ] Still running and listening

### Terminal 2 (Flask)
- [ ] Shows "Running on http://0.0.0.0:5000"
- [ ] Shows requests being processed
- [ ] Shows POST /ask requests
- [ ] No 500 errors
- [ ] No connection refused errors

## ✅ Files Generated During Use

After first query, check these files were created:
- [ ] `response.txt` created
- [ ] `relevant_chunks.json` created
- [ ] `prompt.txt` created

Check content:
- [ ] `response.txt` contains answer text
- [ ] `relevant_chunks.json` contains 5 video chunks
- [ ] `prompt.txt` contains formatted prompt

## ✅ Documentation Review

- [ ] Read START_HERE.md
- [ ] Read QUICK_START.md
- [ ] Understand RUN_INSTRUCTIONS.md steps
- [ ] Review HOW_IT_WORKS.md (optional but helpful)
- [ ] Know where to find troubleshooting (SETUP_GUIDE.md)

## ✅ Backup Plan

- [ ] Know how to stop Ollama: Ctrl+C in Terminal 1
- [ ] Know how to stop Flask: Ctrl+C in Terminal 2
- [ ] Know how to restart: Repeat the startup steps
- [ ] Know how to change port: Edit app.py last line

## ✅ Ready for Students

- [ ] All checks above passed
- [ ] Both terminals remain open
- [ ] Browser can access http://localhost:5000
- [ ] Multiple questions tested successfully
- [ ] Response quality verified
- [ ] Video timestamps are accurate
- [ ] Ready to share with students

## 🎯 Final Verification Steps

Before deploying to students:

1. **Complete Power Cycle**
   - [ ] Restart computer
   - [ ] Start Ollama: `ollama serve`
   - [ ] Start Flask: `python app.py`
   - [ ] Test in browser
   - [ ] Verify everything still works

2. **Ask Variety of Questions**
   - [ ] Basic topic: "What is HTML?"
   - [ ] Advanced topic: "What are CSS Grid layouts?"
   - [ ] Specific module: "Which video teaches forms?"
   - [ ] Off-topic: "Tell me a joke" (should say not related)

3. **Verify Response Quality**
   - [ ] Answers are accurate
   - [ ] Video numbers are correct
   - [ ] Timestamps point to right content
   - [ ] Explanations are clear
   - [ ] No hallucinated information

4. **Check All Features**
   - [ ] Example pills work
   - [ ] Enter key submits question
   - [ ] Loading state shows
   - [ ] Results display properly
   - [ ] Mobile responsive
   - [ ] No console errors

## 📊 Performance Baseline

Record these times for reference:

| Metric | Time | Status |
|--------|------|--------|
| Page load | ___ seconds | [ ] OK |
| First query | ___ seconds | [ ] 30-60s |
| Second query | ___ seconds | [ ] 5-15s |
| Average query | ___ seconds | [ ] ~10s |

## 🎉 All Done!

If all checkboxes above are checked:

- [ ] System is fully functional
- [ ] Ready for student use
- [ ] Performance meets expectations
- [ ] Documentation complete
- [ ] Backup procedures known
- [ ] Troubleshooting understood

**Congratulations! Your AI Course Assistant is ready! 🚀**

---

## 📞 Troubleshooting Quick Links

If any checkbox failed:

| Issue | Solution |
|-------|----------|
| Ollama won't start | See SETUP_GUIDE.md - Ollama section |
| Flask won't start | See SETUP_GUIDE.md - Port already in use |
| No results | See RUN_INSTRUCTIONS.md - Troubleshooting |
| Slow responses | See SETUP_GUIDE.md - Performance |
| Connection error | Verify both terminals running |
| Files missing | Check project structure section |

---

**Great job getting everything set up! Your students are about to have a much better learning experience.**

Keep this checklist for reference during future deployments! ✨
