'''
   =======================================================================
   
   Copyright 2024 Mohan Krishna G R

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   =======================================================================
'''
import pandas as pd
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt') # for sentence tokenization
nltk.download('stopwords') # for removing stopwords
nltk.download('wordnet') # for lemmatization
nltk.download('averaged_perceptron_tagger') # for POS tagging

stop_words = set(stopwords.words('english')) # stop words
lemmatizer = WordNetLemmatizer() # lemmatizer

def preprocess(text):
    text = text.lower() # Lowercasing 
    tokens = word_tokenize(text) # Tokenizing 
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words] # Removing stopwords and lemmatizing
    processed_text = ' '.join(tokens) # single string
    sentences = nltk.sent_tokenize(processed_text) # Tokenizing into sentences
    pos_tagged_sentences = [' '.join([word for word, pos in pos_tag(word_tokenize(sentence))]) for sentence in sentences] # POS tagging 
    return pos_tagged_sentences # Returning the POS tagged sentences

def generate_summary(text, num_clusters=3):
    sentences = preprocess(text) # Preprocessing the input text

    if len(sentences) < num_clusters: 
        num_clusters = 2  # Adjust number of clusters 
        if len(sentences) < num_clusters:
            num_clusters = 1 # Adjust number of clusters 

    vectorizer = TfidfVectorizer(stop_words='english') # TF-IDF Vectorizer with stopwords
    tfidf_matrix = vectorizer.fit_transform(sentences) # Fitting and transforming sentences into TF-IDF matrix

    kmeans = KMeans(n_clusters=num_clusters) # KMeans 
    kmeans.fit(tfidf_matrix) # Fitting to TF-IDF matrix
    labels = kmeans.labels_ # the cluster labels for each sentence
    
    representative_sentences = [] # Initializing list to store representative sentences

    for i in range(num_clusters): # Iterating over each cluster
        cluster_indices = np.where(labels == i)[0] # Finding indices of sentences in the current cluster
        cluster_vectors = tfidf_matrix[cluster_indices].toarray() # Getting TF-IDF vectors of the current cluster
        centroid = np.mean(cluster_vectors, axis=0) # Calculating the centroid of the cluster
        closest_index = np.argmin(np.linalg.norm(cluster_vectors - centroid, axis=1)) # Finding the index of the sentence closest to the centroid
        representative_sentences.append(sentences[cluster_indices[closest_index]]) # Adding the representative sentence to the list
    return ' '.join(representative_sentences) # Joining and returning the representative sentences as a summary
