# -*- coding: utf-8 -*-
import pickle
import numpy as np
import os

DATA_DIR = "../../../data"

def get_idx_to_mid():
    print("Loading idx_to_mid dict")
    with open(os.path.join(DATA_DIR, 'idx_to_mid.pkl'), 'rb') as input:
        idx_to_mid = pickle.load(input)
    return idx_to_mid

def get_mid_to_idx():
    print("Loading mid_to_idx dict")
    with open(os.path.join(DATA_DIR, 'mid_to_idx.pkl'), 'rb') as input:
        mid_to_idx = pickle.load(input)
    return mid_to_idx

def get_movies():
    print("Loading movies dataset as pickle and then transforming it to dict")
    with open(os.path.join(DATA_DIR, 'movies.pkl'), 'rb') as input:
        df_movies = pickle.load(input)
    movies = df_movies[["movieId", "title"]].set_index("movieId")
    movies_dict = movies.to_dict(orient="index")
    return movies_dict

def get_similarity_scores():
    print("Loading model saved as similarity scores")
    with open(os.path.join(DATA_DIR, 'similarity_scores.pkl'), 'rb') as input:
        similarity_scores = pickle.load(input)#.astype(float)
    return similarity_scores

def get_movie_name(mid, movies):
    try:
        name = movies[int(mid)]["title"]
    except:
        name = "Unknown"
    return name
