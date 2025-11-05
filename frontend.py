import streamlit as st
from sentiment_analysis import read_comments

st.title("RM Analytics")
st.write("Find out the emotion behind a piece of text.")

# insta_link = st.text_input("Enter URL of Instagram Reel: ")

insta_comments_csv = st.file_uploader("Upload CSV file containing comments:", type="csv")

# This checks if a user has uploaded the csv file.
# Without it Streamlit will read the file and break immediately.

if insta_comments_csv is not None:
    # Pass the uploaded file to the backend function
    df = read_comments(insta_comments_csv)

    st.write(f"Total comments: {len(df)}")
    st.dataframe(df) 
