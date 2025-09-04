# Tiktok_and_Instagram_analysis

The sentiment_analysis.py file scrapes Instagram comments from a given Instagram Reel.
User gives the URL of a Reel.
The script then scrapes the comments and puts it into a CSV file.

It then opens the CSV file where the comments are located and starts the following:
Tokenize: Breaks down the text into indivdual words or "tokens".
Removes stop words i.e. "and", "the", "of" etc...
Lemmatization: reduce words to their root form.

Each comment is given a score where "1" means positive sentiment and "0" meaning a negative sentiment.

