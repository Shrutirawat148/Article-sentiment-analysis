from goose3 import Goose

# Function to fetch and parse article content
def fetch_article_content(url):
    try:
        # Initialize Goose3
        g = Goose()
        article = g.extract(url=url)
        
        # Extract Title and Main Content
        title = article.title
        content = article.cleaned_text
        
        if content:
            return {"title": title, "content": content.strip()}
        else:
            return {"error": "No article content found."}
    
    except Exception as e:
        return {"error": f"Error fetching the article: {e}"}

# Example Usage
if __name__ == "__main__":
    url = input("Enter the news article URL: ")
    result = fetch_article_content(url)
    print("\nExtracted Article:\n")
    print(f"Title: {result.get('title', 'N/A')}\n")
    print(result.get('content', 'Content not found.'))
