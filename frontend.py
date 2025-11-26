import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import os
from wordcloud import WordCloud, STOPWORDS
from database import init_db, csv_in_database, get_all_links
# Bring backend components to the frontend. NOT the other way around.
from sentiment_analysis import read_comments,preprocess_text,get_sentiment,overall_sentiment
from creds import csv_folder_path


# Run the following command in terminal: streamlit run frontend.py

init_db()

st.set_page_config(
    page_title="RM Analytics",
    page_icon="bar_chart",
    layout="wide")

st.title("RM Analytics")
st.subheader("Find out the emotion behind what people think.")

# insta_link = st.text_input("Enter URL of Instagram Reel: ")

insta_comments_csv = st.file_uploader("Upload CSV file containing comments:", type="csv")

def analyse_and_visualise(df):
    results = overall_sentiment(df)

    wc = WordCloud(background_color="black").generate(' '.join(df["Comments"]))
    
    # total_comments = st.subheader(f"Total Comments: {results['total']}")
    
    st.dataframe(results["df"][["Comments", "sentiment"]])
    
    data_to_be_plotted = {
         "Sentiment": ["Positive", "Negative"],
        "Count": [results["positive_count"], results["negative_count"]]
    }
    
    chart_df = pd.DataFrame(data_to_be_plotted)
    
    # Plot the graph. .set_index enables one or more columns of a Dataframe as an index.   
    # Important when adding new indices to the data as it improves data retrieval 
    
    col1, col2, col3 = st.columns(3)
    
    # with col1:
    #     st.write(results["summary"])
                    
    with col2:
        # Comparing the number of positive and negative comments. 
        the_pie_chart = px.pie(chart_df,values="Count",names="Sentiment",title="Positive and Negative comments comparsion")
        st.plotly_chart(the_pie_chart)
        
    # Display the generated word cloud:
    fig, ax = plt.subplots()
    plt.axis("off")
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)  
    
# This checks if a user has uploaded the csv file.
# Without it, Streamlit will read the file and break immediately.
if insta_comments_csv is not None:
    df = read_comments(insta_comments_csv)  
    
    if st.button("Save"):
        # Safe way to create a full file path by combing folder and file name so that
        # the computer knows where to save the uploaded CSV file.
        save_path = os.path.join(csv_folder_path, insta_comments_csv.name)

        # Save the file to the folder
        df.to_csv(save_path, index=False)
        
        database_name = "all_csv_files.db"
        csv_in_database(csv_folder_path, database_name)
        
        st.success("Dashboard saved succesfully")
        
        
# 'links' is the list of CSV files in the database        
links = get_all_links()

st.subheader("Saved comments")

for file_id, file_name in links:
    # Creates a clickable button for each saved CSV.
    if st.button(file_name, key=f"{file_id}_{file_name}"): # ensures each button is unique
        csv_path = file_id
        csv_path = os.path.join(csv_folder_path, file_name)
        df = read_comments(csv_path)
        analyse_and_visualise(df)
        
              
    
    
            