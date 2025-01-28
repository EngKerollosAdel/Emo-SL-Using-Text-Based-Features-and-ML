import csv
import openpyxl

import Configuration

class DataSet:
    @staticmethod
    def fetch_tweets():
        tweets =  Configuration.fetch_tweets()
    

    @staticmethod
    def fetch_setting(sheet_name):
        """
        Fetch the sentiment lexicon from an Excel file.
        
        :param file_name: Path to the Excel file.
        :param sheet_name: Name of the sheet to read from (defaults to the first sheet if None).
        :return: A dictionary where keys are words and values are their sentiment scores.
        """

        file_name = 'Data/sentiment_lexicon.xlsx'

        setting = {}

        try:
            # Load the workbook
            workbook = openpyxl.load_workbook(file_name)
            
            # Select the specified sheet or the first sheet
            sheet = workbook[sheet_name] if sheet_name else workbook.active
            
            # Iterate through the rows (assuming the first row contains headers)
            for row in sheet.iter_rows(min_row=2, values_only=True):
                key, value = row
                if key and value is not None:
                    setting[key.strip()] = float(value)
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        except KeyError:
            print(f"The sheet '{sheet_name}' does not exist in the workbook.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return setting


    @staticmethod
    def fetch_stop_words(file_name='Data/stop_words.txt'):
        tweets = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    tweet = line.strip()
                    if tweet:
                        tweets.append(tweet)
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        return tweets
    
    
 