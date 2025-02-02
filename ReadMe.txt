# Emo-SL-Using-Text-Based-Features-and-ML

This project aims to preprocess Arabic tweets for sentiment analysis using various text-based features and machine learning techniques.

## Project Structure

```
Emo-SL-Using-Text-Based-Features-and-ML-master/
│
├── Data/
│   ├── sentiment_lexicon.xlsx       # Excel file containing sentiment lexicon
│   ├── stop_words.txt               # Text file containing stop words
│   ├── tweets.txt                   # Text file containing tweets data
│   ├── emojis.txt                   # Text file containing emojis data
│   ├── positive_lexicon.txt         # Text file containing positive lexicon
│   ├── negative_lexicon.txt         # Text file containing negative lexicon
│   └── additional_data.txt          # Placeholder for any additional data files
│
├── src/
│   ├── Configuration.py             # Configuration settings and utility functions
│   ├── Excel_Helper.py              # Helper functions for creating and managing Excel files
│   ├── main.py                      # Main script to run the project
│   ├── SentimentFeatureExtractor.py # Functions to extract sentiment features from text
│   ├── TextPreprocessor.py          # Functions to preprocess Arabic text
│   ├── TrainingSet.py               # Functions to manage training datasets
│   └── additional_module.py         # Placeholder for any additional source files
│
├── requirements.txt                 # List of required Python libraries
├── ReadMe.md                        # Project description and setup instructions
├── setup.bat                        # Batch script to automate setup (Windows)
└── setup.sh                         # Shell script to automate setup (macOS/Linux)
```

## Setup Instructions

### Prerequisites

- Python 3.x: Download and install Python from the official website: [python.org](https://www.python.org/downloads/)
  - Make sure to check the option to add Python to your PATH during installation.

### Install Required Libraries

1. **Using `requirements.txt`**:
   - Create a `requirements.txt` file with the following content:
     ```plaintext
     arabic-reshaper
     python-bidi
     pandas
     openpyxl
     emoji
     joblib
     ```
   - Install the required libraries using `pip`:
     ```sh
     pip install -r requirements.txt
     ```

2. **Install Additional Libraries Individually (if needed)**:
   - If you need to install libraries individually, use the following commands:
     ```sh
     pip install arabic-reshaper
     pip install python-bidi
     pip install pandas
     pip install openpyxl
     pip install emoji
     pip install joblib
     ```

### Automate Setup

You can automate the setup process using the provided scripts:

1. **Windows**:
   - Run the `setup.bat` script:
     ```sh
     setup.bat
     ```

2. **macOS/Linux**:
   - Make the `setup.sh` script executable and run it:
     ```sh
     chmod +x setup.sh
     ./setup.sh
     ```

## Usage

1. **Navigate to the Project Directory**:
   ```sh
   cd "D:/Other/Private/Master/Project/Emo-SL-Using-Text-Based-Features-and-ML-master/Emo-SL-Using-Text-Based-Features-and-ML-master"
   ```

2. **Run the Main Script**:
   ```sh
   python src/main.py
   ```

## Project Description

This project preprocesses Arabic tweets for sentiment analysis using various text-based features and machine learning techniques. The main steps include:

1. **Preprocess the Tweets**: Clean and normalize the Arabic text.
2. **Build the Emoji Sentiment Lexicon**: Create a lexicon of emojis with their associated sentiment scores.
3. **Extract Features**: Extract relevant features from the preprocessed tweets.
4. **Classify Sentiments**: Classify the sentiment of the tweets using the extracted features.
5. **Apply VADER Analysis**: (Mocked) Apply VADER sentiment analysis to the tweets.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
