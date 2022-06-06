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
    pass

def get_ranked_recos(sims):
    # TODO: Create the function that returns for a vector of similarity scores
    # sims the list of all ranked recommendations (n_movies) (from most
    # recommended to least recommended) - in the format list of
    # tuple (mid, score, name)
    pass

def get_reco(list_mids, N=5, exclude_selection=False):
    # TODO: Create the function that returns a list of N recommendations
    # (in the format list of tuples (mid, score, name))
    # based on a list of mids selected
    # [BONUS]: remove movies selected by user from final recommendations
    # when exclude_selection is set to True
    # We start by loading the files as global variable
    pass
