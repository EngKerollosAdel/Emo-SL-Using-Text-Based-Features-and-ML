# Algorithm 1: Enhanced Preprocess Arabic Tweets for Sentiment Analysis
# This algorithm aims to clean and preprocess Arabic text for sentiment analysis. 
# It incorporates several text normalization and filtering steps based on linguistic properties specific to Arabic.
import re
import arabic_reshaper
from bidi.algorithm import get_display

from Configuration import Configuration 

class TextPreprocessor:
    @staticmethod
    def normalize_arabic_text(text):
        """
        Normalize Arabic text to standard form.
        Replace variations of Arabic letters with their standard forms.
        For example:
        - 'إ', 'أ', 'آ' are normalized to 'ا'
        - 'ة' is normalized to 'ه'
        - 'ى' is normalized to 'ي'
        This step reduces variations in text forms and helps achieve more accurate sentiment classification.
        """
        normalization_patterns =  Configuration.fetch_setting_pattern('normalization_patterns')
        # Apply each normalization pattern to the text
        for pattern, replacement in normalization_patterns.items():
            text = text.replace(pattern, replacement)
        return text
 
    @staticmethod
    def remove_non_arabic_chars(text):
        """
        Remove all English characters from the text, but keep Arabic letters, digits, spaces, basic punctuation, and emojis.
        Keeping only Arabic characters focuses the sentiment analysis on the relevant language and avoids noise.
        """
        # Remove all English characters (both uppercase and lowercase)
        return re.sub(r'[a-zA-Z]', '', text)

    @staticmethod
    def remove_numbers(text):
        """
        Remove numeric characters (both Arabic and Western digits) from the text.
        This ensures that numbers (e.g., 123 or ١٢٣) are excluded, as they are not relevant for sentiment analysis.
        """
        # Remove both Arabic and Western numerals
        return re.sub(r'[\d٠-٩۰-۹]+', '', text)

    @staticmethod
    def remove_special_chars(text):
        """
        Remove special characters (e.g., punctuation) from the text.
        This step ensures that only Arabic letters, spaces, and relevant punctuation remain,
        while preserving emojis and underscores, by filtering out unwanted characters from an array.
        Emojis are retained since they can carry sentiment information.
        """
        # Define the allowed characters as an array
        allowed_chars = (
            set('0123456789') |  # Arabic/Western digits
            set('ء-ي') |  # Arabic letters
            set('،؛؟') |  # Relevant Arabic punctuation marks
            set('ًٌٍَُِّْْ') |  # Arabic diacritics (fatha, kasra, damma, etc.)
            set(chr(i) for i in range(0x0600, 0x06FF + 1)) |  # Arabic block (more characters)
            set(chr(i) for i in range(0x0750, 0x077F + 1)) |  # Arabic Supplement block (additional Arabic characters)
            set(chr(i) for i in range(0x08A0, 0x08FF + 1)) |  # Arabic Extended-A block
            set(chr(i) for i in range(0x1F600, 0x1F64F + 1)) |  # Emoji range (smiling faces)
            set(chr(i) for i in range(0x1F300, 0x1F5FF + 1)) |  # Emoji range (symbols and pictographs)
            set(chr(i) for i in range(0x1F680, 0x1F6FF + 1)) |  # Emoji range (transportation and map symbols)
            set(chr(i) for i in range(0x1F700, 0x1F77F + 1)) |  # Emoji range (alchemical symbols)
            set(chr(i) for i in range(0x1F780, 0x1F7FF + 1)) |  # Emoji range (geometric shapes)
            set(chr(i) for i in range(0x1F800, 0x1F8FF + 1)) |  # Emoji range (Supplemental Arrows-C)
            set(chr(i) for i in range(0x1F900, 0x1F9FF + 1)) |  # Emoji range (Supplemental Symbols and Pictographs)
            set(chr(i) for i in range(0x1FA00, 0x1FA6F + 1)) |  # Emoji range (symbols and pictographs)
            set(chr(i) for i in range(0x1FA70, 0x1FAFF + 1)) |  # Emoji range (symbols)
            set(chr(i) for i in range(0x2600, 0x26FF + 1)) |  # Emoji range (Miscellaneous symbols)
            set(chr(i) for i in range(0x2700, 0x27BF + 1)) |  # Emoji range (Dingbats)
            set(' ') |  # Space character
            set('_')  # Underscore
        )

        # Filter out characters that are not in the allowed set
        return ''.join([char for char in text if char in allowed_chars])

    @staticmethod
    def remove_diacritics(text):
        """
        Remove diacritics (tashkeel) from the text.
        Diacritics include symbols such as fathah, kasrah, dammah, etc. (unicode range: \u064B-\u0652).
        Example: "أحبُّ" becomes "احب".
        Removing diacritics standardizes the text, reducing variations in word forms.
        """
        return re.sub(r'[\u064B-\u0652\u0670]', '', text)  # Optionally add any additional diacritics if needed

    @staticmethod
    def remove_elongation(text):
        """
        Remove elongation (kashida) from the text.
        Kashida (ـ) is often used to stretch words for emphasis or style. It does not affect meaning.
        Example: "الحــب" becomes "الحب".
        Removing elongation simplifies text representation.
        """
        return re.sub(r'ـ+', '', text)

    @staticmethod
    def remove_hash_symbols(text):
        """
        Remove hash (#) symbols from the text.
        Hashtags are often used in social media but are not part of the linguistic content.
        Example: "#حب" becomes "حب".
        """
        return text.replace('#', '').replace('_', ' ')

    @staticmethod
    def remove_extra_whitespaces(text):
        """
        Remove extra whitespaces from the text.
        This step ensures that multiple spaces are replaced by a single space, and leading/trailing spaces are removed.
        Example: "  أحب   البرمجة " becomes "أحب البرمجة".
        Clean and compact text improves processing efficiency.
        """
        return re.sub(r'\s+', ' ', text).strip()

    @staticmethod
    def remove_stop_words(text):
        """
        Remove stop words from the text.
        This ensures that commonly used words which do not add significant meaning are excluded.
        Example: "أنا أحب البرمجة" becomes "أحب البرمجة".
        This step focuses sentiment analysis on the most meaningful words.
        """
        stop_words = Configuration.fetch_data_from_file(Configuration.FileName.stopWordsFileName)

        # Split the text into words
        words = text.split()
        # Remove the stop words
        filtered_words = [word for word in words if word not in stop_words]
        # Join the words back into a string
        return ' '.join(filtered_words)

    @staticmethod
    def preprocess_text(text):
        """
        Full preprocessing pipeline for Arabic text.
        This pipeline combines all the individual preprocessing steps to clean and standardize the input text.
        """
        # Normalize Arabic text to standard form
        text = TextPreprocessor.normalize_arabic_text(text)
        # Remove non-Arabic characters
        text = TextPreprocessor.remove_non_arabic_chars(text)        
        # Remove numbers
        text = TextPreprocessor.remove_numbers(text)
        # Remove special characters
        text = TextPreprocessor.remove_special_chars(text)
        # Remove diacritics
        text = TextPreprocessor.remove_diacritics(text)
        # Remove elongation
        text = TextPreprocessor.remove_elongation(text)
        # Remove hash symbols
        text = TextPreprocessor.remove_hash_symbols(text)
        # Remove extra whitespaces
        text = TextPreprocessor.remove_extra_whitespaces(text)
        # Remove Stop Words
        text = TextPreprocessor.remove_stop_words(text)

        return text
    
def main():
    # Arabic text examples
    examples = [
        "أحببت فيلم كثيراً قصة مؤثرة تمثيل رائع 😍🎥",
        "شعرت خيبة انا أمل خدمة اليوم أتوقع أفضل 😞💔"
    ]

    # Process and display the text
    print("نتائج المعالجة:")
    for example in examples:
        preprocessed_text = TextPreprocessor.preprocess_text(example)
        print("النص الأصلي:", example)
        print("النص بعد المعالجة:", preprocessed_text)
        print("=" * 50)

if __name__ == "__main__":
    main()

