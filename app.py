from textblob import TextBlob
from better_profanity import profanity
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class TextAnalyzer:
    def __init__(self):
        pass

    def check_spelling(self, text):
        blob = TextBlob(text)
        incorrect_spellings = []
        for word in blob.words:
            if word.correct() != word:
                incorrect_spellings.append(word)
        return incorrect_spellings

    def detect_profanity(self, text):
        return profanity.contains_profanity(text)

    def extract_nouns(self, text):
        pattern = r"\b\w[\w'-]*\b"
        words = nltk.regexp_tokenize(text, pattern)
        tagged_words = nltk.pos_tag(words)
        nouns = [word for word, pos in tagged_words if pos.startswith('NN')]
        return sorted(nouns, key=lambda x: (len(x), x))

    def analyze_text(self, text):
        if not text:
            raise ValueError('No text provided')

        incorrect_spellings = self.check_spelling(text)
        contains_profanity = self.detect_profanity(text)
        sorted_nouns = self.extract_nouns(text)

        return {
            'incorrect_spellings': incorrect_spellings,
            'contains_profanity': contains_profanity,
            'sorted_nouns': sorted_nouns
        }

def analyze():
    text = input("Enter text to analyze: ")  # Use input to get text from user
    analyzer = TextAnalyzer()

    try:
        result = analyzer.analyze_text(text)
        
        # Print each section of the result separately
        if result['incorrect_spellings']:
            print("\nincorrect_spellings:")
            for word in result['incorrect_spellings']:
                print(word)
        
        print("\ncontains_profanity:")
        print(result['contains_profanity'])
        
        if result['sorted_nouns']:
            print("\nsorted_nouns:")
            print("[", ", ".join(f"'{noun}'" for noun in result['sorted_nouns']), "]")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    analyze()  # Call analyze function to analyze and print the result
