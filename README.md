# 🎓 Emo-SL Using Text-Based Features and Machine Learning

This project aims to preprocess Arabic tweets for sentiment analysis using various text-based features and machine learning techniques.

─────────────────────────────────────────────────────────

## 📁 Project Structure  

Emo-SL-Using-Text-Based-Features-and-ML-master/
├── 📂 Data/
│   ├── 📄 sentiment_lexicon.xlsx       - Excel file containing sentiment lexicon
│   ├── 📄 stop_words.txt               - Text file containing stop words
│   ├── 📄 tweets.txt                   - Text file containing tweets data
│   ├── 📄 emojis.txt                   - Text file containing emojis data
│   ├── 📄 positive_lexicon.txt         - Text file containing positive lexicon
│   ├── 📄 negative_lexicon.txt         - Text file containing negative lexicon
│   └── 📄 additional_data.txt          - Placeholder for any additional data files
├── 📂 src/
│   ├── 🛠️ Configuration.py             - Configuration settings and utility functions
│   ├── 🛠️ Excel_Helper.py              - Helper functions for creating and managing Excel files
│   ├── 🛠️ main.py                      - Main script to run the project
│   ├── 🛠️ SentimentFeatureExtractor.py - Functions to extract sentiment features from text
│   ├── 🛠️ TextPreprocessor.py          - Functions to preprocess Arabic text
│   ├── 🛠️ TrainingSet.py               - Functions to manage training datasets
│   └── 🛠️ additional_module.py         - Placeholder for any additional source files
├── 📄 requirements.txt                 - List of required Python libraries
├── 📄 ReadMe.md                        - Project description and setup instructions
├── 🛡️ setup.bat                        - Batch script to automate setup (Windows)
└── 🛡️ setup.sh                         - Shell script to automate setup (macOS/Linux)


─────────────────────────────────────────────────────────

## 🛠️ Setup Instructions

### 📋 Prerequisites

🐍 Python 3.x: Download and install Python from the official website:
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)
✅ Ensure you select Add Python to PATH during installation.

─────────────────────────────────────────────────────────

### 📦 Install Required Libraries

#### ⚙️ Option 1: Using `requirements.txt`

1️⃣ Ensure the `requirements.txt` file contains the following content:

```
arabic-reshaper
python-bidi
pandas
openpyxl
emoji
joblib
```

2️⃣ Install the required libraries using:

```
pip install -r requirements.txt
```

#### ⚙️ Option 2: Install Libraries Individually

💡 If any installation fails, use the following commands:

```
pip install arabic-reshaper
pip install python-bidi
pip install pandas
pip install openpyxl
pip install emoji
pip install joblib
```

─────────────────────────────────────────────────────────

### ⚙️ Automate Setup

Automate the setup process using the provided scripts:

#### 🖥️ Windows

```
setup.bat
```

#### 🖥️ macOS/Linux

```
chmod +x setup.sh
./setup.sh
```

─────────────────────────────────────────────────────────

## 🚀 Usage

### 🔍 1. Navigate to the Project Directory

```
cd "D:/Other/Private/Master/Project/Emo-SL-Using-Text-Based-Features-and-ML-master/Emo-SL-Using-Text-Based-Features-and-ML-master"
```

### 🔧 2. Run the Main Script

```
python src/main.py
```

─────────────────────────────────────────────────────────

## 📚 Project Description

This project preprocesses Arabic tweets for sentiment analysis using various text-based features and machine learning techniques. The main steps include:

1️⃣ Preprocess the Tweets: Clean and normalize the Arabic text.
2️⃣ Build the Emoji Sentiment Lexicon: Create a lexicon of emojis with their associated sentiment scores.
3️⃣ Extract Features: Extract relevant features from the preprocessed tweets.
4️⃣ Classify Sentiments: Classify the sentiment of the tweets using the extracted features.
5️⃣ Apply VADER Analysis: (Mocked) Apply VADER sentiment analysis to the tweets.

─────────────────────────────────────────────────────────

## 🤝 Contributing

🙌 Contributions are welcome!
Feel free to submit a pull request or open an issue for suggestions or improvements.
