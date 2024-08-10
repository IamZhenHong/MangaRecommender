# Importing necessary libraries
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import RegexpTokenizer
import re
import string
import random
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import joblib

nltk.download('stopwords')

# Reading the file
df = pd.read_csv("backend/manga_info.csv")


#Reading the first five records
df.head()

#Checking the shape of the file
print(df.shape)

# # Genre distribution
# df['genre'].value_counts().plot(x = 'genre', y ='count', kind = 'bar', figsize = (10,5)  )

print(df['synopsis'] [2464])

df['word_count'] = df['synopsis'].apply(lambda x: len(str(x).split()))

# Step 2: Plot distribution of word counts
plt.figure(figsize=(10, 6))
plt.hist(df['word_count'], bins=50, color='skyblue', edgecolor='black')
plt.title('Word Count Distribution of Synopsis')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with a 'synopsis' column

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with a 'synopsis' column

# Fill missing values in the 'synopsis' column with an empty string
df['synopsis'].fillna('', inplace=True)

# Initialize the TfidfVectorizer
tf = TfidfVectorizer(ngram_range=(3, 3), stop_words='english', lowercase=False)

# Fit and transform the synopsis to obtain the TF-IDF matrix
tfidf_matrix = tf.fit_transform(df['synopsis'])

# Sum the TF-IDF values for each bigram
total_bigrams = tfidf_matrix.sum(axis=0)

# Create a list of (bigram, frequency) tuples
freq = [(bigram, total_bigrams[0, idx]) for bigram, idx in tf.vocabulary_.items()]

# Sort the list by frequency in descending order
freq = sorted(freq, key=lambda x: x[1], reverse=True)

# Convert the list to a DataFrame
bigram_df = pd.DataFrame(freq)

# Rename the columns
bigram_df.rename(columns={0: 'bigram', 1: 'count'}, inplace=True)

# Take the top 20 bigrams
top_20_bigrams = bigram_df.head(20)

# Plot the bigram distribution
top_20_bigrams.plot(x='bigram', y='count', kind='bar', title="Bigram Distribution for Top 20 Words in the Synopsis",
                    figsize=(15, 7))
plt.xlabel('Bigram')
plt.ylabel('Frequency')
plt.show()


# Function for removing NonAscii characters
def _removeNonAscii(s):
    return "".join(i for i in s if  ord(i)<128)

# Function for converting into lower case
def make_lower_case(text):
    return text.lower()

# Function for removing stop words
def remove_stop_words(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

# Function for removing punctuation
def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text

# Function for removing the html tags
def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

# Applying all the functions in description and storing as a cleaned_desc
df['cleaned_synopsis'] = df['synopsis'].apply(_removeNonAscii)
df['cleaned_synopsis'] = df.cleaned_synopsis.apply(func = make_lower_case)
df['cleaned_synopsis'] = df.cleaned_synopsis.apply(func = remove_stop_words)
df['cleaned_synopsis'] = df.cleaned_synopsis.apply(func=remove_punctuation)
df['cleaned_synopsis'] = df.cleaned_synopsis.apply(func=remove_html)

# Converting the cleaned_synopsis field into vectors using bigrams
tf_synopsis = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df=1, stop_words='english')
tfidf_matrix_synopsis = tf_synopsis.fit_transform(df['cleaned_synopsis'])

# Calculating the similarity measures based on Cosine Similarity
cosine_sim_synopsis = cosine_similarity(tfidf_matrix_synopsis, tfidf_matrix_synopsis)


joblib.dump(cosine_sim_synopsis, 'cosine_sim_synopsis.pkl')