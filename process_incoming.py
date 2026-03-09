import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests
import numpy as np
import joblib
import sys
import json

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model" : "bge-m3",
        "input": text_list
    })

    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model" : "llama3.2",
        "prompt": prompt,
        "stream" : False
    })
    response = r.json()
    return response


df = joblib.load('embeddings.joblib')

# Get query from command line argument
incoming_query = sys.argv[1] if len(sys.argv) > 1 else input("Ask a Question: ")

question_embedding = create_embedding([incoming_query])[0]

# Find similarities of question_embedding with other embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results]
new_df = df.loc[max_indx]

# Enhanced prompt with explanation request
prompt = f'''I am teaching web development in my Sigma web development course.
Here are video subtitle chunks containing video title, video number, start time in seconds,
end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
User asked: "{incoming_query}"

Please provide a comprehensive response that includes:
1. A clear explanation of the topic they're asking about
2. Which video(s) cover this topic with specific video numbers
3. The timestamp ranges where this content appears
4. A brief summary of what they'll learn in each relevant section

Answer in a friendly, helpful way as if you're a teaching assistant guiding a student through the course.
If the question is unrelated to the course, politely explain that you can only answer questions about web development topics covered in the Sigma course.
'''

with open('prompt.txt', 'w') as f:
    f.write(prompt)

response = inference(prompt)["response"]

with open('response.txt', 'w') as f:
    f.write(response)

# Save relevant chunks for the UI
chunks_data = new_df[["title", "number", "start", "end", "text"]].to_dict('records')
with open('relevant_chunks.json', 'w') as f:
    json.dump(chunks_data, f)
