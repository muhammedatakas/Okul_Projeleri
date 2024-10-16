import requests
import re
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Ensure nltk data is available for tokenization
nltk.download('punkt')

# Step 1: Download a Turkish text (Nutuk by Atatürk from Project Gutenberg)
url = 'https://archive.org/stream/capitalvol1/capitalvol1_djvu.txt'
response = requests.get(url)
text = response.text

# Step 2: Preprocess the text - remove non-alphabetic characters and tokenize
def preprocess(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    return tokens

tokens = preprocess(text)

# Step 3: Remove common Turkish stopwords
# You can extend this list of Turkish stop words
stopwords = set(["the", "and", "a", "of", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they", "I", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other", "about", "out", "many", "then", "them", "these",])

filtered_tokens = [word for word in tokens if word not in stopwords]

# Step 4: Generate word frequencies
word_freq = Counter(filtered_tokens)

# Step 5: Generate and plot the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate_from_frequencies(word_freq)

# Step 6: Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of 'Nutuk' by Mustafa Kemal Atatürk")
plt.show()
