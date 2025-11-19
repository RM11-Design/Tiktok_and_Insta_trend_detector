import streamlit as st
import pandas as pd
import os
from database import csv_in_database
# Bring backend components to the frontend. NOT the other way around.
from sentiment_analysis import read_comments,preprocess_text,get_sentiment,overall_sentiment
# Run the following command in terminal: streamlit run frontend.py

csv_folder_path = f"C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\Tiktok_trend_detector\\all_csv_files"

st.set_page_config(
    page_title="RM Analytics",
    page_icon="bar_chart",
    layout="wide")

st.title("RM Analytics")
st.subheader("Find out the emotion behind a piece of text.")

# insta_link = st.text_input("Enter URL of Instagram Reel: ")

insta_comments_csv = st.file_uploader("Upload CSV file containing comments:", type="csv")

# This checks if a user has uploaded the csv file.
# Without it, Streamlit will read the file and break immediately.
if insta_comments_csv is not None:
    df = read_comments(insta_comments_csv)

    results = overall_sentiment(df)
    
    # This is where the results of the analysis are displayed. 
    # positive_count is the key that has the value from the analysis.
    # st.write(f"Positive Comments: {results['positive_count']}")
    # st.write(f"Negative Comments: {results['negative_count']}")
    total_comments = st.write(f"Total Comments: {results['total']}")
    
    st.dataframe(results["df"][["Comments", "sentiment"]])
    
    chart_df = pd.DataFrame({
        "Sentiment": ["Positive", "Negative"],
        "Count": [results["positive_count"], results["negative_count"]]
    })
     
    # Plot the graph. .set_index enables one or more columns of a Dataframe as an index.   
    # Important when adding new indices to the data as it improves data retrieval 
    
    the_bar_chart = st.bar_chart(chart_df.set_index("Sentiment"),x_label="Type of comment",
                 y_label="Number of positive and negative comments",
                 horizontal=False)

    if st.button("Save"):
        save_path = os.path.join(csv_folder_path, insta_comments_csv.name)

        # Save the file to the folder
        df.to_csv(save_path, index=False)
        
        database_name = "all_csv_files.db"
        csv_in_database(csv_folder_path, database_name)
        
        st.success("Dashboard saved succesfully")
            

              
    
    
            