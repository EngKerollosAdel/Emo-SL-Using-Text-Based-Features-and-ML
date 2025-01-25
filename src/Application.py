import tkinter as tk
from tkinter import ttk, messagebox
import time  # For measuring execution time
from datetime import datetime  # For capturing start and end date-time
from EmojiSentimentScoreCalculator import calculate_sentiment_scores
from TextPreprocessor import TextPreprocessor
from SentimentFeatureExtractor import SentimentFeatureExtractor
from EmojiCounter import count_emojis
from EmoSLArabicTweets import EmoSLArabicTweets
from Configuration import Configuration 


# Example sentiment lexicons
SENTIMENT_LEXICON =  Configuration.fetch_setting(Configuration.SheetName.sentiment_lexicon)
EMOJI_SENTIMENT_LEXICON =  Configuration.fetch_setting(Configuration.SheetName.emoji_sentiment_lexicon)

 
# Create the main window
class EmoSLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emo-SL Framework: Emoji Sentiment Lexicon")
        self.root.geometry("1000x600")  # Set window size
        self.root.resizable(True, True)  # Allow resizing of the window
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="Emo-SL Framework: Emoji Sentiment Lexicon Using Text-Based Features and Machine Learning for Sentiment Analysis", 
                               font=("Helvetica", 16), wraplength=980, justify="center")
        title_label.pack(pady=20)

        # Fetch the tweets from the DataSet
        self.tweets = Configuration.fetch_tweets()

        # Create buttons to load and clear content
        load_button = tk.Button(self.root, text="Load Tweets", command=self.confirm_load_tweets, font=("Helvetica", 14))
        load_button.pack(pady=10)

        clear_button = tk.Button(self.root, text="Clear Content", command=self.confirm_clear_content, font=("Helvetica", 14))
        clear_button.pack(pady=10)

        # Label to show status and execution time
        self.status_label = tk.Label(self.root, text="Action: Idle, Start Time: N/A, End Time: N/A, Time: 0.00 seconds", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Display the tweets in a table (initially empty)
        self.create_tweet_table()

    def create_tweet_table(self):
        # Create a frame for the Treeview widget
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, pady=20)

        # Create a Treeview widget for the tweet table with 7 columns (including the new row number column)
        columns = ("Row", "Tweet", "Algorithm 1 Output", "Algorithm 2 Output", "Algorithm 3 Output", "Algorithm 4 Output", "Algorithm 5 Output")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=20)  # Increase height for more rows

        # Define the columns for the Treeview
        self.tree.heading("Row", text="Row")
        self.tree.heading("Tweet", text="Tweet")
        self.tree.heading("Algorithm 1 Output", text="Algorithm 1 Enhanced Preprocess Arabic Tweets for Sentiment Analysis")
        self.tree.heading("Algorithm 2 Output", text="Algorithm 2 Feature Extraction for Sentiment Analysis")
        self.tree.heading("Algorithm 3 Output", text="Algorithm 3 Counting Emoji Occurrences")
        self.tree.heading("Algorithm 4 Output", text="Algorithm 4 Calculating Emoji Sentiment Scores")
        self.tree.heading("Algorithm 5 Output", text="Algorithm 5 Emo-SL for Arabic Tweets Algorithm")

        # Set the width for each column
        for col in columns:
            self.tree.column(col, width=200, anchor="center", stretch=tk.YES)

        # Enable multiline wrapping for "Tweet" column
        self.tree.tag_configure("multiline", font=("Helvetica", 12), anchor="w")

        # Create scrollbars
        v_scroll = tk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        h_scroll = tk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        # Place the scrollbars
        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")

        # Place the Treeview in the frame
        self.tree.pack(fill="both", expand=True)

    def confirm_load_tweets(self):
        # Ask for confirmation before loading tweets
        confirm = messagebox.askyesno("Confirm Load", "Are you sure you want to load the tweets?")
        if confirm:
            self.load_tweets()

    def load_tweets(self):
        # Capture start time and update the label
        start_time = time.time()
        start_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status_label.config(text=f"Action: Loading Tweets, Start Time: {start_datetime}, Time: 0.00 seconds")

        # Clear the existing content in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        extractor = SentimentFeatureExtractor()
        total_positive_emojis = {}
        total_negative_emojis = {}

        # Add tweets and their corresponding algorithm outputs to the table
        for i, tweet in enumerate(self.tweets): 
            algorithm_1_output = self.analyze_sentiment(tweet)  # Placeholder for Algorithm 1 output
            algorithm_2_output = self.analyze_sentiment(tweet)  # Placeholder for Algorithm 2 output
            algorithm_3_output = self.analyze_sentiment(tweet)  # Placeholder for Algorithm 3 output
            algorithm_4_output = self.analyze_sentiment(tweet)  # Placeholder for Algorithm 4 output
            algorithm_5_output = self.analyze_sentiment(tweet)  # Placeholder for Algorithm 5 output

            # Preprocess the tweet text
            # Algorithm 1 Enhanced Preprocess Arabic Tweets for Sentiment Analysis
            processed_text = TextPreprocessor.preprocess_text(tweet)

            # Algorithm 2 Feature Extraction for Sentiment Analysis 
            feature_vector = extractor.extract_features_from_tweet(processed_text)
            
            # Algorithm 3 Counting Emoji Occurrences
            # Use the output from Feature Extraction (Algorithm 2) for Emoji Counting (Algorithm 3)
            positive_emojis, negative_emojis = count_emojis(feature_vector, extractor)

            # Aggregate positive emojis
            for emoji, count in positive_emojis.items():
                if emoji in total_positive_emojis:
                    total_positive_emojis[emoji] += count
                else:
                    total_positive_emojis[emoji] = count

            # Aggregate negative emojis
            for emoji, count in negative_emojis.items():
                if emoji in total_negative_emojis:
                    total_negative_emojis[emoji] += count
                else:
                    total_negative_emojis[emoji] = count



            # Algorithm 4 Calculating Emoji Sentiment Scores
            # Calculate sentiment scores
            emoji_sentiment_scores = calculate_sentiment_scores(total_positive_emojis, total_negative_emojis)

            # Print results
            print("Emoji Sentiment Scores (One-Line Format):")
            for emoji, score in emoji_sentiment_scores.items():
                print(f"{emoji}: {score:.2f}")

            print("\nEmoji Sentiment Scores (Detailed):")
            print(emoji_sentiment_scores)



            # Algorithm 5 Emo-SL for Arabic Tweets Algorithm
            # Example lexicons
            # Example lexicons
            positive_lexicon = Configuration.fetch_data_from_file(Configuration.FileName.positive_lexicon)
            negative_lexicon = Configuration.fetch_data_from_file(Configuration.FileName.negative_lexicon)
            
            # Example tweets
            tweets = Configuration.fetch_tweets()
            
            # Example emojis
            emojis = set(Configuration.fetch_data_from_file(Configuration.FileName.emojis))
            
            # Instantiate EmoSL for Arabic Sentiment Analysis
            emosl = EmoSLArabicTweets(positive_lexicon, negative_lexicon)

            # Step 1: Preprocess the tweets
            preprocessed_tweets = emosl.preprocess_data(tweets)
            
            # Step 2: Build the Emoji Sentiment Lexicon
            emosl.build_emo_sl(preprocessed_tweets, emojis)
            
            # Step 3: Extract features
            features = emosl.extract_features(preprocessed_tweets, emojis)
            
            # Step 4: Classify sentiments
            sentiment_results = emosl.classify_sentiments(preprocessed_tweets, features)
            
            # Step 5: Apply VADER analysis (mocked)
            vader_scores = emosl.analyze_tweets_with_vader(preprocessed_tweets)
            
            # Print results
            print("Sentiment Classification Results:", sentiment_results)
            print("VADER Sentiment Scores (mocked):", vader_scores)



            # Insert tweet and its outputs as multiline text in the table
            self.tree.insert("", "end", values=(i+1, tweet, 
                                                processed_text, 
                                                feature_vector.to_one_line(), 
                                                f"Positive Emojis Count: {positive_emojis}, Negative Emojis Count: {negative_emojis}"
                                                , algorithm_4_output, algorithm_5_output), tags=("multiline",))





        # Display total counts
        print("\nFinal Aggregated Emoji Counts:")
        print(f"Total Positive Emojis Count: {total_positive_emojis}")
        print(f"Total Negative Emojis Count: {total_negative_emojis}")
        
        # Calculate sentiment scores
        emoji_sentiment_scores = calculate_sentiment_scores(positive_emojis, negative_emojis)

        # Print results
        print("Emoji Sentiment Scores (One-Line Format):")
        for emoji, score in emoji_sentiment_scores.items():
            print(f"{emoji}: {score:.2f}")

        print("\nEmoji Sentiment Scores (Detailed):")
        print(emoji_sentiment_scores)

        # Capture end time and calculate execution time
        end_time = time.time()
        end_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_time = round(end_time - start_time, 2)
        self.status_label.config(text=f"Action: Loaded Tweets, Start Time: {start_datetime}, End Time: {end_datetime}, Time: {execution_time} seconds")

    def confirm_clear_content(self):
        # Ask for confirmation before clearing the table
        confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear the content?")
        if confirm:
            self.clear_content()

    def clear_content(self):
        # Capture start time and update the label
        start_time = time.time()
        start_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status_label.config(text=f"Action: Clearing Content, Start Time: {start_datetime}, Time: 0.00 seconds")

        # Clear the content in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Capture end time and calculate execution time
        end_time = time.time()
        end_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_time = round(end_time - start_time, 2)
        self.status_label.config(text=f"Action: Cleared Content, Start Time: {start_datetime}, End Time: {end_datetime}, Time: {execution_time} seconds")

    def analyze_sentiment(self, tweet):
        # Placeholder sentiment analysis logic (Algorithm 1)
        sentiment = "Positive" if "سعيد" in tweet or "رائع" in tweet else "Negative"
        return sentiment


# Run the application
def main():
    root = tk.Tk()
    app = EmoSLApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
