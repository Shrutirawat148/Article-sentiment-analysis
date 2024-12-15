import tkinter as tk
from tkinter import messagebox
from goose3 import Goose
import spacy

# Load spaCy Model
nlp = spacy.load("en_core_web_sm")

# Function to Extract Article and Entities
def extract_entities():
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

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve article: {e}")

# Create Main Window
root = tk.Tk()
root.title("News Article Scraper with NER")
root.geometry("700x600")

# URL Entry
tk.Label(root, text="Enter Article URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Extract Button
tk.Button(root, text="Extract Article and Entities", command=extract_entities).pack(pady=10)

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

# Start Tkinter Event Loop
root.mainloop()
