import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download("punkt")
nltk.download("stopwords")

def extract_keywords(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Remove stopwords (common words like "the", "is", "and", etc.)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Calculate word frequency
    word_freq = FreqDist(filtered_words)

    # Get the most common keywords (adjust `n` as needed)
    n = 3  # Number of keywords to extract
    keywords = word_freq.most_common(n)

    return [keyword[0] for keyword in keywords]


# Example usage
sentence = "I am addicted to fentanyl and need help regarding this issue"
keywords = extract_keywords(sentence)
print("Keywords:", keywords)