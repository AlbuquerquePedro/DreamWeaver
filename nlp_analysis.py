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

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    return [word for word in tokens if word not in STOPWORDS]

def lemmatize_tokens(tokens):
    return [LEMMA.lemmatize(word) for word in tokens]

def preprocess_text(text):
    tokens = tokenize_text(text)
    tokens_no_stops = remove_stopwords(tokens)
    lemmatized_tokens = lemmatize_tokens(tokens_no_stops)
    return " ".join(lemmatized_tokens)

def extract_entities(text):
    doc = nlp(text)
    entities = [(X.text, X.label_) for X in doc.ents]
    return entities

def filter_alpha_tokens(tokens):
    return [word.lower() for word in tokens if word.isalpha()]

def find_common_words(tokens, num=10):
    common_words = Counter(tokens).most_common(num)
    return common_words

def analyze_text_for_themes(text):
    processed_text = preprocess_text(text)
    tokens = tokenize_text(processed_text)
    alpha_tokens = filter_alpha_tokens(tokens)
    common_words = find_common_words(alpha_tokens)
    return common_words, alpha_tokens

def identify_themes(text):
    common_words, alpha_tokens = analyze_text_for_themes(text)
    entities = extract_entities(" ".join(alpha_tokens))
    themes = {'common_words': common_words, 'named_entities': entities}
    return themes

def generate_interpretation(themes):
    interpretation = f"Based on the common words and named entities, your dream may involve themes such as: {themes['common_words']} and {themes['named_entities']}."
    return interpretation

def export_analysis(dream_text, filepath):
    themes = identify_themes(dream_text)
    interpretation = generate_interpretation(themes)
    analysis = {
        'preprocessed_text': preprocess_text(dream_text),
        'themes': themes,
        'interpretation': interpretation
    }
    with open(filepath, 'w') as f_out:
        json.dump(analysis, f_out, indent=4)

if __name__ == "__main__":
    dream = "Last night, I dreamt about wandering through a forest with a pack of wolves under the full moon."
    export_analysis(dream, "dream_analysis.json")