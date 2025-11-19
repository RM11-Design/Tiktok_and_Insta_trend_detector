import sqlite3
import os
import pandas as pd


def csv_in_database(csv_folder_path,database_name):
    conn = sqlite3.connect(database_name)
    
    for filename in os.listdir(csv_folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(csv_folder_path, filename)
                table_name = os.path.splitext(filename)[0]  # Use filename (without extension) as table name

                try:
                    df = pd.read_csv(file_path)
                    df.to_sql(table_name, conn, if_exists='replace', index=False)
                    print(f"Successfully imported '{filename}' into table '{table_name}'")
                except Exception as e:
                    print(f"Error importing '{filename}': {e}")
                    
    conn.close()

csv_folder_path = 'C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\Tiktok_trend_detector\\all_csv_files'
database_name = 'all_csv_files.db'

csv_in_database(csv_folder_path, database_name)


                
            
                
   