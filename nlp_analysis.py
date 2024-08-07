import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy
from collections import Counter
import json

nlp = spacy.load("en_core_web_sm")

STOPWORDS = set(stopwords.words('english'))
LEMMA = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in STOPWORDS]
    tokens = [LEMMA.lemmatize(word) for word in tokens]
    return " ".join(tokens)

def extract_entities(text):
    doc = nlp(text)
    entities = [(X.text, X.label_) for X in doc.ents]
    return entities

def find_common_words(text, num=10):
    tokens = [word for word in word_tokenize(text.lower()) if word.isalpha() and word not in STOPWORDS]
    common_words = Counter(tokens).most_common(num)
    return common_words

def identify_themes(text):
    common_words = find_common_words(text)
    entities = extract_entities(text)
    themes = {'common_words': common_words, 'named_entities': entities}
    return themes

def generate_interpretation(text):
    themes = identify_themes(text)
    interpretation = f"Based on the common words and named entities, your dream may involve themes such as: {themes['common_words']} and {themes['named_entities']}."
    return interpretation

def export_analysis(dream_text, filepath):
    analysis = {
        'preprocessed_text': preprocess_text(dream_text),
        'themes': identify_themes(dream_text),
        'interpretation': generate_interpretation(dream_text)
    }
    with open(filepath, 'w') as f_out:
        json.dump(analysis, f_out, indent=4)

if __name__ == "__main__":
    dream = "Last night, I dreamt about wandering through a forest with a pack of wolves under the full moon."
    export_analysis(dream, "dream_analysis.json")