# Algorithm 4 Calculating Emoji Sentiment Scores
def calculate_sentiment_scores(positive_emojis, negative_emojis):
    """
    Calculates sentiment scores for emojis based on their positive and negative occurrences.

    :param positive_emojis: Dictionary of emoji counts in positive tweets
    :param negative_emojis: Dictionary of emoji counts in negative tweets
    :return: Dictionary of emoji sentiment scores
    """
    scores = {}
    # Get the union of all emojis from positive and negative counts
    all_emojis = set(positive_emojis.keys()).union(set(negative_emojis.keys()))

    for emoji in all_emojis:
        # Get the positive and negative counts for the emoji (default to 0 if not present)
        p = positive_emojis.get(emoji, 0)
        n = negative_emojis.get(emoji, 0)
        # Avoid division by zero
        if p + n > 0:
            scores[emoji] = (p - n) / (p + n)
        else:
            scores[emoji] = 0.0  # Neutral if no occurrences

    return scores


def main():
    # Example input data
    positive_emojis = {
        "😂": 10,  # "😂" appears 10 times in positive tweets
        "😊": 5,   # "😊" appears 5 times in positive tweets
        "😎": 2    # "😎" appears 2 times in positive tweets
    }

    negative_emojis = {
        "😂": 3,   # "😂" appears 3 times in negative tweets
        "😊": 2,   # "😊" appears 2 times in negative tweets
        "😢": 6    # "😢" appears 6 times in negative tweets
    }

    # Calculate sentiment scores
    emoji_sentiment_scores = calculate_sentiment_scores(positive_emojis, negative_emojis)

    # Print results
    print("Emoji Sentiment Scores (One-Line Format):")
    for emoji, score in emoji_sentiment_scores.items():
        print(f"{emoji}: {score:.2f}")

    print("\nEmoji Sentiment Scores (Detailed):")
    print(emoji_sentiment_scores)


# Run the main function
if __name__ == "__main__":
    main()
