import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download("punkt")
nltk.download("stopwords")

def extract_keywords(sentence):
    words = word_tokenize(sentence)

    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    word_freq = FreqDist(filtered_words)

    n = 4
    keywords = word_freq.most_common(n)

    return [keyword[0] for keyword in keywords]