import tkinter as tk
from tkinter import messagebox
from goose3 import Goose

# Function to Extract Article
def extract_article():
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
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve article: {e}")

# Main Window
root = tk.Tk()
root.title("News Article Scraper")
root.geometry("600x500")

# URL Entry
tk.Label(root, text="Enter Article URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Extract Button
tk.Button(root, text="Extract Article", command=extract_article).pack(pady=10)

# Title Display
tk.Label(root, text="Article Title:").pack(pady=5)
title_var = tk.StringVar()
tk.Entry(root, textvariable=title_var, width=60, state="readonly").pack(pady=5)

# Content Display
tk.Label(root, text="Article Content:").pack(pady=5)
content_text = tk.Text(root, wrap="word", height=15, width=70)
content_text.pack(pady=5)

# Starting Loop
root.mainloop()
