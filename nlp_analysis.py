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
    # Using generator to reduce memory consumption
    tokens = (word for word in tokens if word not in STOPWORDS)
    tokens = (LEMMA.lemmatize(word) for word in tokens)
    return " ".join(tokens)

def extract_entities(text):
    doc = nlp(text)
    entities = [(X.text, X.label_) for X in doc.ents]
    return entities

def find_common_words(tokens, num=10):
    common_words = Counter(tokens).most_common(num)
    return common_words

def identify_themes(text):
    tokens = [word.lower() for word in word_tokenize(preprocess_text(text)) if word.isalpha()]
    common_words = find_common_words(tokens)
    entities = extract_entities(" ".join(tokens))
    themes = {'common_words': common_words, 'named_entities': entities}
    return themes

def generate_interpretation(themes):
    interpretation = f"Based on the common words and named entities, your dream may involve themes such as: {themes['common_words']} and {themes['named_entities']}."
    return interpretation

def export_analysis(dream_text, filepath):
    preprocessed_text = preprocess_text(dream_text)
    themes = identify_themes(preprocessed_text)
    interpretation = generate_interpretation(themes)
    analysis = {
        'preprocessed_text': preprocessed_text,
        'themes': themes,
        'interpretation': interpretation
    }
    with open(filepath, 'w') as f_out:
        json.dump(analysis, f_out, indent=4)

if __name__ == "__main__":
    dream = "Last night, I dreamt about wandering through a forest with a pack of wolves under the full moon."
    export_analysis(dream, "dream_analysis.json")