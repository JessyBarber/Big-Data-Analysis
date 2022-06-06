# -*- coding: utf-8 -*-
import pickle
import numpy as np
import os
from utils.load import get_similarity_scores, get_idx_to_mid, get_mid_to_idx, \
    get_movies, get_movie_name

idx_to_mid = None
mid_to_idx = None
movies = None
similarity_scores = None

def load_files():
    global similarity_scores
    global idx_to_mid
    global mid_to_idx
    global movies
    similarity_scores = get_similarity_scores()
    idx_to_mid = get_idx_to_mid()
    mid_to_idx = get_mid_to_idx()
    movies = get_movies()


def get_sim_scores(list_mids):
    # TODO: Create the function that returns the vector of the similarity
    # scores sims between a movie list `list_mid` and all the other movies
    
    # We get the list of idx from the list of mid
    list_idx = [mid_to_idx[int(id)] for id in list_mids]
    sims = similarity_scores[list_idx]

    # Trick to sum similarities if user selects multiple rows
    sims = np.sum(sims, axis=0)
    
    return sims

def get_ranked_recos(sims):
    # TODO: Create the function that returns for a vector of similarity scores
    # sims the list of all ranked recommendations (n_movies) (from most
    # recommended to least recommended) - in the format list of
    # tuple (mid, score, name)
    
    recos = []
    for idx in np.argsort(-sims):
        mid = idx_to_mid[idx]
        name = get_movie_name(mid, movies)
        score = sims[idx]
        recos.append((mid, score, name))
    return recos

def get_reco(list_mids, N=5, exclude_selection=False):
    # TODO: Create the function that returns a list of N recommendations
    # (in the format list of tuples (mid, score, name))
    # based on a list of mids selected
    # [BONUS]: remove movies selected by user from final recommendations
    # when exclude_selection is set to True
    # We start by loading the files as global variable
    
    if (similarity_scores is None):
        return None
    # Retrieve recommendations
    sims = get_sim_scores(list_mids)
    recos = get_ranked_recos(sims)

    # Exclude selection from results
    if exclude_selection is True:
        recos = [r for r in recos if str(r[0]) not in list_mids]

    # Limiting to N results for display
    recos = recos[:N]
    print("Recommendations:", recos)
    
    return recos
