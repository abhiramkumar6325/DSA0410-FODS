import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

data = {
    'feedback': [
        "This product is great!",
        "I love this product.",
        "The customer service was terrible.",
        "Highly recommended!",
        "Not satisfied with the quality.",
        "Excellent experience with the company.",
        "Will never buy again.",
        "Amazing service!",
        "Poor packaging.",
        "Very disappointed."
    ]
}

df = pd.DataFrame(data)

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

df['preprocessed_feedback'] = df['feedback'].apply(preprocess_text)

word_freq = Counter(word for sublist in df['preprocessed_feedback'] for word in sublist)

N = 5  
top_N_words = word_freq.most_common(N)
print(f"Top {N} most frequent words and their frequencies:")
for word, freq in top_N_words:
    print(f"{word}: {freq}")

words, frequencies = zip(*top_N_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
