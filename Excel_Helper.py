import pandas as pd
from datetime import datetime
import os

class ExcelHelper:
    def __init__(self):
        # Define column names and initial fixed data
        self.columns = ['Tweets', 'processed_text', 'positive_words_count', 'negative_words_count',
                        'positive_emojis_count', 'negative_emojis_count', 'total_emojis_count', 'positive_score', 
                        'negative_score', 'emojis', 'sentiment', 'positive_emojis', 'negative_emojis']
        self.fixed_data = []
        
        # Emoji data
        self.total_positive_emojis = []  # Each entry: [emoji, count]
        self.total_negative_emojis = []  # Each entry: [emoji, count]
        self.emoji_sentiment_scores = []  # Each entry: [emoji, score]
        self.sentiment_classification_results = []  # Each entry: [word, sentiment]
        self.vader_sentiment_scores = []  # Each entry: [word, score]

    def create_excel(self):
        # Create an empty DataFrame with the specified columns
        df = pd.DataFrame(columns=self.columns)

        # Loop to append fixed data rows to the DataFrame
        for row in self.fixed_data:
            new_row = pd.DataFrame([row], columns=self.columns)
            df = pd.concat([df, new_row], ignore_index=True)

        # Create DataFrames for all sheets
        df_positive = pd.DataFrame(self.total_positive_emojis, columns=['Emoji', 'Count'])
        df_negative = pd.DataFrame(self.total_negative_emojis, columns=['Emoji', 'Count'])
        df_sentiment_scores = pd.DataFrame(self.emoji_sentiment_scores, columns=['Emoji', 'Score'])
        df_sentiment_classification_results = pd.DataFrame(self.sentiment_classification_results, columns=['Word', 'Sentiment'])
        df_vader_sentiment_scores = pd.DataFrame(self.vader_sentiment_scores, columns=['Word', 'Score'])

        # Get the current time and format the filename
        current_time = datetime.now()
        file_name = f"report_{current_time.year}_{current_time.month}_{current_time.day}_{current_time.hour}_{current_time.minute}_{current_time.second}.xlsx"
        
        # Ensure the output folder exists
        output_folder = 'output'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Define the full file path
        file_path = os.path.join(output_folder, file_name)

        # Write the DataFrames to an Excel file with multiple sheets
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='report')
            df_positive.to_excel(writer, index=False, sheet_name='total_positive_emojis')
            df_negative.to_excel(writer, index=False, sheet_name='total_negative_emojis')
            df_sentiment_scores.to_excel(writer, index=False, sheet_name='emoji_sentiment_scores')
            df_sentiment_classification_results.to_excel(writer, index=False, sheet_name='Classification_Results')
            df_vader_sentiment_scores.to_excel(writer, index=False, sheet_name='VADER Sentiment Scores')

        print(f"Excel file '{file_name}' has been created and saved in the '{output_folder}' folder.")

    def append_data(self, new_data):
        # Append new data to the fixed_data list
        self.fixed_data.append(new_data)

    def append_positive_emojis(self, emoji, count):
        # Append data for positive emojis
        self.total_positive_emojis.append([emoji, count])

    def append_negative_emojis(self, emoji, count):
        # Append data for negative emojis
        self.total_negative_emojis.append([emoji, count])

    def append_emoji_sentiment_score(self, emoji, score):
        # Append data for emoji sentiment scores
        self.emoji_sentiment_scores.append([emoji, score])

    def append_sentiment_classification_result(self, word, sentiment):
        # Append data to the sentiment classification results
        self.sentiment_classification_results.append([word, sentiment])

    def append_vader_sentiment_score(self, word, score):
        # Append data to the VADER sentiment scores
        self.vader_sentiment_scores.append([word, score])

def main():
    # Create an instance of the ExcelHelper class
    excel_helper = ExcelHelper()

    # Append new data for the main sheet
    excel_helper.append_data(['Tweet1', 'processed_tweet1', 2, 1, 5, 2, 7, 0.8, 0.2, '😊👍', 'positive', '😊', ''])
    excel_helper.append_data(['Tweet2', 'processed_tweet2', 1, 3, 4, 6, 10, 0.5, 0.7, '😢😡', 'negative', '', '😡'])

    # Append data for the positive and negative emoji sheets
    excel_helper.append_positive_emojis('😊', 5)  # 5 positive emojis for '😊'
    excel_helper.append_positive_emojis('👍', 3)  # 3 positive emojis for '👍'
    excel_helper.append_negative_emojis('😢', 2)  # 2 negative emojis for '😢'
    excel_helper.append_negative_emojis('😡', 4)  # 4 negative emojis for '😡'

    # Append data for the emoji sentiment scores
    excel_helper.append_emoji_sentiment_score('😊', 0.9)  # Positive sentiment score for '😊'
    excel_helper.append_emoji_sentiment_score('😢', -0.8)  # Negative sentiment score for '😢'

    # Append data for sentiment classification results
    excel_helper.append_sentiment_classification_result('happy', 'positive')
    excel_helper.append_sentiment_classification_result('sad', 'negative')
    excel_helper.append_sentiment_classification_result('angry', 'negative')

    # Append data for VADER sentiment scores
    excel_helper.append_vader_sentiment_score('love', 0.95)
    excel_helper.append_vader_sentiment_score('hate', -0.85)
    excel_helper.append_vader_sentiment_score('neutral', 0.0)

    # Create the Excel file with multiple sheets
    excel_helper.create_excel()

if __name__ == "__main__":
    main()
