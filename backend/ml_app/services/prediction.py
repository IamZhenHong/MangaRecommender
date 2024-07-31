# Importing necessary libraries
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
import re
import string
import random
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import joblib

def predict(title):
    # Load cosine similarity matrix from .pkl file
    data = pd.read_csv('manga_info.csv')

    indices = pd.Series(data.index, index = data['title'])

    cosine_sim_synopsis = 'ml_app/services/cosine_sim_synopsis.pkl'

    sg = joblib.load(cosine_sim_synopsis)
    
    idx = indices[title]# Get the pairwsie similarity scores 
    sig = list(enumerate(sg[idx]))# Sort the books
    # Extract similarity scores from sig and sort
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
# Scores of the 5 most similar books 
    sig = sig[1:6]# Book indicies
    movie_indices = [i[0] for i in sig]
   
    # Top 5 book recommendation
    rec = data[['title']].iloc[movie_indices]

    return rec
    
    # It reads the top 5 recommend book url and print the images
    
    

predict('Slam Dunk')