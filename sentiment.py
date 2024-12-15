import tkinter as tk
from tkinter import messagebox
from goose3 import Goose
from textblob import TextBlob
from transformers import pipeline
import spacy


# Load spaCy Model
nlp = spacy.load("en_core_web_sm")

# Load Hugging Face Sentiment Model
sentiment_model = pipeline("sentiment-analysis")

# Function to Extract and Analyze Sentiment
def analyze_sentiment():
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Please enter a valid URL!")
        return

    g = Goose()
    try:
        article = g.extract(url=url)
        title_var.set(article.title)
        content_text.delete("1.0", tk.END)
        content_text.insert(tk.END, article.cleaned_text)

        # Entity Extraction
        doc = nlp(article.cleaned_text)
        persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

        persons_text.delete("1.0", tk.END)
        orgs_text.delete("1.0", tk.END)

        persons_text.insert(tk.END, "\n".join(set(persons)) if persons else "None Found")
        orgs_text.insert(tk.END, "\n".join(set(orgs)) if orgs else "None Found")

        # Sentiment Analysis with TextBlob
        blob = TextBlob(article.cleaned_text)
        textblob_sentiment.set(f"Polarity: {blob.sentiment.polarity:.2f}, Subjectivity: {blob.sentiment.subjectivity:.2f}")
        
        # Sentiment Analysis with Hugging Face
        hf_result = sentiment_model(article.cleaned_text[:512])[0]  # Limiting to 512 characters for efficiency
        hf_sentiment.set(f"{hf_result['label']} (Confidence: {hf_result['score']:.2f})")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve article: {e}")


# Create Main Window
root = tk.Tk()
root.title("News Article Sentiment Analyzer")
root.geometry("700x600")

# URL Entry
tk.Label(root, text="Enter Article URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Extract Button
tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment).pack(pady=10)

# Title Display
tk.Label(root, text="Article Title:").pack(pady=5)
title_var = tk.StringVar()
tk.Entry(root, textvariable=title_var, width=60, state="readonly").pack(pady=5)

# Article Content Display
tk.Label(root, text="Article Content:").pack(pady=5)
content_text = tk.Text(root, wrap="word", height=10, width=80)
content_text.pack(pady=5)
# Entity Display
tk.Label(root, text="Extracted Persons:").pack(pady=5)
persons_text = tk.Text(root, wrap="word", height=5, width=80)
persons_text.pack(pady=5)

tk.Label(root, text="Extracted Organizations:").pack(pady=5)
orgs_text = tk.Text(root, wrap="word", height=5, width=80)
orgs_text.pack(pady=5)

# Sentiment Results Display
tk.Label(root, text="Sentiment Analysis (TextBlob):").pack(pady=5)
textblob_sentiment = tk.StringVar()
tk.Entry(root, textvariable=textblob_sentiment, width=60, state="readonly").pack(pady=5)

tk.Label(root, text="Sentiment Analysis (Hugging Face):").pack(pady=5)
hf_sentiment = tk.StringVar()
tk.Entry(root, textvariable=hf_sentiment, width=60, state="readonly").pack(pady=5)

# Start Tkinter Event Loop
root.mainloop()
