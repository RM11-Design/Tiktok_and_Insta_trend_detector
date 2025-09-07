from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import creds
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import time

# while True:
instagram_video_link = input("Enter Instagram reel link: ")
    
    # # if instagram_video_link.startswith == "https://www.instagram.com/":
    # #     break
    # else:
    #     print("Please enter a valid link")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    page = browser.new_page()
    page.goto(instagram_video_link)
    
    # Click on decline cookies    
    page.get_by_role("button", name="Decline optional cookies").click()
    
    # Click on X button   
    page.locator("div[role='button']", has=page.locator("svg[aria-label='Close']")).click()
    
    # all_spans = page.locator('//span').all()
    all_spans = page.locator('//span[contains(@style, "--x-lineHeight: 20px")]').all()
    
    page.mouse.down(335, 400.44)
    
    # for x in range(1,5):
    #     page.keyboard.press("End")
    #     print("scrolling key press",x)
    #     time.sleep(3)
    # Click on more comments button

    comments = []
    for span in all_spans:
        comments.append(span.text_content())
        
    # time.sleep(5)
        
filename = "comments.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file,fieldnames=["Comments"])
    for comment in comments:
        writer.writerow({"Comments": comment})

h = ["Comments"]
comments = pd.read_csv("comments.csv", header=None, names=h)   
comments.to_csv("comments.csv", index=False)
     

# Sentiment_analysis

comments = pd.read_csv('comments.csv')

# create preprocess_text function
def preprocess_text(text):

    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

comments['Comments'] = comments['Comments'].apply(preprocess_text)

analyzer = SentimentIntensityAnalyzer()

# create get_sentiment function

def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment

def overall_sentiment():
    comments['sentiment'] = comments['Comments'].apply(get_sentiment)

    # print(comments)

    comments.to_csv('sentiment_for_each_comment.csv', index=False)

    # Read and find the overall sentiment.

    df = pd.read_csv('sentiment_for_each_comment.csv')

    count_positive = df['sentiment'].value_counts().get(1)
    print(count_positive)

    count_negative = df['sentiment'].value_counts().get(0)
    print(count_negative)
    
    total_comments = count_positive + count_negative
    
    percentage_of_positive_comments = count_positive/total_comments * 100
    print(f"Percentage of positive comments",percentage_of_positive_comments,"%")
    
    percentage_of_negative_comments = count_negative/total_comments * 100
    print(f"Percentage of negative comments",percentage_of_negative_comments,"%")
    
    # most_common_words = df['Comments'].mode()
    
    # print(f"Most common words found",most_common_words)
            
overall_sentiment()


