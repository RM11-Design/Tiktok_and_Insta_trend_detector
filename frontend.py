import streamlit as st
# Bring backend components to the frontend. NOT the other way around.
from sentiment_analysis import read_comments,preprocess_text,get_sentiment
# Run the following command in terminal: streamlit run frontend.py


st.title("RM Analytics")
st.write("Find out the emotion behind a piece of text.")

# insta_link = st.text_input("Enter URL of Instagram Reel: ")

insta_comments_csv = st.file_uploader("Upload CSV file containing comments:", type="csv")

# This checks if a user has uploaded the csv file.
# Without it, Streamlit will read the file and break immediately.

if insta_comments_csv is not None:
    # Pass the uploaded file to the backend function i.e "read_comments function"
    df = read_comments(insta_comments_csv)
    
    # This applys the preprocess_text function
    df["Processed comments"] = df["Comments"].apply(preprocess_text)

    # Displays the following on the web app
    st.write(f"Total comments: {len(df)}")
    st.dataframe(df["processed_comments"])

    