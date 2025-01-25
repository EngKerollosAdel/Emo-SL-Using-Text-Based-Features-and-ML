# Algorithm 5 Emo-SL for Arabic Tweets Algorithm

import re
from collections import Counter

from Configuration import Configuration

class EmoSLArabicTweets:
    def __init__(self, positive_lexicon, negative_lexicon):
        """
        Initialize Emo-SL for Arabic Tweets with sentiment lexicons.

        :param positive_lexicon: List of positive words.
        :param negative_lexicon: List of negative words.
        """
        self.positive_lexicon = set(positive_lexicon)
        self.negative_lexicon = set(negative_lexicon)
        self.emoji_sentiment_lexicon = {}
        self.sentiment_results = {}

    def preprocess_data(self, tweets):
        """
        Preprocess tweets by removing non-Arabic characters and normalizing text.
        
        :param tweets: List of tweets to preprocess.
        :return: Preprocessed list of tweets.
        """
        processed_tweets = []
        for tweet in tweets:
            tweet = re.sub(r'[^\u0600-\u06FF\s]', '', tweet)  # Remove non-Arabic characters
            tweet = tweet.lower()  # Normalize text to lowercase
            processed_tweets.append(tweet)
        return processed_tweets

    def build_emo_sl(self, tweets, emojis):
        """
        Build the Emoji Sentiment Lexicon based on the emojis in the tweets.
        
        :param tweets: List of tweets.
        :param emojis: Set of distinct emojis extracted from the tweets.
        """
        emoji_counts = {emoji: {Configuration.Sentiment.positive: 0, Configuration.Sentiment.negative: 0} for emoji in emojis}

        # Count positive and negative emoji occurrences
        for tweet in tweets:
            sentiment = Configuration.Sentiment.positive if any(word in tweet for word in self.positive_lexicon) else Configuration.Sentiment.negative
            tweet_emojis = [char for char in tweet if char in emojis]
            for emoji in tweet_emojis:
                emoji_counts[emoji][sentiment] += 1

        # Calculate emoji sentiment scores
        for emoji, counts in emoji_counts.items():
            p = counts[Configuration.Sentiment.positive]
            n = counts[Configuration.Sentiment.negative]
            if p + n > 0:
                self.emoji_sentiment_lexicon[emoji] = p / (p + n)

    def extract_features(self, tweets, emojis):
        """
        Extract features from the tweets, including word counts and emoji sentiment scores.
        
        :param tweets: List of tweets.
        :param emojis: Set of distinct emojis extracted from the tweets.
        :return: List of feature vectors for each tweet.
        """
        features = []
        for tweet in tweets:
            # Feature 1: Emoji sentiment scores
            emoji_features = [self.emoji_sentiment_lexicon.get(emoji, 0) for emoji in emojis if emoji in tweet]

            # Feature 2: Count of positive and negative words
            positive_count = sum(1 for word in tweet.split() if word in self.positive_lexicon)
            negative_count = sum(1 for word in tweet.split() if word in self.negative_lexicon)

            # Normalize features
            total_words = len(tweet.split())
            normalized_positive = positive_count / total_words if total_words else 0
            normalized_negative = negative_count / total_words if total_words else 0

            # Combine all features
            features.append({
                'emoji_features': emoji_features,
                'positive_count': normalized_positive,
                'negative_count': normalized_negative
            })
        return features

    def classify_sentiments(self, tweets, features):
        """
        Classify sentiments using extracted features (Dummy ML classifier).
        
        :param tweets: List of tweets.
        :param features: List of feature vectors.
        :return: Sentiment classification for each tweet.
        """
        for tweet, feature_vector in zip(tweets, features):
            score = sum(feature_vector['emoji_features']) + feature_vector['positive_count'] - feature_vector['negative_count']
            sentiment = Configuration.Sentiment.positive if score > 0 else Configuration.Sentiment.negative if score < 0 else 'Neutral'
            self.sentiment_results[tweet] = sentiment
        return self.sentiment_results

    def apply_vader(self, tweet):
        """
        Apply VADER for sentiment analysis (mocked as we are working with Arabic).
        
        :param tweet: The tweet to analyze.
        :return: Sentiment score using VADER (mocked as random).
        """
        # In reality, you'd translate the tweet to English and use VADER
        sentiment_score = 0  # Placeholder
        return sentiment_score

    def analyze_tweets_with_vader(self, tweets):
        """
        Analyze tweets using VADER and calculate accuracy metrics (mocked as we lack actual sentiment data).
        
        :param tweets: List of tweets.
        :return: VADER sentiment scores for analysis.
        """
        vader_scores = {}
        for tweet in tweets:
            vader_scores[tweet] = self.apply_vader(tweet)
        return vader_scores

# Example usage:
def main():
    # Example lexicons
    positive_lexicon = Configuration.fetch_data_from_file(Configuration.FileName.positive_lexicon)
    negative_lexicon = Configuration.fetch_data_from_file(Configuration.FileName.negative_lexicon)
    
    # Example emojis
    emojis = set(Configuration.fetch_data_from_file(Configuration.FileName.emojis))
    
    # Example tweets
    tweets = [  # Example tweets
        "أنا سعيد 😊",
        "أنا حزين 😢",
        "أنا جيد 👍",
        "أنا سيء 😡"
    ]   
       
    
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

if __name__ == "__main__":
    main()
