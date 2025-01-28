# Algorithm 3: Counting Emoji Occurrences (Fixed for Accurate Sentiment)
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
        self.sentiment = ""  # Will be determined dynamically

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
        self.SENTIMENT_LEXICON =  Configuration.fetch_setting(Configuration.SheetName.sentiment_lexicon)
        self.EMOJI_SENTIMENT_LEXICON =  Configuration.fetch_setting(Configuration.SheetName.emoji_sentiment_lexicon)

    def tokenize(self, text):
        """
        Tokenizes the input text into individual words for feature extraction.
        Uses a regex pattern to match word boundaries.
        """
        return re.findall(r'\b\w+\b', text)

    def extract_emojis(self, text):
        """
        Extracts emojis from the input text.
        Emojis are essential as they often carry sentiment information.
        """
        return [char for char in text if char in self.EMOJI_SENTIMENT_LEXICON]

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
        feature_vector.emojis = emojis  # Store the emojis
        for emoji in emojis:
            sentiment_score = self.EMOJI_SENTIMENT_LEXICON.get(emoji, 0)
            if sentiment_score > 0:
                feature_vector.positive_emojis_count += 1
                feature_vector.positive_score += sentiment_score
            else:
                feature_vector.negative_emojis_count += 1
                feature_vector.negative_score += sentiment_score

        # -------------------------
        # Determine sentiment
        # -------------------------
        if feature_vector.positive_score > feature_vector.negative_score:
            feature_vector.sentiment = Configuration.Sentiment.positive
        else:
            feature_vector.sentiment = Configuration.Sentiment.negative

        return feature_vector


# Algorithm 3: Counting Emoji Occurrences
def count_emojis(feature_vector, extractor):
    """
    Counts the occurrences of each emoji in the tweet, categorizing them as positive or negative
    based on sentiment scores obtained from the emoji sentiment lexicon.
    """
    # Dictionaries to store emoji counts for both positive and negative sentiments
    positive_emojis = {}
    negative_emojis = {}

    # Count emojis based on the sentiment
    for emoji in feature_vector.emojis:
        sentiment_score = extractor.EMOJI_SENTIMENT_LEXICON.get(emoji, 0)
        if sentiment_score > 0:
            if emoji in positive_emojis:
                positive_emojis[emoji] += 1
            else:
                positive_emojis[emoji] = 1
        elif sentiment_score < 0:
            if emoji in negative_emojis:
                negative_emojis[emoji] += 1
            else:
                negative_emojis[emoji] = 1

    return positive_emojis, negative_emojis


# Main function to demonstrate usage
def main():
    """
    Main function that demonstrates the usage of sentiment feature extraction and emoji counting.
    It processes each tweet, extracts sentiment features, counts emoji occurrences, and aggregates the counts.
    """
    tweets =  Configuration.fetch_tweets()  # Fetch a dataset of tweets
    
    extractor = SentimentFeatureExtractor()
    total_positive_emojis = {}
    total_negative_emojis = {}

    print("Processing each tweet...\n")
    for i, tweet_text in enumerate(tweets, 1):
        # Extract features from the tweet using SentimentFeatureExtractor
        feature_vector = extractor.extract_features_from_tweet(tweet_text)

        print(f"Tweet {i}: {tweet_text}")
        print("Extracted Features (Detailed Format):")
        print(feature_vector)  # Display the detailed feature vector
        print("-" * 50)

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

    # Display total counts
    print("\nFinal Aggregated Emoji Counts:")
    print(f"Total Positive Emojis Count: {total_positive_emojis}")
    print(f"Total Negative Emojis Count: {total_negative_emojis}")


if __name__ == "__main__":
    main()
