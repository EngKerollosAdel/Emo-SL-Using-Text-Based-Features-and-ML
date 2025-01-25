import tkinter as tk
from tkinter import scrolledtext
from EmojiCounter import count_emojis
from EmojiSentimentScoreCalculator import calculate_sentiment_scores
from SentimentFeatureExtractor import SentimentFeatureExtractor
from TextPreprocessor import TextPreprocessor
from Configuration import Configuration

class SentimentAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analysis for Arabic Tweets")

        # Set window to full screen (or dynamically fit it based on screen size)
        self.root.attributes('-fullscreen', True)

        # Make the window resizable
        self.root.resizable(True, True)

        # Create a frame to hold everything
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create grid configuration with 3 rows and 2 columns
        self.main_frame.grid_rowconfigure(0, weight=1, minsize=300)  # First part (output text)
        self.main_frame.grid_rowconfigure(1, weight=1)  # Second part (positive & negative emojis)
        self.main_frame.grid_rowconfigure(2, weight=1)  # Emoji sentiment scores
        self.main_frame.grid_columnconfigure(0, weight=1)  # First column for output text
        self.main_frame.grid_columnconfigure(1, weight=1)  # Second column for positive/negative emojis

        # First part: Adding a label and a scrolled text box for output (100% width, 50% height)
        self.label = tk.Label(self.main_frame, text="Sentiment Analysis Output", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')

        self.output_text = scrolledtext.ScrolledText(self.main_frame, width=80, height=10)
        self.output_text.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        # Second part: Adding two columns for positive and negative emojis (50% height)
        self.positive_label = tk.Label(self.main_frame, text="Positive Emojis", font=("Arial", 12))
        self.positive_label.grid(row=2, column=0, pady=10, sticky='ew')

        self.positive_emojis_text = tk.Text(self.main_frame, height=15, width=40)
        self.positive_emojis_text.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

        self.negative_label = tk.Label(self.main_frame, text="Negative Emojis", font=("Arial", 12))
        self.negative_label.grid(row=2, column=1, pady=10, sticky='ew')

        self.negative_emojis_text = tk.Text(self.main_frame, height=15, width=40)
        self.negative_emojis_text.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

        # Adding a label and Text widget for Emoji Sentiment Scores
        self.sentiment_label = tk.Label(self.main_frame, text="Emoji Sentiment Scores", font=("Arial", 12))
        self.sentiment_label.grid(row=4, column=0, columnspan=2, pady=10, sticky='ew')

        self.sentiment_scores_text = tk.Text(self.main_frame, height=15, width=80)
        self.sentiment_scores_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        # Adding a button to trigger analysis
        self.analyze_button = tk.Button(self.main_frame, text="Analyze Tweets", command=self.analyze_tweets, font=("Arial", 12))
        self.analyze_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Adding a close button to quit the app
        self.quit_button = tk.Button(self.main_frame, text="Close", command=self.close_app, font=("Arial", 12))
        self.quit_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def analyze_tweets(self):
        # Sample tweets 
        tweets = Configuration.fetch_tweets()
        extractor = SentimentFeatureExtractor()

        total_positive_emojis = {}
        total_negative_emojis = {}

        # Clear previous output
        self.output_text.delete(1.0, tk.END)
        self.positive_emojis_text.delete(1.0, tk.END)
        self.negative_emojis_text.delete(1.0, tk.END)
        self.sentiment_scores_text.delete(1.0, tk.END)

        # Process each tweet
        for tweet in tweets:
            # Algorithm 1 Enhanced Preprocess Arabic Tweets for Sentiment Analysis
            processed_text = TextPreprocessor.preprocess_text(tweet)

            # Display processed text in the scrolled text widget
            self.output_text.insert(tk.END, f"Processed Text: {processed_text}\n\n")

            # Extract features from the tweet using SentimentFeatureExtractor
            feature_vector = extractor.extract_features_from_tweet(processed_text)
            self.output_text.insert(tk.END, f"Feature Vector: {feature_vector.to_one_line()}\n\n")

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

        # Display the aggregated positive and negative emojis
        self.display_emoji_counts(total_positive_emojis, self.positive_emojis_text)
        self.display_emoji_counts(total_negative_emojis, self.negative_emojis_text)

        # Calculate sentiment scores
        emoji_sentiment_scores = calculate_sentiment_scores(total_positive_emojis, total_negative_emojis)

        # Display emoji sentiment scores
        self.display_sentiment_scores(emoji_sentiment_scores)

    def display_emoji_counts(self, emoji_counts, text_widget):
        """Helper function to display emoji counts in the provided text widget"""
        for emoji, count in emoji_counts.items():
            text_widget.insert(tk.END, f"{emoji}: {count}\n")

    def display_sentiment_scores(self, sentiment_scores):
        """Helper function to display sentiment scores for emojis in the sentiment_scores_text widget"""
        for emoji, score in sentiment_scores.items():
            self.sentiment_scores_text.insert(tk.END, f"{emoji}: {score:.2f}\n")

    def close_app(self):
        # Close the application
        self.root.quit()


# Main function to run the application
def main():
    # Create a Tkinter window
    root = tk.Tk()

    # Create an instance of the SentimentAnalysisApp
    app = SentimentAnalysisApp(root)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
