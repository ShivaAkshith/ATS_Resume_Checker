import nltk
import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    tokens = nltk.word_tokenize(text)
    cleaned_tokens = [word for word in tokens if word not in stop_words]

    return " ".join(cleaned_tokens)
