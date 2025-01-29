from Configuration import Configuration
from EmoSLArabicTweets import EmoSLArabicTweets
from EmojiCounter import count_emojis
from EmojiSentimentScoreCalculator import calculate_sentiment_scores
from Excel_Helper import ExcelHelper
from SentimentFeatureExtractor import SentimentFeatureExtractor
from TextPreprocessor import TextPreprocessor


def main():
    # Create an instance of the ExcelHelper class
    excel_helper = ExcelHelper()

    # Sample tweets 
    tweets = Configuration.fetch_tweets()
    extractor = SentimentFeatureExtractor()

    total_positive_emojis = {}
    total_negative_emojis = {}
   # Process each tweet
    for tweet in tweets:
        # Algorithm 1 Enhanced Preprocess Arabic Tweets for Sentiment Analysis
        processed_text = TextPreprocessor.preprocess_text(tweet)
  
        # Extract features from the tweet using SentimentFeatureExtractor
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
    
        # Append new data
        excel_helper.append_data([tweet, 
                                  processed_text, 
                                  feature_vector.positive_words_count, 
                                  feature_vector.negative_words_count,
                                  feature_vector.positive_emojis_count,
                                  feature_vector.negative_emojis_count,
                                  feature_vector.total_emojis_count,
                                  feature_vector.positive_score,
                                  feature_vector.negative_score,
                                  feature_vector.emojis,
                                  feature_vector.sentiment,
                                  positive_emojis,
                                  negative_emojis ])

    # Print all total_positive_emojis 
    for emoji, count in total_positive_emojis.items():
        excel_helper.append_positive_emojis(emoji, count)

    # Print all total_negative_emojis
    for emoji, count in total_negative_emojis.items():
        excel_helper.append_negative_emojis(emoji, count)



    # Algorithm 4 Calculating Emoji Sentiment Scores
    # Calculate sentiment scores
    emoji_sentiment_scores = calculate_sentiment_scores(total_positive_emojis, total_negative_emojis)

    # Print results 
    for emoji, score in emoji_sentiment_scores.items():
        excel_helper.append_emoji_sentiment_score(emoji, score)
   


    # Example lexicons
    positive_lexicon = Configuration.fetch_data_from_file(Configuration.FileName.positive_lexicon)
    negative_lexicon = Configuration.fetch_data_from_file(Configuration.FileName.negative_lexicon)
    
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
     
    # Print all Sentiment Classification Results
    for word, sentiment in sentiment_results.items():
        excel_helper.append_sentiment_classification_result(word, sentiment)

    
    # Print all VADER Sentiment Scores
    for word, score in vader_scores.items():
        excel_helper.append_vader_sentiment_score(word, score)   

    # Create the Excel file
    excel_helper.create_excel()

if __name__ == "__main__":
    main()
