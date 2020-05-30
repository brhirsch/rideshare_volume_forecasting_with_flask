from app import app
from internal_services.functions import *
from flask import Flask, render_template,request
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

historical_data = pd.read_csv(r'..\rideshare_webapp\data\historical_data.csv')

@app.route('/')
def home():
    line = create_plot(historical_data, 'Historical Hourly Taxi Volume', 'Date', 'Number of Rides')
    return render_template('home.html', plot=line)