# Algorithm 2 Feature Extraction for Sentiment Analysis
import re
import json
from Configuration import Configuration

class FeatureVector:
    def __init__(self):
        """
        Initializes the feature vector to store counts and scores for sentiment analysis features.
        This includes positive/negative words, emojis, and their sentiment scores.
        """
        self.positive_words_count = 0
        self.negative_words_count = 0
        self.positive_emojis_count = 0
        self.negative_emojis_count = 0
        self.total_emojis_count = 0
        self.positive_score = 0.0
        self.negative_score = 0.0
        self.emojis = []  # Store emojis for further processing in Emoji Counter
        self.sentiment = ""  # Store sentiment for further processing

    def to_dict(self):
        """
        Convert the feature vector into a dictionary for easy representation.
        """
        return {
            "positive_words_count": self.positive_words_count,
            "negative_words_count": self.negative_words_count,
            "positive_emojis_count": self.positive_emojis_count,
            "negative_emojis_count": self.negative_emojis_count,
            "total_emojis_count": self.total_emojis_count,
            "positive_score": self.positive_score,
            "negative_score": self.negative_score,
            "emojis": self.emojis,
            "sentiment": self.sentiment
        }

    def __str__(self):
        """
        Return the feature vector in a detailed JSON-like format for display.
        """
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

    def to_one_line(self):
        """
        Return the feature vector in a compact JSON string for easier logging or display.
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)


class SentimentFeatureExtractor:
    def __init__(self):
        """
        Initializes the sentiment and emoji lexicons from the configuration.
        These lexicons provide sentiment scores for words and emojis.
        """
        self.SENTIMENT_LEXICON = Configuration.fetch_setting(Configuration.SheetName.sentiment_lexicon)
        self.EMOJI_SENTIMENT_LEXICON = Configuration.fetch_setting(Configuration.SheetName.emoji_sentiment_lexicon)

        self.all_emojis = Configuration.fetch_data_from_file(Configuration.FileName.emojis)


    def tokenize(self, text):
        """
        Tokenizes the input text into individual words for feature extraction.
        Uses a regex pattern to match word boundaries.
        """
        return re.findall(r'\b\w+\b', text)

    def extract_emojis(self, text):
        """
        Extracts emojis from the input text by checking if they are in the predefined emoji list.
        """
        return [char for char in text if char in self.all_emojis]


    def extract_features_from_tweet(self, tweet):
        """
        Extracts sentiment features from a single tweet, including both text-based and emoji-based features.
        """
        feature_vector = FeatureVector()

        # -------------------------
        # Extract text-based features
        # -------------------------
        words = self.tokenize(tweet)
        for word in words:
            # Check if the word exists in the Sentiment Lexicon
            if word in self.SENTIMENT_LEXICON:
                sentiment_score = self.SENTIMENT_LEXICON[word]
                if sentiment_score > 0:
                    feature_vector.positive_words_count += 1
                    feature_vector.positive_score += sentiment_score
                else:
                    feature_vector.negative_words_count += 1
                    feature_vector.negative_score += sentiment_score

        # -------------------------
        # Extract emoji-based features
        # -------------------------
        emojis = self.extract_emojis(tweet)
        feature_vector.total_emojis_count = len(emojis)
        feature_vector.emojis = emojis  # Store the emojis for further processing
        for emoji in emojis:
            if emoji in self.EMOJI_SENTIMENT_LEXICON:
                sentiment_score = self.EMOJI_SENTIMENT_LEXICON[emoji]
                if sentiment_score > 0:
                    feature_vector.positive_emojis_count += 1
                    feature_vector.positive_score += sentiment_score
                else:
                    feature_vector.negative_emojis_count += 1
                    feature_vector.negative_score += sentiment_score
        
        # Determine sentiment from word and emoji analysis (for simplicity, compare positive and negative scores)
        if feature_vector.positive_score > feature_vector.negative_score:
            feature_vector.sentiment = Configuration.Sentiment.positive
        else:
            feature_vector.sentiment = Configuration.Sentiment.negative

        return feature_vector


# Main function to run the example
def main():
    tweets = Configuration.fetch_tweets()  # Fetch a dataset of tweets from the configuration
    
    extractor = SentimentFeatureExtractor()

    print("Processing each tweet...\n")
    for i, tweet_text in enumerate(tweets, 1):
        # Extract features from the tweet using SentimentFeatureExtractor
        feature_vector = extractor.extract_features_from_tweet(tweet_text)
        
        print(f"Tweet {i}: {tweet_text}")
        print("Extracted Features (Detailed Format):")
        print(feature_vector)  # Display the detailed feature vector
        print("-" * 50)

        # print("Extracted Features (One-Line Format):")
        # print(feature_vector.to_one_line())  # Display the one-line feature vector
        # print("-" * 50)


if __name__ == "__main__":
    main()
