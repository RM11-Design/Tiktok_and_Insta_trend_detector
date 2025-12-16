# Tiktok_and_Instagram_analysis

User uploads a CSV file containing comments from an Instagram post.

It then opens the CSV file where the comments are located and starts the following:
Tokenize: Breaks down the text into indivdual words or "tokens".
Removes stop words i.e. "and", "the", "of" etc...
Lemmatization: reduce words to their root form.

Each comment is given a score where "1" means positive sentiment and "0" meaning a negative sentiment.

--------------------------------------------------------------------------------------------

# To set up a virtual environment:
python -m venv venv

To activate virtual environemnt:
.\venv\Scripts\activate

# How to install libraries:

pip install -r requirements.txt

# To install NLTK attributes:

nltk.download('all')

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Change file path

Go to creds.py file.
Write click on the "sample_comments" directory, select copy path.
Paste the path in the "csv_folder_path" variable.
Click Save.
Sometimes, you made need to add double backslashes due to unicode error. So add another backslash to each backslash that is currently in the file path.

# Run the following command in terminal: streamlit run frontend.py

On the web app, click on the "browse files" button.
It will the prompt you to upload a CSV file containing comments.
Go to the "sample comments" folder and click on a CSV file to be analysed.
Once uploaded, the web app will preform the analysis.
At the bottom, click the "Save" button. This will store the CSV file in the database.