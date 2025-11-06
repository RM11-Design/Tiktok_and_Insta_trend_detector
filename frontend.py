import streamlit as st
# Bring backend components to the frontend. NOT the other way around.
from sentiment_analysis import read_comments,preprocess_text,get_sentiment,overall_sentiment
# Run the following command in terminal: streamlit run frontend.py


st.title("RM Analytics")
st.write("Find out the emotion behind a piece of text.")

# insta_link = st.text_input("Enter URL of Instagram Reel: ")

insta_comments_csv = st.file_uploader("Upload CSV file containing comments:", type="csv")

# This checks if a user has uploaded the csv file.
# Without it, Streamlit will read the file and break immediately.
if insta_comments_csv is not None:
    df = read_comments(insta_comments_csv)

    results = overall_sentiment(df)
    
    # This is where the results of the analysis are displayed. 
    # positive_count is the key that has the value from the analysis.
    st.write(f"Positive Comments: {results['positive_count']})")
    st.write(f"Negative Comments: {results['negative_count']}")
    st.write(f"Total Comments: {results['total']}")

    st.dataframe(results["df"][["Comments", "Processed", "sentiment"]])




    