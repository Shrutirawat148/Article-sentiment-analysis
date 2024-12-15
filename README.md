# Article-sentiment-analysis
 
This project focuses on extracting meaningful data from Wikipedia articles and performing sentiment analysis and entity extraction on the text. The workflow involves:

Data Extraction: The content of the Wikipedia article is extracted using the Goose library, which removes any HTML tags and gives clean text for analysis.

Entity Extraction: The project uses spaCy’s Named Entity Recognition (NER) to identify entities such as names of people, organizations, locations, and other key terms within the text.

Sentiment Analysis: Sentiment analysis is performed using two approaches:

TextBlob: This library is used to determine the polarity (positive or negative sentiment) and subjectivity (fact vs opinion) of the text.
Hugging Face’s Transformers: A more advanced model is used to classify the sentiment as positive, negative, or neutral.
UI: A simple user interface is created using the Tkinter library to display the extracted data in an easy-to-read format.

Database Integration: All extracted data, including the named entities and sentiment analysis results, are stored in a database for further use and analysis.

I started the project by using a Wikipedia URL as the input.

URL used: https://en.wikipedia.org/wiki/Syrian_civil_war

The first task was to extract the article's content, for which I used the Goose library. This tool allowed me to retrieve the article's title and the main text. The cleaned text function helped remove any HTML tags, making the content cleaner and easier to process (see the file: extract.py).

Then, I created a simple user interface (UI) using the Tkinter library to display the extracted text (see the file: app.py).
For Entity Extraction, I used spaCy, a popular tool for natural language processing (NLP). Specifically, I used the pre-trained en_core_web_sm model to identify and extract named entities (such as people, organizations, and locations) from the text. (see the file: ner.py).

For Sentiment Analysis, I used two methods:
  1.	TextBlob: This library provides a pretrained model to analyze sentiment. It gives two main measures:
     
       o	Polarity: Ranges from -1 to +1, indicating whether the text is negative or positive.
       
       o	Subjectivity: Ranges from 0.0 to 1.0, showing how much the text is based on personal opinions or factual information.
  3.	Hugging Face Transformers: This library uses advanced models to classify the sentiment of the text as either positive, negative, or neutral.
  4.	(see the file: sentiment.py).

Finally, all the extracted data, including named entities and sentiment analysis results, were stored in a database for later use.
The entire assignment is in the file withdb.py.
