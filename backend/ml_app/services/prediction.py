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
from google.cloud import storage
import pickle
import os

def download_and_save_pkl(url, filename):
  """Downloads a PKL file from a URL and saves it locally.

  Args:
      url (str): The URL of the PKL file.
      filename (str): The desired filename for the downloaded file.

  Raises:
      requests.exceptions.RequestException: If there's an error downloading the file.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for error HTTP statuses

    # Extract filename from URL or use provided filename (safer)
    if not filename:
      filename = url.split("/")[-1]

    with open(filename, 'wb') as f:
      # Write downloaded content directly to file (more efficient)
      f.write(response.content)

    print(f"Downloaded PKL file: {filename}")

  except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")
def load_pkl_from_grandparent_dir(filename):
  """Loads a PKL file from the grandparent directory.

  Args:
      filename (str): The name of the PKL file.

  Returns:
      The loaded data from the PKL file.
  """

  current_dir = os.path.dirname(__file__)  # Get the current directory
  parent_dir = os.path.dirname(current_dir)  # Get the parent directory
  grandparent_dir = os.path.dirname(parent_dir)  # Get the grandparent directory
  file_path = os.path.join(grandparent_dir, filename)

  with open(file_path, 'rb') as f:
      data = pickle.load(f)
  return data

def predict(title):
    # Load cosine similarity matrix from .pkl file
    data = pd.read_csv('manga_info.csv')

    indices = pd.Series(data.index, index = data['title'])
    url = "https://storage.googleapis.com/mangatracker_model/cosine_sim_synopsis.pkl"
    filename = "downloaded_cosine_sim_synopsis.pkl"  # Choose a desired filename

    
    cosine_sim_synopsis = 'ml_app/services/downloaded_cosine_sim_synopsis.pkl'
    

    sg = joblib.load(cosine_sim_synopsis)
    
    idx = indices[title]# Get the pairwsie similarity scores 
    sig = list(enumerate(sg[idx]))# Sort the books
    # Extract similarity scores from sig and sort
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
# Scores of the 5 most similar books 
    sig = sig[1:10]# Book indicies
    movie_indices = [i[0] for i in sig]
   
    # Top 5 book recommendation
    return data.iloc[movie_indices]
    
    # It reads the top 5 recommend book url and print the images
    
    

predict('Slam Dunk')