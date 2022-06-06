# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
import requests
import json
import pandas as pd
import numpy as np
from utils.load import get_movies, get_movie_name
from utils.reco import * #get_reco

# Initialization of the Flask App
app = Flask(__name__)

# Index
@app.route('/')
def homepage():
    return render_template('index.html')

# Recommendation homepage
@app.route('/home')
def choose_movies():
    movies = get_movies()
    return render_template('recommendations.html', movies=movies)

# Retrieve recommendations (POST method)
@app.route('/get_recommandations', methods=['POST','GET'])
def get_recommandations():
    recos = []

    # We retrieve the list of mids selected by the user
    list_mid = request.form.getlist("mid")
    print("mid selected:", list_mid)
    
    # We retrieve the list of movie names of the mids selected by the user
    movies = get_movies()
    names = [get_movie_name(mid, movies) for mid in list_mid]

    # When the user clicks on submit
    if request.method == 'POST':
        # TODO: based on the movies selected, populate the variable `recos` with
        # recommendations in the format (mid, name, score)
        pass

    return render_template('recommendations.html', movies=movies, recos=recos, selection=names)
