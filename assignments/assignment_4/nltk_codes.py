# Assignment 4 - NLP using NLTK

import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk

# Download required resources (run once)
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Sample Text
text = """
Apple is a big technology company based in California.
Tim Cook is the CEO of Apple.
NLP is very interesting and useful in Artificial Intelligence.
"""

print("Original Text:\n", text)

# ------------------------------------------------
# 1. Lowercasing
text_lower = text.lower()
print("\nLowercased Text:\n", text_lower)

# ------------------------------------------------
# 2. Remove Punctuation
text_no_punct = text_lower.translate(str.maketrans('', '', string.punctuation))
print("\nText without Punctuation:\n", text_no_punct)

# ------------------------------------------------
# 3. Tokenization
tokens = word_tokenize(text_no_punct)
print("\nTokens:\n", tokens)

# ------------------------------------------------
# 4. Stop Word Removal
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]
print("\nAfter Stopword Removal:\n", filtered_words)

# ------------------------------------------------
# 5. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("\nStemmed Words:\n", stemmed_words)

# ------------------------------------------------
# 6. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
print("\nLemmatized Words:\n", lemmatized_words)

# ------------------------------------------------
# 7. POS Tagging
pos_tags = pos_tag(tokens)
print("\nPOS Tags:\n", pos_tags)

